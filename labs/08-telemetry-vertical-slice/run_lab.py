"""Run the local, deterministic telemetry vertical-slice lab."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


PIPELINE_REVISION = "local-telemetry-pipeline-v1"
MONITOR_REVISION = "telemetry-monitor-v1"


@dataclass(frozen=True)
class Event:
    event_id: str
    trace_id: str | None
    span_id: str | None
    kind: str
    name: str
    payload: dict[str, Any]


def _events() -> tuple[Event, ...]:
    return (
        Event("event-001", "trace-healthy-001", "span-001", "workflow", "agent.run", {"agent_revision": "agent-r1", "model_revision": "model-r1"}),
        Event("event-002", "trace-healthy-001", "span-002", "model", "model.generate", {"authorized": True, "raw_content": "synthetic-safe"}),
        Event("event-003", "trace-healthy-001", "span-003", "tool", "tool.lookup", {"authorized": True, "raw_content": "synthetic-safe"}),
        Event("event-004", "trace-healthy-001", "span-004", "terminal", "agent.completed", {"terminal_state": "completed"}),
        Event("event-101", "trace-unauthorized-001", "span-101", "model", "model.generate", {"authorized": True, "raw_content": "synthetic-safe"}),
        Event("event-102", "trace-unauthorized-001", "span-102", "tool", "tool.write_record", {"authorized": False, "raw_content": "synthetic-safe"}),
        Event("event-103", "trace-unauthorized-001", "span-103", "terminal", "agent.completed", {"terminal_state": "completed"}),
        Event("event-201", "trace-raw-content-001", "span-201", "model", "model.generate", {"authorized": True, "raw_content": "synthetic-sensitive-value"}),
        Event("event-202", "trace-raw-content-001", "span-202", "terminal", "agent.completed", {"terminal_state": "completed"}),
        Event("event-301", "trace-missing-span-001", "span-301", "workflow", "agent.run", {"authorized": True, "raw_content": "synthetic-safe"}),
        Event("event-302", "trace-missing-span-001", "span-302", "model", "model.generate", {"authorized": True, "raw_content": "synthetic-safe"}),
        Event("event-303", "trace-missing-span-001", None, "terminal", "agent.completed", {"terminal_state": "completed"}),
        Event("event-401", None, "span-401", "tool", "tool.lookup", {"authorized": True, "raw_content": "synthetic-safe"}),
        Event("event-501", "trace-exporter-failure-001", "span-501", "workflow", "agent.run", {"authorized": True, "raw_content": "synthetic-safe"}),
    )


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optional JSON report path.")
    parser.add_argument("--show-stages", action="store_true", help="Print pipeline stages.")
    return parser.parse_args()


def _instrument(events: tuple[Event, ...]) -> list[dict[str, Any]]:
    return [
        {
            "event_id": event.event_id,
            "trace_id": event.trace_id,
            "span_id": event.span_id,
            "kind": event.kind,
            "name": event.name,
            "payload": dict(event.payload),
        }
        for event in events
    ]


def _collect(records: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], dict[str, int]]:
    accepted: list[dict[str, Any]] = []
    health = {"received": len(records), "accepted": 0, "rejected": 0, "dropped": 0}
    for record in records:
        if not record["trace_id"] or not record["span_id"]:
            health["rejected"] += 1
            continue
        if record["trace_id"] == "trace-exporter-failure-001":
            health["dropped"] += 1
            continue
        payload = dict(record["payload"])
        if payload.get("raw_content"):
            payload["raw_content"] = "[REDACTED]"
            payload["redaction_status"] = "redacted"
        record = dict(record)
        record["payload"] = payload
        accepted.append(record)
        health["accepted"] += 1
    return accepted, health


def _query(records: list[dict[str, Any]], health: dict[str, int]) -> dict[str, Any]:
    traces: dict[str, list[dict[str, Any]]] = {}
    for record in records:
        traces.setdefault(record["trace_id"], []).append(record)

    trace_results: dict[str, dict[str, Any]] = {}
    for trace_id, trace_events in traces.items():
        findings: list[str] = []
        if any(event["kind"] == "tool" and event["payload"].get("authorized") is False for event in trace_events):
            findings.append("unauthorized_tool_observed")
        if any(event["payload"].get("raw_content") not in {None, "[REDACTED]"} for event in trace_events):
            findings.append("raw_content_retained")
        if not any(event["kind"] == "terminal" for event in trace_events):
            findings.append("terminal_event_missing")
        if not any(event["kind"] == "model" for event in trace_events):
            findings.append("model_span_missing")
        incomplete = any(
            code in {"terminal_event_missing", "model_span_missing"}
            for code in findings
        )
        trace_results[trace_id] = {
            "status": "not_evaluated" if incomplete else ("failed" if findings else "passed"),
            "reason_codes": findings or ["telemetry_contract_passed"],
            "event_count": len(trace_events),
        }

    telemetry_health = {
        **health,
        "pipeline_status": "unavailable" if health["dropped"] or health["rejected"] else "available",
    }
    alerts = [
        {
            "alert_id": "alert-telemetry-loss-001",
            "status": "triggered",
            "reason": "telemetry_records_rejected_or_dropped",
            "action": "mark_evidence_unavailable_and_investigate",
        }
    ] if health["dropped"] or health["rejected"] else []
    return {"trace_results": trace_results, "telemetry_health": telemetry_health, "alerts": alerts}


def run_lab() -> dict[str, Any]:
    events = _events()
    instrumented = _instrument(events)
    stored, health = _collect(instrumented)
    queried = _query(stored, health)
    expected_findings = {
        "trace-unauthorized-001": "failed",
        "trace-raw-content-001": "passed",
        "trace-missing-span-001": "not_evaluated",
    }
    caught = {
        trace_id: queried["trace_results"][trace_id]["status"]
        for trace_id, expected_status in expected_findings.items()
        if queried["trace_results"][trace_id]["status"] == expected_status
    }
    raw_record = next(record for record in stored if record["trace_id"] == "trace-raw-content-001")
    privacy_control_passed = raw_record["payload"]["raw_content"] == "[REDACTED]"
    pipeline_control_passed = queried["telemetry_health"]["pipeline_status"] == "unavailable"
    return {
        "pipeline_revision": PIPELINE_REVISION,
        "monitor_revision": MONITOR_REVISION,
        "vertical_slice_status": (
            "passed"
            if len(caught) == len(expected_findings) and privacy_control_passed and pipeline_control_passed
            else "failed"
        ),
        "stages": {
            "instrumented_records": len(instrumented),
            "collected_records": len(stored),
            "backend_records": len(stored),
            "dashboard_queries": 1,
            "alerts": len(queried["alerts"]),
        },
        "telemetry_health": queried["telemetry_health"],
        "trace_results": queried["trace_results"],
        "alerts": queried["alerts"],
        "negative_controls": {
            "expected_findings": expected_findings,
            "caught_findings": caught,
            "privacy_redaction_passed": privacy_control_passed,
            "telemetry_loss_visible": pipeline_control_passed,
        },
        "trace_to_case": [
            {
                "trace_id": trace_id,
                "case_id": f"regression-{trace_id}",
                "reason_codes": result["reason_codes"],
                "decision": "add_to_regression_set",
            }
            for trace_id, result in queried["trace_results"].items()
            if result["status"] != "passed"
        ],
        "candidate_release_decision": "block",
        "evidence_template": {
            "trace_ids": sorted(queried["trace_results"]),
            "pipeline_revision": PIPELINE_REVISION,
            "monitor_revision": MONITOR_REVISION,
            "telemetry_loss_action": "unavailable_not_green",
            "alert_owner": "synthetic-on-call",
            "regression_case_owner": "synthetic-evaluator",
        },
        "limitations": [
            "The backend is a local in-memory teaching store.",
            "No network, collector process, dashboard service, or provider API is used.",
            "Pipeline health logic is synthetic and not a capacity or availability claim.",
        ],
    }


def main() -> int:
    args = _parse_args()
    report = run_lab()
    if args.show_stages:
        print(json.dumps({"instrumented_records": len(_instrument(_events())), "message": "The report below contains every stage's summary."}, indent=2))
    rendered = json.dumps(report, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(rendered + "\n")
        print(f"Wrote {args.output}")
    else:
        print(rendered)
    return 0 if report["vertical_slice_status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
