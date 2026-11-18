"""Deterministic RAG failure-decomposition lab using synthetic documents."""

from __future__ import annotations

import json
import math
import re
from collections import Counter
from typing import Iterable


TOKEN_RE = re.compile(r"[a-z0-9]+")
SYNONYMS = {
    "return": "refund",
    "returns": "refund",
    "purchase": "item",
    "purchases": "item",
    "credential": "password",
    "credentials": "password",
}

DOCUMENTS = (
    {
        "id": "refund-current",
        "version": "current",
        "text": "Customers may request a refund within 30 days of purchase.",
    },
    {
        "id": "refund-stale",
        "version": "stale",
        "text": "Customers may request a refund within 14 days of purchase.",
    },
    {
        "id": "password-reset",
        "version": "current",
        "text": "Customers can reset a password using the account recovery link.",
    },
    {
        "id": "refund-unofficial",
        "version": "unofficial",
        "text": "A social post says refunds are always available with no time limit.",
    },
)

QUESTIONS = (
    {
        "id": "q-refund",
        "text": "How long may I return an item?",
        "answerable": True,
        "required_documents": ("refund-current",),
        "expected_claim": "30 days",
    },
    {
        "id": "q-password",
        "text": "How do I recover my credentials?",
        "answerable": True,
        "required_documents": ("password-reset",),
        "expected_claim": "account recovery link",
    },
    {
        "id": "q-crypto",
        "text": "Do you support cryptocurrency payments?",
        "answerable": False,
        "required_documents": (),
        "expected_claim": None,
    },
)


def _tokens(text: str, *, normalize: bool = False) -> list[str]:
    tokens = TOKEN_RE.findall(text.lower())
    if normalize:
        return [SYNONYMS.get(token, token) for token in tokens]
    return tokens


def _bm25_scores(question: str, documents: Iterable[dict]) -> dict[str, float]:
    query = Counter(_tokens(question))
    docs = list(documents)
    document_tokens = {doc["id"]: Counter(_tokens(doc["text"])) for doc in docs}
    document_frequency = Counter(
        token for tokens in document_tokens.values() for token in tokens if token in query
    )
    scores: dict[str, float] = {}
    for doc_id, tokens in document_tokens.items():
        score = 0.0
        for token, query_count in query.items():
            if not tokens[token]:
                continue
            idf = math.log((len(docs) + 1) / (document_frequency[token] + 1)) + 1
            score += idf * min(tokens[token], query_count)
        scores[doc_id] = score
    return scores


def _semantic_scores(question: str, documents: Iterable[dict]) -> dict[str, float]:
    query = set(_tokens(question, normalize=True))
    return {
        doc["id"]: sum(token in query for token in _tokens(doc["text"], normalize=True))
        for doc in documents
    }


def retrieve(question: str, mode: str, k: int = 2) -> list[str]:
    """Return document IDs in descending score order for one declared retriever."""

    if mode == "bm25":
        scores = _bm25_scores(question, DOCUMENTS)
    elif mode == "semantic":
        scores = _semantic_scores(question, DOCUMENTS)
    elif mode == "hybrid":
        lexical = _bm25_scores(question, DOCUMENTS)
        semantic = _semantic_scores(question, DOCUMENTS)
        scores = {
            doc["id"]: lexical[doc["id"]] + semantic[doc["id"]]
            for doc in DOCUMENTS
        }
    else:
        raise ValueError(f"unknown retrieval mode: {mode}")

    ordered = sorted(scores, key=lambda doc_id: (-scores[doc_id], doc_id))
    return ordered[:k]


def _retrieval_result(question: dict, retrieved: list[str]) -> dict:
    required = set(question["required_documents"])
    found = required.intersection(retrieved)
    rank = next(
        (retrieved.index(document_id) + 1 for document_id in required if document_id in retrieved),
        None,
    )
    return {
        "required_documents": sorted(required),
        "retrieved_documents": retrieved,
        "recall_at_k": 1.0 if not required or found == required else 0.0,
        "best_rank": rank,
    }


def _generation_result(question: dict, retrieved: list[str]) -> dict:
    context = [doc for doc in DOCUMENTS if doc["id"] in retrieved]
    cited = retrieved[0] if retrieved else None
    claim = question["expected_claim"]
    claim_supported = (
        not question["answerable"]
        or any(claim and claim in doc["text"] for doc in context)
    )
    wrong_document = bool(
        question["answerable"]
        and retrieved
        and question["required_documents"]
        and retrieved[0] not in question["required_documents"]
    )
    stale_grounding = bool(
        question["answerable"]
        and any(doc["version"] == "stale" for doc in context)
        and not any(
            doc["id"] in question["required_documents"]
            for doc in context
        )
    )
    citation_correct = (
        not question["answerable"]
        or cited in question["required_documents"]
    )
    return {
        "answerable": question["answerable"],
        "claim_supported": claim_supported,
        "citation_correct": citation_correct,
        "wrong_document_grounding": wrong_document,
        "stale_source_grounding": stale_grounding,
    }


def run_lab() -> dict:
    retrieval_results: dict[str, dict[str, dict]] = {}
    for mode in ("bm25", "semantic", "hybrid"):
        retrieval_results[mode] = {
            question["id"]: _retrieval_result(
                question,
                retrieve(question["text"], mode),
            )
            for question in QUESTIONS
        }

    hybrid_answers = {
        question["id"]: _generation_result(
            question,
            retrieve(question["text"], "hybrid"),
        )
        for question in QUESTIONS
    }
    negative_controls = {
        "wrong_document_grounding": _generation_result(
            QUESTIONS[0],
            ["refund-unofficial"],
        ),
        "stale_source_grounding": _generation_result(
            QUESTIONS[0],
            ["refund-stale"],
        ),
        "citation_failure": _generation_result(
            QUESTIONS[0],
            ["password-reset"],
        ),
        "unanswerable_forced_answer": {
            "answerable": False,
            "claim_supported": True,
            "citation_correct": False,
            "wrong_document_grounding": False,
            "stale_source_grounding": False,
        },
    }
    failures = {
        "wrong_document_grounding": negative_controls["wrong_document_grounding"][
            "wrong_document_grounding"
        ],
        "stale_source_grounding": negative_controls["stale_source_grounding"][
            "stale_source_grounding"
        ],
        "citation_failure": not negative_controls["citation_failure"]["citation_correct"],
        "unanswerable_forced_answer": negative_controls["unanswerable_forced_answer"][
            "claim_supported"
        ],
    }
    return {
        "retrieval_results": retrieval_results,
        "hybrid_generation_results": hybrid_answers,
        "negative_controls": negative_controls,
        "failure_decomposition": failures,
        "retrieval_vs_generation_ablations": {
            "retrieval_fixed_generation_degraded": {
                "retrieval_success": True,
                "generation_success": False,
                "diagnosis": "generation failure despite available evidence",
            },
            "generation_fixed_retrieval_degraded": {
                "retrieval_success": False,
                "generation_success": True,
                "diagnosis": "retrieval failure cannot be repaired by a correct generator",
            },
        },
        "candidate_release_decision": "block" if any(failures.values()) else "release",
    }


def main() -> None:
    print(json.dumps(run_lab(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
