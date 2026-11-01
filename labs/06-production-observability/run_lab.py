"""Run the offline production-observability contract lab."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


LAB_ID = "06-production-observability"
TRACE_SCHEMA_REVISION = "agent-trace-contract-v1"
EVALUATOR_REVISION = "observability-controls-v1"


@dataclass(frozen=True)
class Span:
    span_id: str
    kind: str
    name: str
    duration_ms: int
    status: str
    attributes: dict[str, Any]


@dataclass(frozen=True)
class Trace:
    trace_id: str
    session_id: str
    workflow_name: str
    model_revision: str
    agent_revision: str
    terminal_state: str | None
    redaction_status: str
    spans: tuple[Span, ...]
    total_tokens: int
    estimated_cost_usd: float
    retry_count: int
    expected_decision: str = "pass"


def _trace(
    trace_id: str,
    *,
    terminal_state: str | None = "completed",
    redaction_status: str = "redacted",
    spans: tuple[Span, ...],
    total_tokens: int = 420,
    estimated_cost_usd: float = 0.04,
    retry_count: int = 0,
    expected_decision: str = "pass",
) -> Trace:
    return Trace(
        trace_id=trace_id,
        session_id=f"session-{trace_id.removesuffix('-001')}",
        workflow_name="synthetic-support-agent",
        model_revision="claude-synthetic-r1",
        agent_revision="agent-policy-r1",
        terminal_state=terminal_state,
        redaction_status=redaction_status,
        spans=spans,
        total_tokens=total_tokens,
        estimated_cost_usd=estimated_cost_usd,
        retry_count=retry_count,
        expected_decision=expected_decision,
    )


def _span(
    span_id: str,
    kind: str,
    name: str,
    *,
    duration_ms: int = 20,
    status: str = "ok",
    **attributes: Any,
) -> Span:
    return Span(
        span_id=span_id,
        kind=kind,
        name=name,
        duration_ms=duration_ms,
        status=status,
        attributes=attributes,
    )


def _traces() -> tuple[Trace, ...]:
    return (
        _trace(
            "trace-healthy-001",
            spans=(
                _span("span-001", "workflow", "agent.run", decision="support"),
                _span(
                    "span-002",
                    "model",
                    "model.generate",
                    model="claude-synthetic",
                    input_tokens=180,
                    output_tokens=240,
                ),
                _span(
                    "span-003",
                    "tool",
                    "tool.lookup_status",
                    tool_authorized=True,
                    result_status="ok",
                ),
                _span(
                    "span-004",
                    "state",
                    "state.verify",
                    before="pending",
                    after="verified",
                ),
                _span("span-005", "event", "agent.terminal", terminal_state="completed"),
            ),
        ),
        _trace(
            "trace-unauthorized-tool-001",
            spans=(
                _span("span-101", "workflow", "agent.run", decision="support"),
                _span(
                    "span-102",
                    "tool",
                    "tool.update_record",
                    tool_authorized=False,
                    result_status="ok",
                ),
                _span("span-103", "event", "agent.terminal", terminal_state="completed"),
            ),
            expected_decision="fail",
        ),
        _trace(
            "trace-missing-terminal-001",
            terminal_state=None,
            spans=(
                _span("span-201", "workflow", "agent.run", decision="support"),
                _span("span-202", "model", "model.generate", input_tokens=180, output_tokens=240),
            ),
            expected_decision="not_evaluated",
        ),
        _trace(
            "trace-cost-spike-001",
            total_tokens=18_000,
            estimated_cost_usd=2.40,
            spans=(
                _span("span-301", "workflow", "agent.run", decision="support"),
                _span(
                    "span-302",
                    "model",
                    "model.generate",
                    input_tokens=9_000,
                    output_tokens=9_000,
                ),
                _span("span-303", "event", "agent.terminal", terminal_state="completed"),
            ),
            expected_decision="fail",
        ),
        _trace(
            "trace-retry-loop-001",
            retry_count=5,
            spans=(
                _span("span-401", "workflow", "agent.run", decision="support"),
                _span(
                    "span-402",
                    "tool",
                    "tool.lookup_status",
                    tool_authorized=True,
                    result_status="error",
                ),
                _span(
                    "span-403",
                    "tool",
                    "tool.lookup_status",
                    tool_authorized=True,
                    result_status="error",
                ),
                _span("span-404", "event", "agent.terminal", terminal_state="failed"),
            ),
            expected_decision="fail",
        ),
        _trace(
            "trace-raw-content-001",
            redaction_status="raw",
            spans=(
                _span("span-501", "workflow", "agent.run", decision="support"),
                _span("span-502", "model", "model.generate", input_tokens=180, output_tokens=240),
                _span("span-503", "event", "agent.terminal", terminal_state="completed"),
            ),
            expected_decision="fail",
        ),
    )


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional path for the JSON observability report.",
    )
    parser.add_argument(
        "--show-traces",
        action="store_true",
        help="Print the synthetic trace inventory before the report.",
    )
    return parser.parse_args()


def _span_names(trace: Trace) -> list[str]:
    return [span.name for span in trace.spans]


def _evaluate_trace(trace: Trace) -> dict[str, Any]:
    findings: list[dict[str, str]] = []
    span_names = _span_names(trace)

    if trace.terminal_state is None:
        return {
            "status": "not_evaluated",
            "reason_code": "terminal_state_missing",
            "trace_id": trace.trace_id,
            "span_names": span_names,
        }

    if trace.redaction_status != "redacted":
        findings.append({"reason_code": "content_redaction_incomplete"})

    tool_spans = [span for span in trace.spans if span.kind == "tool"]
    if any(not span.attributes.get("tool_authorized", False) for span in tool_spans):
        findings.append({"reason_code": "unauthorized_tool_observed"})

    if trace.estimated_cost_usd > 1.00:
        findings.append({"reason_code": "spend_budget_exceeded"})

    if trace.retry_count > 3:
        findings.append({"reason_code": "retry_loop_exceeded"})

    if findings:
        return {
            "status": "fail",
            "reason_code": (
                findings[0]["reason_code"]
                if len(findings) == 1
                else "multiple_observability_findings"
            ),
            "findings": findings,
            "trace_id": trace.trace_id,
            "span_names": span_names,
        }

    return {
        "status": "pass",
        "reason_code": "trace_contract_and_operational_controls_passed",
        "trace_id": trace.trace_id,
        "span_names": span_names,
    }


def _metrics(traces: tuple[Trace, ...]) -> dict[str, Any]:
    completed = [trace for trace in traces if trace.terminal_state == "completed"]
    return {
        "trace_count": len(traces),
        "completed_trace_count": len(completed),
        "total_tokens": sum(trace.total_tokens for trace in traces),
        "estimated_cost_usd": round(
            sum(trace.estimated_cost_usd for trace in traces),
            2,
        ),
        "retry_count_total": sum(trace.retry_count for trace in traces),
        "tool_span_count": sum(
            sum(span.kind == "tool" for span in trace.spans) for trace in traces
        ),
    }


def _incident_findings(results: dict[str, dict[str, Any]]) -> list[dict[str, str]]:
    return [
        {
            "trace_id": trace_id,
            "severity": "high" if result["reason_code"] == "unauthorized_tool_observed" else "medium",
            "action": "hold_and_investigate",
            "reason_code": result["reason_code"],
        }
        for trace_id, result in results.items()
        if result["status"] == "fail"
    ]


def _trace_to_case(results: dict[str, dict[str, Any]]) -> list[dict[str, str]]:
    return [
        {
            "trace_id": trace_id,
            "case_id": f"regression-{trace_id}",
            "next_evaluator": result["reason_code"],
            "decision": "add_to_regression_set",
        }
        for trace_id, result in results.items()
        if result["status"] == "fail"
    ]


def run_lab() -> dict[str, Any]:
    traces = _traces()
    results = {trace.trace_id: _evaluate_trace(trace) for trace in traces}
    expected_failures = [
        trace.trace_id
        for trace in traces
        if trace.expected_decision in {"fail", "not_evaluated"}
    ]
    caught_failures = [
        trace_id
        for trace_id in expected_failures
        if results[trace_id]["status"] == {
            "fail": "fail",
            "not_evaluated": "not_evaluated",
        }[_trace_by_id(traces, trace_id).expected_decision]
    ]
    suite_passed = set(caught_failures) == set(expected_failures)

    report: dict[str, Any] = {
        "lab_id": LAB_ID,
        "trace_schema_revision": TRACE_SCHEMA_REVISION,
        "evaluator_revision": EVALUATOR_REVISION,
        "execution_state": "completed",
        "observability_suite_status": "passed" if suite_passed else "failed",
        "case_results": results,
        "metrics": _metrics(traces),
        "incident_findings": _incident_findings(results),
        "trace_to_case": _trace_to_case(results),
        "negative_controls": {
            "expected_failures": expected_failures,
            "caught_failures": caught_failures,
        },
        "candidate_release_decision": "block" if suite_passed else "not_evaluated",
        "evidence_template": {
            "trace_ids": list(results),
            "required_trace_fields": [
                "trace_id",
                "session_id",
                "workflow_name",
                "model_revision",
                "agent_revision",
                "span_id",
                "span_kind",
                "terminal_state",
                "redaction_status",
            ],
            "operational_signals": [
                "latency_ms",
                "total_tokens",
                "estimated_cost_usd",
                "retry_count",
                "tool_authorization",
            ],
            "privacy_boundary": "synthetic identifiers and redacted content only",
        },
        "limitations": [
            "The trace fields are OpenTelemetry-shaped teaching metadata, not a live exporter.",
            "The metrics use synthetic values and do not establish production SLOs.",
            "The lab does not prove live Claude quality, security, or incident response readiness.",
        ],
    }
    return report


def _trace_by_id(traces: tuple[Trace, ...], trace_id: str) -> Trace:
    for trace in traces:
        if trace.trace_id == trace_id:
            return trace
    raise KeyError(trace_id)


def main() -> int:
    args = _parse_args()
    traces = _traces()
    if args.show_traces:
        print(json.dumps([asdict(trace) for trace in traces], indent=2))
    report = run_lab()
    if args.output:
        args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    return 0 if report["observability_suite_status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
