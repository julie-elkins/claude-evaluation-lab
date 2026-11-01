#!/usr/bin/env python3
"""Validate that GUIDE.md matches the generated learner-facing source."""

from __future__ import annotations

import sys
from pathlib import Path

from build_guide import OUTPUT, build


def main() -> int:
    expected = build()
    if not OUTPUT.exists():
        print(f"Missing generated guide: {OUTPUT}", file=sys.stderr)
        return 1

    actual = OUTPUT.read_text()
    if actual != expected:
        print(
            "GUIDE.md is stale. Run: uv run python scripts/build_guide.py",
            file=sys.stderr,
        )
        return 1

    lesson_headings = actual.count("\n### Lesson ")
    if lesson_headings != 48:
        print(f"Expected 48 lesson headings, found {lesson_headings}", file=sys.stderr)
        return 1

    visual_sections = {
        "\n## Fundamentals 📘": 1,
        "\n### Runnable labs 🔬": 1,
        "\n#### Learner practice 🧪": 48,
        "\n#### What this lesson does not prove ⚠️": 48,
        "\n### Module practice check 📝": 11,
        "\n## Lab 1: Transport success is not task success 🔬": 1,
        "\n## Lab 2: Build a case set before you trust the score 🔬": 1,
        "\n## Lab 3: Layer the evaluator before you trust the judge 🔬": 1,
        "\n## Lab 4: Evaluate the path, not only the final answer 🔬": 1,
        "\n## Lab 5: Turn evaluation evidence into a release decision 🔬": 1,
        "\n## Lab 6: Observe the agent before you trust the dashboard 🔬": 1,
        "\n## Lab 7: Test the agent security boundary 🛡️": 1,
        "\n## Lab 8: Build the local telemetry vertical slice 📡": 1,
        "\n##### Terminal states 🚦": 1,
    }
    for marker, expected_count in visual_sections.items():
        actual_count = actual.count(marker)
        if actual_count != expected_count:
            print(
                f"Expected {expected_count} occurrence(s) of {marker.strip()!r}, "
                f"found {actual_count}",
                file=sys.stderr,
            )
            return 1

    for state in ("completed", "failed", "refused", "skipped", "not_evaluated"):
        if f"| `{state}` |" not in actual:
            print(f"Missing terminal-state table entry: {state}", file=sys.stderr)
            return 1

    required_links = [
        "FUNDAMENTALS.md",
        "GLOSSARY.md",
        "course/VISUAL-SYSTEM.md",
        "labs/01-semantic-outcomes/README.md",
        "labs/02-case-design/README.md",
        "labs/03-automated-evaluators/README.md",
        "labs/04-agent-behavior/README.md",
        "labs/05-release-capstone/README.md",
        "labs/06-production-observability/README.md",
        "labs/07-security-controls/README.md",
        "labs/08-telemetry-vertical-slice/README.md",
        "labs/optional-live-claude-adapter/README.md",
        "https://github.com/julie-elkins/claude-architect-lab",
        "https://github.com/julie-elkins/agent-assurance-harness",
        "https://github.com/julie-elkins/agent-systems-design-guide",
        "https://github.com/julie-elkins/agent-systems-design-guide/blob/main/REPORT_VOCABULARY.md",
        "https://github.com/julie-elkins/apple-platform-agent-quality-lab",
        "https://www.youtube.com/@JulieElkins",
        "https://julie-elkins.github.io",
        "https://opentelemetry.io/docs/specs/semconv/gen-ai/",
        "https://github.com/Arize-ai/phoenix",
        "https://github.com/langfuse/langfuse",
    ]
    missing = [link for link in required_links if link not in actual]
    if missing:
        print("Missing required guide links:", file=sys.stderr)
        for link in missing:
            print(f"  {link}", file=sys.stderr)
        return 1

    print("GUIDE.md is current and contains all 48 lessons.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
