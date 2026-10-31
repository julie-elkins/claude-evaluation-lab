"""Run the first Claude Evaluation Lab using the pinned assurance harness."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path


HARNESS_REVISION = "3d69db3cc45a86c832c53244f6c9fba55f4b16db"
HARNESS_LAB = Path("examples/agent-workflow-teaching-lab/run_lab.py")


def _default_harness_root() -> Path:
    return Path(__file__).resolve().parents[3] / "agent-assurance-harness"


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--harness-root",
        type=Path,
        default=None,
        help="Local checkout of the Agent Assurance Harness.",
    )
    return parser.parse_args()


def _revision(root: Path) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def main() -> int:
    args = _parse_args()
    root = (args.harness_root or _default_harness_root()).resolve()
    if not root.is_dir():
        raise SystemExit(
            f"Harness checkout not found at {root}. "
            "Clone agent-assurance-harness beside this repository or pass --harness-root."
        )

    actual_revision = _revision(root)
    if actual_revision != HARNESS_REVISION:
        raise SystemExit(
            "Harness revision mismatch: "
            f"expected {HARNESS_REVISION}, found {actual_revision}. "
            "Use the course-pinned revision before recording a learner result."
        )

    command = [
        "uv",
        "run",
        "--project",
        str(root),
        "python",
        str(root / HARNESS_LAB),
    ]
    child_environment = os.environ.copy()
    child_environment.pop("VIRTUAL_ENV", None)
    result = subprocess.run(
        command,
        check=False,
        text=True,
        capture_output=True,
        env=child_environment,
    )
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="")

    summary = {
        "course": "claude-evaluation-lab",
        "lab": "01-semantic-outcomes",
        "harness_revision": actual_revision,
        "offline": True,
        "metadata_only": True,
        "underlying_exit_code": result.returncode,
        "what_it_does_not_prove": [
            "live Claude quality",
            "production observability",
            "business impact",
        ],
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
