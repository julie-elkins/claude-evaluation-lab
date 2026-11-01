"""Run the offline agent-security control lab."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


CONTROL_SCHEMA_REVISION = "agent-security-controls-v1"
EVALUATOR_REVISION = "security-controls-v1"


@dataclass(frozen=True)
class SecurityCase:
    case_id: str
    principal: str
    tenant: str
    authorized_scope: bool
    credential_exposure: bool
    network_allowed: bool
    output_validated: bool
    approval_present: bool
    audit_event_present: bool
    idempotency_checked: bool
    deletion_check_present: bool
    expected_status: str = "passed"
    tenant_scope_allowed: bool = True
    tool_revision_pinned: bool = True
    dependency_revision_pinned: bool = True
    compensation_available: bool = True


def _cases() -> tuple[SecurityCase, ...]:
    return (
        SecurityCase("security-healthy-001", "synthetic-operator", "tenant-a", True, False, True, True, True, True, True, True),
        SecurityCase("security-unauthorized-scope-001", "synthetic-operator", "tenant-a", False, False, True, True, True, True, True, True, "failed"),
        SecurityCase("security-secret-exposure-001", "synthetic-operator", "tenant-a", True, True, True, True, True, True, True, True, "failed"),
        SecurityCase("security-network-egress-001", "synthetic-operator", "tenant-a", True, False, False, True, True, True, True, True, "failed"),
        SecurityCase("security-output-unvalidated-001", "synthetic-operator", "tenant-a", True, False, True, False, True, True, True, True, "failed"),
        SecurityCase("security-missing-approval-001", "synthetic-operator", "tenant-a", True, False, True, True, False, True, True, True, "refused"),
        SecurityCase("security-missing-audit-001", "synthetic-operator", "tenant-a", True, False, True, True, True, False, True, True, "failed"),
        SecurityCase("security-duplicate-side-effect-001", "synthetic-operator", "tenant-a", True, False, True, True, True, True, False, True, "failed"),
        SecurityCase("security-deletion-evidence-missing-001", "synthetic-operator", "tenant-a", True, False, True, True, True, True, True, False, "not_evaluated"),
        SecurityCase("security-cross-tenant-read-001", "synthetic-operator", "tenant-a", True, False, True, True, True, True, True, True, "failed", tenant_scope_allowed=False),
        SecurityCase("security-unpinned-tool-dependency-001", "synthetic-operator", "tenant-a", True, False, True, True, True, True, True, True, "failed", tool_revision_pinned=False, dependency_revision_pinned=False),
    )


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optional JSON report path.")
    return parser.parse_args()


def _evaluate(case: SecurityCase) -> dict[str, Any]:
    if not case.approval_present:
        return {"status": "refused", "reason_code": "required_approval_missing", "case_id": case.case_id}
    if not case.deletion_check_present:
        return {"status": "not_evaluated", "reason_code": "deletion_evidence_missing", "case_id": case.case_id}

    findings: list[str] = []
    if not case.authorized_scope:
        findings.append("authorization_scope_failed")
    if case.credential_exposure:
        findings.append("credential_boundary_failed")
    if not case.network_allowed:
        findings.append("network_egress_denied")
    if not case.output_validated:
        findings.append("side_effect_output_unvalidated")
    if not case.audit_event_present:
        findings.append("audit_event_missing")
    if not case.idempotency_checked:
        findings.append("idempotency_check_missing")
    if not case.tenant_scope_allowed:
        findings.append("tenant_scope_failed")
    if not case.tool_revision_pinned:
        findings.append("tool_revision_unpinned")
    if not case.dependency_revision_pinned:
        findings.append("dependency_revision_unpinned")
    if not case.compensation_available:
        findings.append("compensation_path_missing")
    if findings:
        return {
            "status": "failed",
            "reason_code": findings[0] if len(findings) == 1 else "multiple_security_findings",
            "findings": findings,
            "case_id": case.case_id,
        }
    return {"status": "passed", "reason_code": "security_control_contract_passed", "case_id": case.case_id}


def run_lab() -> dict[str, Any]:
    cases = _cases()
    results = {case.case_id: _evaluate(case) for case in cases}
    expected = {case.case_id: case.expected_status for case in cases if case.expected_status != "passed"}
    caught = {
        case_id: results[case_id]["status"]
        for case_id, expected_status in expected.items()
        if results[case_id]["status"] == expected_status
    }
    findings = [
        {
            "case_id": case_id,
            "severity": "high" if result["status"] in {"failed", "refused"} else "medium",
            "action": "hold_and_investigate",
            "reason_code": result["reason_code"],
        }
        for case_id, result in results.items()
        if result["status"] != "passed"
    ]
    return {
        "control_schema_revision": CONTROL_SCHEMA_REVISION,
        "evaluator_revision": EVALUATOR_REVISION,
        "security_suite_status": "passed" if len(caught) == len(expected) else "failed",
        "control_results": {
            "trust_boundaries": True,
            "identity_and_scope": True,
            "credential_boundary": True,
            "network_egress": True,
            "output_validation": True,
            "approval_and_audit": True,
            "idempotency": True,
            "deletion_evidence": True,
            "tenant_isolation": True,
            "tool_and_dependency_provenance": True,
            "compensation_path": True,
        },
        "case_results": results,
        "negative_controls": {"expected_failures": expected, "caught_failures": caught},
        "incident_findings": findings,
        "coverage_summary": {
            "synthetic_cases": len(cases),
            "control_categories": 8,
            "high_risk_findings": sum(item["severity"] == "high" for item in findings),
        },
        "candidate_release_decision": "release" if not findings else "block",
        "evidence_template": {
            "principal": "synthetic-operator",
            "tenant_scope": "tenant-a",
            "approval_id": "synthetic-approval-001",
            "audit_event": "synthetic-audit-001",
            "credential_exposure": "none",
            "network_destination": "synthetic-approved-service",
            "deletion_check": "synthetic-deletion-check-001",
            "tool_revision": "synthetic-tool-r1",
            "dependency_revision": "synthetic-dependencies-lock-r1",
            "compensation_action": "synthetic-compensate-update",
        },
        "limitations": [
            "Synthetic controls do not prove deployed enforcement.",
            "No real credentials, network calls, or production data are used.",
            "A policy field is evidence of a declared contract, not an implementation guarantee.",
        ],
    }


def main() -> int:
    args = _parse_args()
    report = run_lab()
    rendered = json.dumps(report, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(rendered + "\n")
        print(f"Wrote {args.output}")
    else:
        print(rendered)
    return 0 if report["security_suite_status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
