# Optional Lab: Decompose RAG Failures 🔎

RAG means retrieval-augmented generation: the system retrieves source material
before generating an answer. This lab separates retrieval failure from generation
failure so a final answer score does not hide the cause.

## Run it

```bash
uv run python labs/optional-rag-failure-decomposition/run_lab.py
```

The lab is offline, deterministic, and uses only synthetic documents. It does not
need a provider key.

## What it evaluates

- BM25-style lexical retrieval;
- a transparent toy semantic retriever using a declared synonym map;
- hybrid retrieval;
- recall@k and rank position;
- chunk and context assembly choices;
- citation correctness;
- wrong-document grounding;
- stale and conflicting sources;
- answerable and unanswerable questions; and
- retrieval-versus-generation ablations.

The semantic retriever is deliberately small. It teaches the evaluation boundary;
it is not a production embedding model.

## What to inspect

The report separates:

1. retrieval evidence — did the needed document appear in the top-k results?
2. context evidence — did the assembled context include the right and current source?
3. generation evidence — did the answer use the available evidence?
4. citation evidence — do cited identifiers support the claims?

The negative controls include a wrong-document answer, a stale-source answer, and
an unanswerable question. The expected result is a blocked candidate release
because a passing final answer alone cannot erase retrieval or citation failures.

## What this proves

The lab demonstrates a reproducible failure decomposition and shows why recall,
grounding, and citation correctness must be measured separately.

## What this does not prove

The toy retrievers do not establish production retrieval quality, embedding-model
quality, user satisfaction, or a provider ranking. A production study needs a
representative corpus, frozen chunking policy, held-out questions, and a declared
human or expert reference.
