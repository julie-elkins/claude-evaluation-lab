"""Contract tests for the course's deliberately degraded evaluation paths."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path
from types import ModuleType


ROOT = Path(__file__).resolve().parents[1]


def load_lab_module(relative_path: str, module_name: str) -> ModuleType:
    path = ROOT / relative_path
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise AssertionError(f"Could not load lab module from {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


class LabContractTests(unittest.TestCase):
    def test_incomplete_judge_output_becomes_visible_not_evaluated_state(self) -> None:
        lab = load_lab_module(
            "labs/03-automated-evaluators/run_lab.py",
            "lab_03_automated_evaluators",
        )

        result = lab._parse_judge_output('{"decision": "pass"}')

        self.assertEqual(result["status"], "not_evaluated")
        self.assertFalse(result["valid"])
        self.assertEqual(result["reason_code"], "schema_incomplete")
        self.assertEqual(
            result["missing_fields"],
            ["evidence_ids", "judge_revision", "reason_code"],
        )

    def test_invalid_judge_field_types_become_visible_not_evaluated_state(self) -> None:
        lab = load_lab_module(
            "labs/03-automated-evaluators/run_lab.py",
            "lab_03_automated_evaluators_types",
        )

        result = lab._parse_judge_output(
            '{"decision": "pass", "reason_code": 7, '
            '"judge_revision": "v1", "evidence_ids": ["response-text"]}'
        )

        self.assertEqual(result["status"], "not_evaluated")
        self.assertFalse(result["valid"])
        self.assertEqual(result["reason_code"], "schema_invalid")

    def test_agent_lab_catches_authorization_and_path_failures(self) -> None:
        lab = load_lab_module(
            "labs/04-agent-behavior/run_lab.py",
            "lab_04_agent_behavior",
        )

        report = lab.run_lab()
        failures = set(report["negative_controls"]["expected_failures"])

        self.assertIn("tool-unauthorized-001", failures)
        self.assertIn("trajectory-unauthorized-tool-001", failures)
        self.assertIn(
            "trajectory-unauthorized-tool-001",
            report["evidence_template"]["tool_findings"],
        )
        self.assertEqual(
            report["case_results"]["factuality-supported-001"]["evidence_ids"],
            {
                "claim-001": ["evidence-001"],
                "claim-002": ["evidence-002"],
            },
        )

    def test_observability_lab_catches_operational_and_privacy_failures(self) -> None:
        lab = load_lab_module(
            "labs/06-production-observability/run_lab.py",
            "lab_06_production_observability",
        )

        report = lab.run_lab()

        self.assertEqual(report["observability_suite_status"], "passed")
        self.assertEqual(report["candidate_release_decision"], "block")
        self.assertIn(
            "trace-missing-terminal-001",
            report["negative_controls"]["caught_failures"],
        )
        self.assertIn(
            "trace-raw-content-001",
            report["negative_controls"]["caught_failures"],
        )
        self.assertEqual(
            report["case_results"]["trace-healthy-001"]["status"],
            "pass",
        )
        self.assertEqual(
            report["case_results"]["trace-missing-terminal-001"]["status"],
            "not_evaluated",
        )

    def test_security_lab_catches_authority_and_evidence_failures(self) -> None:
        lab = load_lab_module(
            "labs/07-security-controls/run_lab.py",
            "lab_07_security_controls",
        )

        report = lab.run_lab()

        self.assertEqual(report["security_suite_status"], "passed")
        self.assertEqual(report["candidate_release_decision"], "block")
        self.assertEqual(
            report["case_results"]["security-healthy-001"]["status"],
            "passed",
        )
        self.assertEqual(
            report["case_results"]["security-missing-approval-001"]["status"],
            "refused",
        )
        self.assertEqual(
            report["case_results"]["security-deletion-evidence-missing-001"]["status"],
            "not_evaluated",
        )
        self.assertEqual(
            report["case_results"]["security-cross-tenant-read-001"]["status"],
            "failed",
        )

    def test_telemetry_vertical_slice_makes_pipeline_loss_visible(self) -> None:
        lab = load_lab_module(
            "labs/08-telemetry-vertical-slice/run_lab.py",
            "lab_08_telemetry_vertical_slice",
        )

        report = lab.run_lab()

        self.assertEqual(report["vertical_slice_status"], "passed")
        self.assertEqual(report["candidate_release_decision"], "block")
        self.assertTrue(report["negative_controls"]["privacy_redaction_passed"])
        self.assertTrue(report["negative_controls"]["telemetry_loss_visible"])
        self.assertEqual(
            report["telemetry_health"]["pipeline_status"],
            "unavailable",
        )
        self.assertEqual(
            report["trace_results"]["trace-missing-span-001"]["status"],
            "not_evaluated",
        )


if __name__ == "__main__":
    unittest.main()
