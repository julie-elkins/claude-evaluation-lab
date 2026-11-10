"""Run the offline automated-evaluator layers lab."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from typing import Any


LAB_ID = "03-automated-evaluators"
JUDGE_REVISION = "synthetic-judge-v1"
QUESTION_SET_REVISION = "question-contract-v1"
QUESTION_SCORE_THRESHOLD = 0.8


@dataclass(frozen=True)
class EvaluationCase:
    case_id: str
    schema_valid: bool
    evidence_present: bool
    claims_completion: bool
    expected_decision: str
    tool_values_accurate: bool = True
    answer_quality: str = "complete"


@dataclass(frozen=True)
class EvaluationQuestion:
    question_id: str
    question_type: str
    construct: str
    weight: float
    blocking: bool
    evidence_ids: tuple[str, ...]


QUESTIONS = (
    EvaluationQuestion(
        question_id="completion-support",
        question_type="binary",
        construct="completion claims are supported by observed evidence",
        weight=0.45,
        blocking=True,
        evidence_ids=("response-text", "completion-evidence"),
    ),
    EvaluationQuestion(
        question_id="tool-faithfulness",
        question_type="binary",
        construct="reported tool-derived values match tool output",
        weight=0.35,
        blocking=True,
        evidence_ids=("tool-output", "response-text"),
    ),
    EvaluationQuestion(
        question_id="final-answer-completeness",
        question_type="ordered",
        construct="final answer meets the declared task outcome",
        weight=0.20,
        blocking=False,
        evidence_ids=("response-text", "task-contract"),
    ),
)

OVERLAP_PROBE_QUESTIONS = (
    EvaluationQuestion(
        question_id="completion-support",
        question_type="binary",
        construct="completion claims are supported by observed evidence",
        weight=0.50,
        blocking=True,
        evidence_ids=("completion-evidence",),
    ),
    EvaluationQuestion(
        question_id="completion-support-duplicate",
        question_type="binary",
        construct="completion claims are supported by observed evidence",
        weight=0.50,
        blocking=True,
        evidence_ids=("completion-evidence",),
    ),
)


CASES = (
    EvaluationCase(
        case_id="supported-001",
        schema_valid=True,
        evidence_present=True,
        claims_completion=True,
        expected_decision="pass",
    ),
    EvaluationCase(
        case_id="malformed-001",
        schema_valid=False,
        evidence_present=True,
        claims_completion=True,
        expected_decision="fail",
    ),
    EvaluationCase(
        case_id="incomplete-001",
        schema_valid=True,
        evidence_present=True,
        claims_completion=True,
        expected_decision="fail",
    ),
    EvaluationCase(
        case_id="unsupported-001",
        schema_valid=True,
        evidence_present=False,
        claims_completion=True,
        expected_decision="fail",
    ),
    EvaluationCase(
        case_id="partial-001",
        schema_valid=True,
        evidence_present=True,
        claims_completion=True,
        expected_decision="pass",
        answer_quality="partial",
    ),
    EvaluationCase(
        case_id="tool-mismatch-001",
        schema_valid=True,
        evidence_present=True,
        claims_completion=True,
        expected_decision="fail",
        tool_values_accurate=False,
    ),
    EvaluationCase(
        case_id="escalation-001",
        schema_valid=True,
        evidence_present=False,
        claims_completion=False,
        expected_decision="pass",
    ),
)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--show-cases",
        action="store_true",
        help="Print the synthetic evaluator cases before the summary.",
    )
    return parser.parse_args()


def _contract_check(case: EvaluationCase) -> dict[str, Any]:
    if not case.schema_valid:
        return {
            "status": "fail",
            "reason_code": "schema_invalid",
            "evidence": ["schema-check"],
        }
    return {
        "status": "pass",
        "reason_code": "schema_valid",
        "evidence": ["schema-check"],
    }


def _synthetic_judge(case: EvaluationCase) -> str:
    """Return a parseable but intentionally fallible judge result."""

    if not case.schema_valid:
        return "{not-json"
    if case.case_id == "incomplete-001":
        return json.dumps({"decision": "pass"})
    # This teaching judge intentionally passes every valid-shaped output so the
    # independent semantic check can expose its false pass.
    decision = "pass"
    reason_code = "fluent-completion" if case.claims_completion else "escalation-language"
    return json.dumps(
        {
            "decision": decision,
            "reason_code": reason_code,
            "judge_revision": JUDGE_REVISION,
            "evidence_ids": ["response-text"],
        }
    )


def _parse_judge_output(raw: str) -> dict[str, Any]:
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError:
        return {
            "status": "not_evaluated",
            "parseable": False,
            "valid": False,
            "decision": None,
            "reason_code": "malformed_json",
        }

    if not isinstance(parsed, dict) or parsed.get("decision") not in {"pass", "fail"}:
        return {
            "status": "not_evaluated",
            "parseable": False,
            "valid": False,
            "decision": None,
            "reason_code": "schema_invalid",
        }

    required_fields = {"reason_code", "judge_revision", "evidence_ids"}
    missing_fields = sorted(required_fields - parsed.keys())
    if missing_fields:
        return {
            "status": "not_evaluated",
            "parseable": True,
            "valid": False,
            "decision": None,
            "reason_code": "schema_incomplete",
            "missing_fields": missing_fields,
        }

    if (
        not isinstance(parsed["reason_code"], str)
        or not isinstance(parsed["judge_revision"], str)
        or not isinstance(parsed["evidence_ids"], list)
        or not all(isinstance(item, str) for item in parsed["evidence_ids"])
    ):
        return {
            "status": "not_evaluated",
            "parseable": True,
            "valid": False,
            "decision": None,
            "reason_code": "schema_invalid",
        }

    return {
        "status": "passed",
        "parseable": True,
        "valid": True,
        "decision": parsed["decision"],
        "reason_code": parsed["reason_code"],
        "judge_revision": parsed["judge_revision"],
        "evidence_ids": parsed["evidence_ids"],
    }


def _independent_semantic_check(case: EvaluationCase) -> dict[str, Any]:
    if case.claims_completion and not case.evidence_present:
        return {
            "status": "fail",
            "reason_code": "completion_without_evidence",
            "evidence": ["independent-evidence-check"],
        }
    return {
        "status": "pass",
        "reason_code": "semantic_contract_satisfied",
        "evidence": ["independent-evidence-check"],
    }


def _question_answer(case: EvaluationCase, question_id: str) -> tuple[str, float]:
    if question_id == "completion-support":
        supported = not case.claims_completion or case.evidence_present
        return ("yes" if supported else "no", 1.0 if supported else 0.0)
    if question_id == "tool-faithfulness":
        return (
            "yes" if case.tool_values_accurate else "no",
            1.0 if case.tool_values_accurate else 0.0,
        )
    if question_id == "final-answer-completeness":
        scores = {"complete": 1.0, "partial": 0.5, "none": 0.0}
        if case.answer_quality not in scores:
            raise AssertionError(f"Unknown answer quality: {case.answer_quality}")
        return (case.answer_quality, scores[case.answer_quality])
    raise AssertionError(f"Unknown question: {question_id}")


def _question_level_evaluation(case: EvaluationCase) -> dict[str, Any]:
    results: list[dict[str, Any]] = []
    weighted_score = 0.0
    blocking_failures: list[str] = []

    for question in QUESTIONS:
        answer, score = _question_answer(case, question.question_id)
        status = "pass" if score == 1.0 else "partial" if score > 0.0 else "fail"
        weighted_score += question.weight * score
        if question.blocking and score < 1.0:
            blocking_failures.append(question.question_id)
        results.append(
            {
                "question_id": question.question_id,
                "question_type": question.question_type,
                "construct": question.construct,
                "answer": answer,
                "probability": score,
                "score": score,
                "weight": question.weight,
                "weighted_score": round(question.weight * score, 2),
                "blocking": question.blocking,
                "status": status,
                "evidence_ids": list(question.evidence_ids),
            }
        )

    overall_score = round(weighted_score, 2)
    decision = (
        "pass"
        if not blocking_failures and overall_score >= QUESTION_SCORE_THRESHOLD
        else "fail"
    )
    return {
        "status": "evaluated",
        "question_set_revision": QUESTION_SET_REVISION,
        "score_threshold": QUESTION_SCORE_THRESHOLD,
        "questions": results,
        "overall_score": overall_score,
        "blocking_failures": blocking_failures,
        "decision": decision,
    }


def _question_overlap_audit() -> dict[str, Any]:
    by_construct: dict[str, list[str]] = {}
    for question in OVERLAP_PROBE_QUESTIONS:
        by_construct.setdefault(question.construct, []).append(question.question_id)

    overlapping_groups = [
        question_ids
        for question_ids in by_construct.values()
        if len(question_ids) > 1
    ]
    return {
        "status": "warning" if overlapping_groups else "pass",
        "question_set_revision": QUESTION_SET_REVISION,
        "overlapping_question_groups": overlapping_groups,
        "action": (
            "review whether one failure would be charged twice before using "
            "the question set as a release gate"
            if overlapping_groups
            else "no duplicate constructs detected"
        ),
    }


def _calibration_report() -> dict[str, Any]:
    return {
        "status": "not_measured",
        "case_ids_for_independent_review": [
            "supported-001",
            "partial-001",
            "unsupported-001",
            "tool-mismatch-001",
        ],
        "per_question_agreement": None,
        "required_before_live_use": True,
        "reason": (
            "This offline lab has no independent human labels. Its question "
            "scores demonstrate the report shape, not evaluator validity."
        ),
    }


def _pairwise_judge(presented: tuple[str, str]) -> str:
    """Synthetic judge that always prefers the first position."""

    return presented[0]


def _bias_probe() -> dict[str, Any]:
    first_order = ("candidate-a", "candidate-b")
    reversed_order = ("candidate-b", "candidate-a")
    first_preference = _pairwise_judge(first_order)
    reversed_preference = _pairwise_judge(reversed_order)
    return {
        "first_order": {
            "presented": list(first_order),
            "preferred": first_preference,
        },
        "reversed_order": {
            "presented": list(reversed_order),
            "preferred": reversed_preference,
        },
        "position_bias_detected": first_preference != reversed_preference,
        "action": "do not use this pairwise judge as a release gate",
    }


def run_lab() -> dict[str, Any]:
    layers: dict[str, Any] = {}
    false_passes: list[str] = []
    contract_failures: list[str] = []
    negative_control_id = "unsupported-001"

    for case in CASES:
        contract = _contract_check(case)
        judge = _parse_judge_output(_synthetic_judge(case))
        independent = _independent_semantic_check(case)
        question_level = (
            _question_level_evaluation(case)
            if contract["status"] == "pass" and judge["valid"]
            else {
                "status": "not_evaluated",
                "reason": "contract or judge output was not valid evidence",
            }
        )
        layers[case.case_id] = {
            "expected_decision": case.expected_decision,
            "contract": contract,
            "judge": judge,
            "independent_semantic_check": independent,
            "question_level": question_level,
        }
        if contract["status"] == "fail" or not judge["valid"]:
            contract_failures.append(case.case_id)
        if (
            judge.get("valid")
            and judge.get("decision") == "pass"
            and independent["status"] == "fail"
        ):
            false_passes.append(case.case_id)

    bias_probe = _bias_probe()
    overlap_audit = _question_overlap_audit()
    calibration = _calibration_report()
    negative_control = layers[negative_control_id]
    summary: dict[str, Any] = {
        "lab": LAB_ID,
        "offline": True,
        "case_count": len(CASES),
        "evaluator_layers": {
            "contract_check": "schema and required-shape validation",
            "synthetic_judge": JUDGE_REVISION,
            "independent_semantic_check": "completion evidence contract",
        },
        "question_contract": {
            "revision": QUESTION_SET_REVISION,
            "score_threshold": QUESTION_SCORE_THRESHOLD,
            "questions": [asdict(question) for question in QUESTIONS],
        },
        "case_results": layers,
        "contract_failures": contract_failures,
        "judge_contract_failures": contract_failures,
        "judge_false_passes": false_passes,
        "negative_control": {
            "case_id": negative_control_id,
            "judge_passed": negative_control["judge"].get("decision") == "pass",
            "independent_check_caught": negative_control["independent_semantic_check"]["status"]
            == "fail",
        },
        "bias_probe": bias_probe,
        "overlap_audit": overlap_audit,
        "calibration": calibration,
        "release_decision": "block",
        "release_reasons": [
            "malformed evaluator output was not parseable",
            "incomplete evaluator output was not valid evidence",
            "semantic judge produced a false pass",
            "pairwise judge changed preference when order changed",
            "the overlap probe found a duplicate construct",
            "question-level calibration was not measured",
        ],
        "what_it_does_not_prove": [
            "live LLM-as-a-judge accuracy",
            "absence of bias beyond the seeded position probe",
            "question-level calibration against independent human labels",
            "that these weights suit another decision",
            "production release readiness",
        ],
    }

    if contract_failures != ["malformed-001", "incomplete-001"]:
        raise AssertionError(
            "The contract layer must catch malformed and incomplete judge output."
        )
    if false_passes != ["unsupported-001"]:
        raise AssertionError("The seeded judge false pass changed unexpectedly.")
    partial = layers["partial-001"]["question_level"]
    if partial["decision"] != "pass" or partial["overall_score"] != 0.9:
        raise AssertionError("The partial-correctness case must retain its score breakdown.")
    tool_mismatch = layers["tool-mismatch-001"]["question_level"]
    if tool_mismatch["blocking_failures"] != ["tool-faithfulness"]:
        raise AssertionError("Tool-faithfulness must remain a blocking question.")
    if not summary["negative_control"]["independent_check_caught"]:
        raise AssertionError("The independent semantic check must catch the negative control.")
    if not bias_probe["position_bias_detected"]:
        raise AssertionError("The position-bias probe must detect the seeded bias.")
    if overlap_audit["status"] != "warning":
        raise AssertionError("The overlap probe must produce a warning.")
    if calibration["status"] != "not_measured":
        raise AssertionError("The lab must not claim human calibration.")
    if summary["release_decision"] != "block":
        raise AssertionError("The layered findings must block this synthetic release.")
    return summary


def main() -> int:
    args = _parse_args()
    if args.show_cases:
        print(
            json.dumps(
                {
                    "cases": [
                        {
                            "case_id": case.case_id,
                            "schema_valid": case.schema_valid,
                            "evidence_present": case.evidence_present,
                            "claims_completion": case.claims_completion,
                            "tool_values_accurate": case.tool_values_accurate,
                            "answer_quality": case.answer_quality,
                            "expected_decision": case.expected_decision,
                        }
                        for case in CASES
                    ]
                },
                indent=2,
                sort_keys=True,
            )
        )
    print(json.dumps(run_lab(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
