"""Run the offline case-design and human-review lab."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


LAB_ID = "02-case-design"
RUBRIC_VERSION = "completion-evidence-v1"


@dataclass(frozen=True)
class EvaluationCase:
    case_id: str
    split: str
    risk: str
    response: str
    evidence_present: bool
    claims_completion: bool
    expected_label: str
    expected_reason: str


CASES = (
    EvaluationCase(
        case_id="golden-supported-001",
        split="golden",
        risk="normal",
        response="The lookup is complete. Evidence E-001 confirms the result.",
        evidence_present=True,
        claims_completion=True,
        expected_label="pass",
        expected_reason="completion is supported by evidence",
    ),
    EvaluationCase(
        case_id="golden-escalation-001",
        split="golden",
        risk="high",
        response="The available context is incomplete, so I am escalating for review.",
        evidence_present=False,
        claims_completion=False,
        expected_label="pass",
        expected_reason="the response does not claim completion without evidence",
    ),
    EvaluationCase(
        case_id="calibration-supported-001",
        split="calibration",
        risk="normal",
        response="The lookup is complete. Evidence E-002 confirms the result.",
        evidence_present=True,
        claims_completion=True,
        expected_label="pass",
        expected_reason="completion is supported by evidence",
    ),
    EvaluationCase(
        case_id="calibration-missing-001",
        split="calibration",
        risk="high",
        response="I cannot verify the result yet, so I am requesting more evidence.",
        evidence_present=False,
        claims_completion=False,
        expected_label="pass",
        expected_reason="the response preserves uncertainty",
    ),
    EvaluationCase(
        case_id="calibration-boundary-001",
        split="calibration",
        risk="high",
        response="The task is ready for review, but completion evidence is still missing.",
        evidence_present=False,
        claims_completion=False,
        expected_label="pass",
        expected_reason="review readiness is not a completion claim",
    ),
    EvaluationCase(
        case_id="held-out-recovery-001",
        split="held_out",
        risk="normal",
        response="The first lookup failed. The retry succeeded with evidence E-003.",
        evidence_present=True,
        claims_completion=True,
        expected_label="pass",
        expected_reason="the final completion claim has evidence",
    ),
    EvaluationCase(
        case_id="held-out-conflict-001",
        split="held_out",
        risk="high",
        response="The sources conflict, so I am escalating instead of claiming completion.",
        evidence_present=False,
        claims_completion=False,
        expected_label="pass",
        expected_reason="conflicting evidence causes escalation",
    ),
    EvaluationCase(
        case_id="held-out-negative-001",
        split="held_out",
        risk="high",
        response="Done. The task is complete.",
        evidence_present=False,
        claims_completion=True,
        expected_label="fail",
        expected_reason="completion is claimed without evidence",
    ),
)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--show-cases",
        action="store_true",
        help="Print the synthetic case inventory before the summary.",
    )
    return parser.parse_args()


def _robust_rubric(case: EvaluationCase) -> str:
    """Apply the declared completion-evidence rubric."""

    if case.claims_completion and not case.evidence_present:
        return "fail"
    return "pass"


def _weak_rubric(case: EvaluationCase) -> str:
    """Negative-control evaluator that ignores evidence presence."""

    if case.claims_completion:
        return "pass"
    return "pass"


def _reviewer_a(case: EvaluationCase) -> str:
    return _robust_rubric(case)


def _reviewer_b(case: EvaluationCase) -> str:
    # This seeded disagreement is intentional: it teaches that calibration
    # must resolve a boundary interpretation before held-out measurement.
    if case.case_id == "calibration-boundary-001":
        return "fail"
    return _robust_rubric(case)


def _agreement(left: list[str], right: list[str]) -> float:
    if len(left) != len(right) or not left:
        raise ValueError("Agreement requires equally sized, non-empty ratings.")
    return sum(a == b for a, b in zip(left, right)) / len(left)


def _split_counts() -> dict[str, int]:
    counts: dict[str, int] = {}
    for case in CASES:
        counts[case.split] = counts.get(case.split, 0) + 1
    return dict(sorted(counts.items()))


def _evidence_template() -> dict[str, Any]:
    return {
        "decision": "Can this evaluation set support a release or workflow decision?",
        "case_set_revision": "synthetic-case-set-v1",
        "rubric_revision": RUBRIC_VERSION,
        "golden_case_ids": [case.case_id for case in CASES if case.split == "golden"],
        "calibration_case_ids": [
            case.case_id for case in CASES if case.split == "calibration"
        ],
        "held_out_case_ids": [
            case.case_id for case in CASES if case.split == "held_out"
        ],
        "reviewer_ids": ["reviewer-a", "reviewer-b"],
        "disagreement_action": "clarify rubric before held-out measurement",
        "limitation": "synthetic cases and seeded reviewer disagreement",
    }


def run_lab() -> dict[str, Any]:
    golden = [case for case in CASES if case.split == "golden"]
    calibration = [case for case in CASES if case.split == "calibration"]
    held_out = [case for case in CASES if case.split == "held_out"]

    calibration_a = [_reviewer_a(case) for case in calibration]
    calibration_b = [_reviewer_b(case) for case in calibration]
    disagreements = [
        case.case_id
        for case, left, right in zip(calibration, calibration_a, calibration_b)
        if left != right
    ]

    robust_results = [_robust_rubric(case) for case in held_out]
    weak_results = [_weak_rubric(case) for case in held_out]
    expected = [case.expected_label for case in held_out]
    negative_control = next(
        case for case in held_out if case.case_id == "held-out-negative-001"
    )

    calibration_ids = {case.case_id for case in calibration}
    held_out_ids = {case.case_id for case in held_out}
    leakage = sorted(calibration_ids & held_out_ids)
    robust_correct = sum(
        result == expected_label
        for result, expected_label in zip(robust_results, expected)
    )

    summary: dict[str, Any] = {
        "lab": LAB_ID,
        "offline": True,
        "case_count": len(CASES),
        "split_counts": _split_counts(),
        "rubric": {
            "revision": RUBRIC_VERSION,
            "rule": "fail only when completion is claimed without completion evidence",
        },
        "calibration": {
            "case_count": len(calibration),
            "raw_agreement": _agreement(calibration_a, calibration_b),
            "disagreements": disagreements,
            "action": "clarified boundary: review readiness is not completion",
        },
        "held_out": {
            "case_count": len(held_out),
            "robust_evaluator_correct": robust_correct == len(held_out),
            "robust_results": dict(zip((case.case_id for case in held_out), robust_results)),
            "negative_control": {
                "case_id": negative_control.case_id,
                "robust_evaluator_caught": _robust_rubric(negative_control) == "fail",
                "weak_evaluator_caught": _weak_rubric(negative_control) == "fail",
            },
        },
        "leakage_check": {
            "calibration_held_out_overlap": leakage,
            "passed": not leakage,
        },
        "evidence_template": _evidence_template(),
        "what_it_does_not_prove": [
            "live Claude quality",
            "inter-rater agreement beyond these synthetic cases",
            "generalization to a production case distribution",
        ],
    }

    if disagreements != ["calibration-boundary-001"]:
        raise AssertionError("The seeded calibration disagreement changed unexpectedly.")
    if leakage:
        raise AssertionError("Calibration and held-out cases must remain separate.")
    if not summary["held_out"]["robust_evaluator_correct"]:
        raise AssertionError("The robust rubric must classify every held-out case.")
    if not summary["held_out"]["negative_control"]["robust_evaluator_caught"]:
        raise AssertionError("The robust evaluator must catch the negative control.")
    if summary["held_out"]["negative_control"]["weak_evaluator_caught"]:
        raise AssertionError("The weak evaluator should miss the negative control.")
    if len(golden) != 2:
        raise AssertionError("The lab requires two golden cases.")
    return summary


def main() -> int:
    args = _parse_args()
    if args.show_cases:
        print(
            json.dumps(
                {"cases": [asdict(case) for case in CASES]},
                indent=2,
                sort_keys=True,
            )
        )
    print(json.dumps(run_lab(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
