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
    if lesson_headings != 30:
        print(f"Expected 30 lesson headings, found {lesson_headings}", file=sys.stderr)
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
        "https://github.com/julie-elkins/claude-architect-lab",
        "https://github.com/julie-elkins/agent-assurance-harness",
        "https://github.com/julie-elkins/agent-systems-design-guide",
        "https://github.com/julie-elkins/apple-platform-agent-quality-lab",
        "https://www.youtube.com/@JulieElkins",
        "https://julie-elkins.github.io",
    ]
    missing = [link for link in required_links if link not in actual]
    if missing:
        print("Missing required guide links:", file=sys.stderr)
        for link in missing:
            print(f"  {link}", file=sys.stderr)
        return 1

    print("GUIDE.md is current and contains all 30 lessons.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
