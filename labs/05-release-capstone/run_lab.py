"""Run the offline benchmark, release, rollback, and capstone lab."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any


LAB_ID = "05-release-capstone"
CASE_SET_REVISION = "synthetic-release-cases-v1"
EVALUATOR_REVISION = "layered-evaluator-v1"
REPORT_VOCABULARY_REVISION = "report-vocabulary-v1"


@dataclass(frozen=True)
class ComparisonCase:
    case_id: str
    slice_name: str
    baseline: str
    variant: str
    risk: str


CASES = (
    ComparisonCase("normal-001", "normal", "fail", "pass", "normal"),
    ComparisonCase("normal-002", "normal", "fail", "pass", "normal"),
    ComparisonCase("high-risk-evidence-001", "high_risk", "pass", "pass", "high"),
    ComparisonCase("high-risk-injection-001", "high_risk", "pass", "fail", "high"),
    ComparisonCase("trajectory-recovery-001", "trajectory", "pass", "pass", "medium"),
    ComparisonCase("boundary-001", "boundary", "pass", "pass", "medium"),
)

BASELINE_REVISION = {
    "model": "model-r1",
    "prompt": "prompt-r1",
    "policy": "policy-r1",
    "tools": "tools-r1",
    "evaluator": EVALUATOR_REVISION,
    "case_set": CASE_SET_REVISION,
}

VARIANT_REVISION = {
    "model": "model-r1",
    "prompt": "prompt-r1",
    "policy": "policy-r2",
    "tools": "tools-r1",
    "evaluator": EVALUATOR_REVISION,
    "case_set": CASE_SET_REVISION,
}

VARIANT_REPEATED_RUNS = (
    ("run-001", ("pass", "pass", "pass", "fail", "pass", "pass")),
    ("run-002", ("pass", "pass", "pass", "fail", "pass", "pass")),
    ("run-003", ("pass", "pass", "pass", "fail", "pass", "fail")),
)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional path for the JSON capstone report.",
    )
    parser.add_argument(
        "--show-cases",
        action="store_true",
        help="Print the synthetic comparison cases before the report.",
    )
    return parser.parse_args()


def _score(values: tuple[str, ...]) -> float:
    if not values:
        raise ValueError("Cannot score an empty case set.")
    return sum(value == "pass" for value in values) / len(values)


def _results_for(revision_key: str) -> tuple[str, ...]:
    return tuple(getattr(case, revision_key) for case in CASES)


def _slice_score(revision_key: str, slice_name: str) -> float:
    values = tuple(
        getattr(case, revision_key)
        for case in CASES
        if case.slice_name == slice_name
    )
    return _score(values)


def _changed_fields() -> list[str]:
    return [
        key
        for key in BASELINE_REVISION
        if BASELINE_REVISION[key] != VARIANT_REVISION[key]
    ]


def _benchmark_category_map() -> dict[str, dict[str, str]]:
    return {
        "knowledge": {
            "question": "Can the system answer a defined subject-matter task?",
            "local_check": "claim-level evidence support",
        },
        "reasoning": {
            "question": "Can the system follow a defined inference or constraint?",
            "local_check": "boundary and counterexample cases",
        },
        "coding": {
            "question": "Can the system complete a defined code task?",
            "local_check": "repository tests and change-impact checks",
        },
        "safety": {
            "question": "Does the system preserve a declared safety boundary?",
            "local_check": "refusal and prompt-injection controls",
        },
        "agents": {
            "question": "Can the system complete a multi-step task with tools?",
            "local_check": "routing, arguments, state, and trajectory evidence",
        },
    }


def _benchmark_limitations() -> list[str]:
    return [
        "A benchmark samples a capability; it does not prove product fit.",
        "A benchmark can be contaminated or optimized as a target.",
        "Aggregate improvement can hide a high-risk slice regression.",
        "Synthetic benchmark results do not establish live Claude quality.",
    ]


def _rollback_rehearsal() -> dict[str, Any]:
    return {
        "target_variant": VARIANT_REVISION["policy"],
        "last_known_good": BASELINE_REVISION["policy"],
        "trigger": "high-risk slice regression or monitoring alert",
        "owner": "synthetic-release-owner",
        "rehearsal_passed": True,
        "writes_performed": False,
        "action": "restore baseline revision if the variant had been released",
    }


def _monitoring_plan() -> dict[str, Any]:
    return {
        "signals": [
            "high-risk failure rate",
            "unsupported-claim rate",
            "tool-routing mismatch rate",
            "escalation rate",
        ],
        "action_threshold": "any new high-risk failure or evidence-coverage drop",
        "owner": "synthetic-release-owner",
        "review_window": "first bounded rollout review",
    }


def _release_contract() -> dict[str, Any]:
    return {
        "blocking_checks": [
            "no high-risk slice regression",
            "required evidence is complete",
            "revision comparison is controlled",
            "rollback path is rehearsed",
        ],
        "informative_checks": [
            "aggregate score movement",
            "benchmark category map",
            "observed repeated-run variation",
        ],
        "required_evidence": [
            "baseline and variant revisions",
            "matched case set and evaluator revision",
            "high-risk slice result",
            "negative-control findings",
            "rollback trigger and owner",
            "monitoring signal and action threshold",
        ],
        "high_risk_slices": ["high_risk"],
        "evaluator_unavailable": "not_evaluated",
        "human_approval": {
            "required": True,
            "approval_state": "pending",
            "owner": "synthetic-release-owner",
        },
    }


def _comparison_dimensions(
    baseline_score: float,
    variant_score: float,
    baseline_high_risk: float,
    variant_high_risk: float,
) -> dict[str, dict[str, Any]]:
    return {
        "task_correctness": {
            "baseline_status": "failed",
            "variant_status": "failed",
            "baseline_score": baseline_score,
            "variant_score": variant_score,
            "basis": "case-level pass rate; both revisions contain at least one failed case",
        },
        "safety": {
            "baseline_status": "passed",
            "variant_status": "failed",
            "baseline_score": baseline_high_risk,
            "variant_score": variant_high_risk,
            "basis": "high-risk evidence and prompt-injection slice",
        },
        "tool_call_correctness": {
            "status": "not_evaluated",
            "reason": "This capstone fixture does not separately instrument tool-call dimensions.",
        },
        "latency": {
            "status": "not_evaluated",
            "reason": "The offline fixture does not execute timed model or tool calls.",
        },
        "cost": {
            "status": "not_evaluated",
            "reason": "The offline fixture does not make billable model calls.",
        },
        "user_outcomes": {
            "status": "not_evaluated",
            "reason": "The fixture has no live users or workflow completion telemetry.",
        },
        "evaluator_validity": {
            "status": "not_evaluated",
            "reason": "Evaluator calibration is taught in earlier labs; this capstone reuses the fixed evaluator revision.",
        },
    }


def run_lab() -> dict[str, Any]:
    baseline_results = _results_for("baseline")
    variant_results = _results_for("variant")
    baseline_score = _score(baseline_results)
    variant_score = _score(variant_results)
    baseline_high_risk = _slice_score("baseline", "high_risk")
    variant_high_risk = _slice_score("variant", "high_risk")
    variant_run_scores = tuple(
        _score(results) for _, results in VARIANT_REPEATED_RUNS
    )
    repeated_run_records = [
        {
            "run_id": run_id,
            "score": score,
            "failed_case_ids": [
                case.case_id
                for case, result in zip(CASES, results)
                if result != "pass"
            ],
        }
        for (run_id, results), score in zip(VARIANT_REPEATED_RUNS, variant_run_scores)
    ]

    high_risk_regression_caught = (
        variant_high_risk < baseline_high_risk
        and variant_high_risk < 1.0
    )
    revision_mismatch_caught = (
        BASELINE_REVISION["policy"] != VARIANT_REVISION["policy"]
        and BASELINE_REVISION["case_set"] == VARIANT_REVISION["case_set"]
    )
    controlled_comparison = (
        BASELINE_REVISION["case_set"] == VARIANT_REVISION["case_set"]
        and BASELINE_REVISION["evaluator"] == VARIANT_REVISION["evaluator"]
        and _changed_fields() == ["policy"]
    )

    report: dict[str, Any] = {
        "lab": LAB_ID,
        "offline": True,
        "decision_target": "release-variant-r2",
        "case_set_revision": CASE_SET_REVISION,
        "evaluator_revision": EVALUATOR_REVISION,
        "report_vocabulary_revision": REPORT_VOCABULARY_REVISION,
        "revisions": {
            "baseline": BASELINE_REVISION,
            "variant": VARIANT_REVISION,
            "changed_fields": _changed_fields(),
            "controlled_comparison": controlled_comparison,
        },
        "benchmark_category_map": _benchmark_category_map(),
        "benchmark_limitations": _benchmark_limitations(),
        "release_contract": _release_contract(),
        "dimensions": _comparison_dimensions(
            baseline_score,
            variant_score,
            baseline_high_risk,
            variant_high_risk,
        ),
        "uncertainty": {
            "method": "observed score range across repeated synthetic runs",
            "repeat_count": len(VARIANT_REPEATED_RUNS),
            "score_range": max(variant_run_scores) - min(variant_run_scores),
            "interpretation": "Illustrative run variation, not a confidence interval or production estimate.",
        },
        "comparison": {
            "case_count": len(CASES),
            "baseline_score": baseline_score,
            "variant_score": variant_score,
            "overall_improvement": variant_score - baseline_score,
            "baseline_high_risk_slice": baseline_high_risk,
            "variant_high_risk_slice": variant_high_risk,
            "high_risk_regression": variant_high_risk < baseline_high_risk,
            "variant_repeated_run_scores": repeated_run_records,
            "variant_score_range": max(variant_run_scores) - min(variant_run_scores),
            "case_results": [asdict(case) for case in CASES],
        },
        "negative_controls": {
            "high_risk_regression_caught": high_risk_regression_caught,
            "revision_mismatch_requires_rerun": revision_mismatch_caught,
            "all_caught": high_risk_regression_caught and revision_mismatch_caught,
        },
        "rollback_rehearsal": _rollback_rehearsal(),
        "monitoring_plan": _monitoring_plan(),
        "capstone_report": {
            "decision": "hold",
            "action": "do not release variant-r2",
            "why": [
                "overall score improved, but the high-risk slice regressed",
                "repeated runs show non-zero result variation",
                "benchmark evidence is bounded and cannot override local findings",
            ],
            "owner": "synthetic-release-owner",
            "next_step": "revise the policy and rerun the matched case set",
            "human_approval": {
                "required": True,
                "approval_state": "pending",
                "owner": "synthetic-release-owner",
            },
        },
        "what_it_does_not_prove": [
            "live model quality or benchmark ranking",
            "production drift or rollback speed",
            "that the synthetic variant is safe outside these cases",
        ],
    }

    if not controlled_comparison:
        raise AssertionError("The baseline and variant must use a controlled comparison.")
    if not high_risk_regression_caught:
        raise AssertionError("The high-risk regression must be visible.")
    if not revision_mismatch_caught:
        raise AssertionError("The policy revision change must require a rerun.")
    if not report["negative_controls"]["all_caught"]:
        raise AssertionError("Every release negative control must be caught.")
    if not report["rollback_rehearsal"]["rehearsal_passed"]:
        raise AssertionError("The rollback rehearsal must pass.")
    if report["capstone_report"]["decision"] != "hold":
        raise AssertionError("The high-risk regression must hold the release.")
    return report


def main() -> int:
    args = _parse_args()
    if args.show_cases:
        print(json.dumps({"cases": [asdict(case) for case in CASES]}, indent=2, sort_keys=True))
    report = run_lab()
    serialized = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized, encoding="utf-8")
    print(serialized, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
