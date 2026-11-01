#!/usr/bin/env python3
"""Build the learner-facing GUIDE.md from the lesson-script source files."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LESSON_DIR = ROOT / "course" / "lesson-scripts"
OUTPUT = ROOT / "GUIDE.md"

MODULES = [
    {
        "number": 1,
        "title": "Evaluation foundations",
        "start": 1,
        "end": 4,
        "outcome": "Identify a false pass and write the evidence needed for a defensible evaluation decision.",
        "diagram": r"""
```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#F7F1E8","primaryTextColor":"#16324F","lineColor":"#2F6B8A","fontFamily":"ui-sans-serif, system-ui, sans-serif"}}}%%
flowchart LR
    A["Declare the decision"] --> B["Run the case"]
    B --> C["Check transport"]
    C --> D["Check semantic outcome"]
    D --> E{"Evidence complete?"}
    E -->|yes| F["Continue or release"]
    E -->|no| G["Stop, fail, or escalate"]
    classDef navy fill:#F7F1E8,stroke:#16324F,color:#16324F,stroke-width:2px
    classDef blue fill:#DCECF3,stroke:#2F6B8A,color:#16324F,stroke-width:2px
    classDef orange fill:#F5D8C4,stroke:#D97941,color:#16324F,stroke-width:2px
    classDef sage fill:#DCE8D8,stroke:#6F8F72,color:#16324F,stroke-width:2px
    classDef red fill:#F3D6D2,stroke:#B44B45,color:#16324F,stroke-width:2px
    class A navy
    class B,C blue
    class D,E orange
    class F sage
    class G red
```
""",
        "practice": [
            "What decision does your evaluation support, and what decision is outside its scope?",
            "Which field would distinguish transport success from semantic success?",
            "What should happen when a required evidence item is missing?",
        ],
    },
    {
        "number": 2,
        "title": "Evaluation cases and human review",
        "start": 5,
        "end": 9,
        "outcome": "Create a small, risk-based case set with a rubric, calibration plan, and disagreement review.",
        "diagram": r"""
```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#F7F1E8","primaryTextColor":"#16324F","lineColor":"#2F6B8A","fontFamily":"ui-sans-serif, system-ui, sans-serif"}}}%%
flowchart TB
    A["Representative cases"] --> B["Golden and calibration set"]
    B --> C["Rubric"]
    C --> D["Independent ratings"]
    D --> E["Disagreement review"]
    E --> F["Held-out decision set"]
    classDef blue fill:#DCECF3,stroke:#2F6B8A,color:#16324F,stroke-width:2px
    classDef orange fill:#F5D8C4,stroke:#D97941,color:#16324F,stroke-width:2px
    classDef sage fill:#DCE8D8,stroke:#6F8F72,color:#16324F,stroke-width:2px
    class A blue
    class B,C,D,E orange
    class F sage
```
""",
        "practice": [
            "Which cases represent normal, boundary, missing-information, conflicting, and recovery paths?",
            "Which cases may tune the rubric, and which must remain held out?",
            "What disagreement would cause recalibration rather than a simple average?",
        ],
    },
    {
        "number": 3,
        "title": "Automated evaluation",
        "start": 10,
        "end": 18,
        "outcome": "Combine deterministic checks, semantic judges, human calibration, and independent negative controls.",
        "diagram": r"""
```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#F7F1E8","primaryTextColor":"#16324F","lineColor":"#2F6B8A","fontFamily":"ui-sans-serif, system-ui, sans-serif"}}}%%
flowchart TB
    A["Observed output"] --> B["Contract checks"]
    A --> C["Semantic evaluator"]
    A --> D["Human review"]
    A --> E["Independent breaker"]
    B --> F["Layered findings"]
    C --> F
    D --> F
    E --> F
    F --> G["Decision rule"]
    classDef blue fill:#DCECF3,stroke:#2F6B8A,color:#16324F,stroke-width:2px
    classDef orange fill:#F5D8C4,stroke:#D97941,color:#16324F,stroke-width:2px
    classDef red fill:#F3D6D2,stroke:#B44B45,color:#16324F,stroke-width:2px
    classDef sage fill:#DCE8D8,stroke:#6F8F72,color:#16324F,stroke-width:2px
    class A blue
    class B,C,D orange
    class E red
    class F,G sage
```
""",
        "practice": [
            "Which criteria are deterministic, and which require semantic or human judgment?",
            "What bias probe would challenge your judge?",
            "What planted failure should your negative control catch?",
        ],
    },
    {
        "number": 4,
        "title": "Factuality, safety, and agents",
        "start": 19,
        "end": 25,
        "outcome": "Evaluate claims, safety boundaries, tool behavior, state changes, and recovery across an agent trajectory.",
        "diagram": r"""
```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#F7F1E8","primaryTextColor":"#16324F","lineColor":"#2F6B8A","fontFamily":"ui-sans-serif, system-ui, sans-serif"}}}%%
flowchart LR
    A["Observe"] --> B["Plan"]
    B --> C["Route to tool"]
    C --> D["Validate arguments"]
    D --> E["Observe result and state"]
    E --> F{"Recovered safely?"}
    F -->|yes| G["Complete or escalate"]
    F -->|no| H["Fail or block"]
    classDef blue fill:#DCECF3,stroke:#2F6B8A,color:#16324F,stroke-width:2px
    classDef orange fill:#F5D8C4,stroke:#D97941,color:#16324F,stroke-width:2px
    classDef sage fill:#DCE8D8,stroke:#6F8F72,color:#16324F,stroke-width:2px
    classDef red fill:#F3D6D2,stroke:#B44B45,color:#16324F,stroke-width:2px
    class A,B blue
    class C,D,E orange
    class F,G sage
    class H red
```
""",
        "practice": [
            "Which claims in the response need separate evidence checks?",
            "What makes a refusal safe and still useful?",
            "What trajectory evidence proves that a tool action was authorized and completed?",
        ],
    },
    {
        "number": 5,
        "title": "Benchmarks, release, and capstone",
        "start": 26,
        "end": 30,
        "outcome": "Compare a baseline and variant, state uncertainty and limitations, and produce an accountable release recommendation.",
        "diagram": r"""
```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#F7F1E8","primaryTextColor":"#16324F","lineColor":"#2F6B8A","fontFamily":"ui-sans-serif, system-ui, sans-serif"}}}%%
flowchart LR
    A["Baseline and variant"] --> B["Matched cases and slices"]
    B --> C["Findings and uncertainty"]
    C --> D{"Release decision"}
    D -->|revise| E["Change and re-evaluate"]
    D -->|release| F["Monitor"]
    D -->|block| G["Hold or rollback"]
    F --> H{"New evidence?"}
    H -->|yes| E
    H -->|no| F
    classDef blue fill:#DCECF3,stroke:#2F6B8A,color:#16324F,stroke-width:2px
    classDef orange fill:#F5D8C4,stroke:#D97941,color:#16324F,stroke-width:2px
    classDef sage fill:#DCE8D8,stroke:#6F8F72,color:#16324F,stroke-width:2px
    classDef red fill:#F3D6D2,stroke:#B44B45,color:#16324F,stroke-width:2px
    class A,B blue
    class C,D orange
    class E,F sage
    class G red
    class H orange
```
""",
        "practice": [
            "What stayed constant between the baseline and variant?",
            "Which high-risk slice could overturn an aggregate improvement?",
            "What owner, monitoring signal, and rollback trigger belong in the final report?",
        ],
    },
    {
        "number": 6,
        "title": "Production observability foundations",
        "start": 31,
        "end": 32,
        "outcome": "Distinguish observability from evaluation and define the trace evidence an agent workflow needs.",
        "diagram": r"""
```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#F7F1E8","primaryTextColor":"#16324F","lineColor":"#2F6B8A","fontFamily":"ui-sans-serif, system-ui, sans-serif"}}}%%
flowchart LR
    A["Agent run"] --> B["Telemetry"]
    B --> C["Trace and events"]
    C --> D["Debug or investigate"]
    C --> E["Evaluation case"]
    E --> F["Decision"]
    classDef blue fill:#DCECF3,stroke:#2F6B8A,color:#16324F,stroke-width:2px
    classDef orange fill:#F5D8C4,stroke:#D97941,color:#16324F,stroke-width:2px
    classDef sage fill:#DCE8D8,stroke:#6F8F72,color:#16324F,stroke-width:2px
    class A,B blue
    class C orange
    class D,E sage
    class F orange
```
""",
        "practice": [
            "Which production question requires a trace, and which requires an evaluation?",
            "What fields are required to reconstruct the agent path?",
            "What would make a trace incomplete rather than merely unsuccessful?",
        ],
    },
    {
        "number": 7,
        "title": "Instrumentation and operational signals",
        "start": 33,
        "end": 34,
        "outcome": "Map agent behavior to provider-neutral spans, metrics, budgets, and service-level objectives.",
        "diagram": r"""
```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#F7F1E8","primaryTextColor":"#16324F","lineColor":"#2F6B8A","fontFamily":"ui-sans-serif, system-ui, sans-serif"}}}%%
flowchart TB
    A["Workflow span"] --> B["Model span"]
    A --> C["Tool span"]
    A --> D["State and terminal event"]
    B --> E["Tokens and latency"]
    C --> F["Authorization and result"]
    D --> G["Outcome and evidence"]
    E --> H["Budget and SLO"]
    F --> H
    G --> H
    classDef blue fill:#DCECF3,stroke:#2F6B8A,color:#16324F,stroke-width:2px
    classDef orange fill:#F5D8C4,stroke:#D97941,color:#16324F,stroke-width:2px
    classDef sage fill:#DCE8D8,stroke:#6F8F72,color:#16324F,stroke-width:2px
    class A,B,C,D blue
    class E,F,G orange
    class H sage
```
""",
        "practice": [
            "Which signal shows the agent was slow, and which shows that it was wrong?",
            "What budget or service-level objective would block release?",
            "Which provider-specific field should be mapped to a provider-neutral field?",
        ],
    },
    {
        "number": 8,
        "title": "Privacy, monitoring, and incident response",
        "start": 35,
        "end": 36,
        "outcome": "Design redaction, retention, alerting, ownership, and rollback boundaries for agent evidence.",
        "diagram": r"""
```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#F7F1E8","primaryTextColor":"#16324F","lineColor":"#2F6B8A","fontFamily":"ui-sans-serif, system-ui, sans-serif"}}}%%
flowchart LR
    A["Raw event"] --> B["Redact and classify"]
    B --> C["Retain minimum evidence"]
    C --> D["Detect threshold"]
    D --> E["Owner investigates"]
    E --> F{"Containment needed?"}
    F -->|yes| G["Rollback or disable"]
    F -->|no| H["Document and monitor"]
    classDef blue fill:#DCECF3,stroke:#2F6B8A,color:#16324F,stroke-width:2px
    classDef orange fill:#F5D8C4,stroke:#D97941,color:#16324F,stroke-width:2px
    classDef red fill:#F3D6D2,stroke:#B44B45,color:#16324F,stroke-width:2px
    classDef sage fill:#DCE8D8,stroke:#6F8F72,color:#16324F,stroke-width:2px
    class A,B,C blue
    class D,E,F orange
    class G red
    class H sage
```
""",
        "practice": [
            "Which event fields are safe to retain, and which require redaction?",
            "What threshold turns a signal into an incident?",
            "Who owns containment, communication, and the follow-up regression case?",
        ],
    },
    {
        "number": 9,
        "title": "Continuous evaluation and production capstone",
        "start": 37,
        "end": 39,
        "outcome": "Turn production-style traces into regression cases and make a bounded release, hold, revise, or rollback decision.",
        "diagram": r"""
```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#F7F1E8","primaryTextColor":"#16324F","lineColor":"#2F6B8A","fontFamily":"ui-sans-serif, system-ui, sans-serif"}}}%%
flowchart LR
    A["Trace sample"] --> B["Review and classify"]
    B --> C["Evaluation case"]
    C --> D["Regression run"]
    D --> E["Compare revision"]
    E --> F{"Decision"}
    F -->|release| G["Monitor"]
    F -->|hold or revise| H["Change and rerun"]
    F -->|rollback| I["Contain"]
    G --> B
    H --> C
    classDef blue fill:#DCECF3,stroke:#2F6B8A,color:#16324F,stroke-width:2px
    classDef orange fill:#F5D8C4,stroke:#D97941,color:#16324F,stroke-width:2px
    classDef sage fill:#DCE8D8,stroke:#6F8F72,color:#16324F,stroke-width:2px
    classDef red fill:#F3D6D2,stroke:#B44B45,color:#16324F,stroke-width:2px
    class A,B,C blue
    class D,E,F orange
    class G,H sage
    class I red
```
""",
        "practice": [
            "What trace finding is important enough to become a regression case?",
            "Which evidence would justify release, and which would require rollback?",
            "What does the production capstone still not prove?",
        ],
    },
    {
        "number": 10,
        "title": "Security and assurance controls",
        "start": 40,
        "end": 44,
        "outcome": "Threat-model an agent, enforce authority and data boundaries, protect telemetry, and test monitoring resilience.",
        "diagram": r"""
```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#F7F1E8","primaryTextColor":"#16324F","lineColor":"#2F6B8A","fontFamily":"ui-sans-serif, system-ui, sans-serif"}}}%%
flowchart LR
    A["Assets and actors"] --> B["Trust boundaries"]
    B --> C["Identity and least privilege"]
    C --> D["Validated side effect"]
    B --> E["Telemetry privacy"]
    E --> F["Audit and response"]
    D --> G["Monitor the monitor"]
    F --> G
    classDef blue fill:#DCECF3,stroke:#2F6B8A,color:#16324F,stroke-width:2px
    classDef orange fill:#F5D8C4,stroke:#D97941,color:#16324F,stroke-width:2px
    classDef red fill:#F3D6D2,stroke:#B44B45,color:#16324F,stroke-width:2px
    classDef sage fill:#DCE8D8,stroke:#6F8F72,color:#16324F,stroke-width:2px
    class A,B blue
    class C,D,E orange
    class F red
    class G sage
```
""",
        "practice": [
            "What asset, actor, trust boundary, and consequence belong in your threat model?",
            "Which authority, data, network, or side-effect control is release-blocking?",
            "What telemetry failure would make the result unavailable rather than green?",
        ],
    },
    {
        "number": 11,
        "title": "Continuous assurance and production implementation",
        "start": 45,
        "end": 48,
        "outcome": "Run a local telemetry path, detect drift and side-effect risk, and produce a security-aware assurance decision.",
        "diagram": r"""
```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#F7F1E8","primaryTextColor":"#16324F","lineColor":"#2F6B8A","fontFamily":"ui-sans-serif, system-ui, sans-serif"}}}%%
flowchart LR
    A["Instrument"] --> B["Collect and redact"]
    B --> C["Store and query"]
    C --> D["Alert and investigate"]
    D --> E["Evaluate and recalibrate"]
    E --> F["Approve, hold, or rollback"]
    F --> A
    classDef blue fill:#DCECF3,stroke:#2F6B8A,color:#16324F,stroke-width:2px
    classDef orange fill:#F5D8C4,stroke:#D97941,color:#16324F,stroke-width:2px
    classDef sage fill:#DCE8D8,stroke:#6F8F72,color:#16324F,stroke-width:2px
    classDef red fill:#F3D6D2,stroke:#B44B45,color:#16324F,stroke-width:2px
    class A,B blue
    class C,D orange
    class E,F sage
```
""",
        "practice": [
            "Where can evidence be lost between instrumentation and action?",
            "What drift or side-effect signal would trigger recalibration or a hold?",
            "Which claim does your final assurance report still not prove?",
        ],
    },
]


def section(text: str, heading: str) -> str:
    pattern = rf"^## {re.escape(heading)}\s*$\n(.*?)(?=^## |\Z)"
    match = re.search(pattern, text, flags=re.MULTILINE | re.DOTALL)
    if not match:
        raise ValueError(f"Missing section {heading!r}")
    return match.group(1).strip()


def lesson_number(path: Path) -> int:
    match = re.match(r"lesson-(\d+)-", path.name)
    if not match:
        raise ValueError(f"Unexpected lesson filename: {path.name}")
    return int(match.group(1))


def lesson_title(text: str) -> str:
    first_line = text.splitlines()[0]
    return re.sub(r"^# Lesson \d+:\s*", "", first_line).strip()


def lesson_metadata(text: str, label: str) -> str:
    pattern = rf"^(?:\*\*)?{re.escape(label)}(?::\*\*|\:)\s*(.+)$"
    match = re.search(pattern, text, flags=re.MULTILINE)
    return match.group(1).strip() if match else ""


def shift_headings(text: str, level: int = 1) -> str:
    prefix = "#" * level
    return re.sub(r"^(#{1,6})\s+", lambda match: prefix + match.group(1) + " ", text, flags=re.MULTILINE)


def render_lesson(path: Path) -> str:
    text = path.read_text()
    number = lesson_number(path)
    title = lesson_title(text)
    objective = section(text, "Learner objective")
    script = section(text, "Speaker script")
    practice = section(text, "Learner practice")
    limitation = section(text, "What this lesson does not prove")
    lab = lesson_metadata(text, "Lab") or lesson_metadata(text, "Primary lab")
    runtime = lesson_metadata(text, "Estimated runtime") or lesson_metadata(text, "Suggested runtime")

    lines = [
        f"### Lesson {number}: {title}",
        "",
        f"*{runtime}*",
        "",
        f"**Lab connection:** {lab}",
        "",
        "#### Learner objective",
        "",
        objective,
        "",
        "#### Core lesson",
        "",
        script,
        "",
        "#### Learner practice 🧪",
        "",
        practice,
        "",
        "#### What this lesson does not prove ⚠️",
        "",
        limitation,
        "",
    ]
    return "\n".join(lines)


def render_fundamentals() -> str:
    text = (ROOT / "FUNDAMENTALS.md").read_text().strip()
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    return shift_headings("\n".join(lines).strip(), level=2)


def render_lab(path: Path) -> str:
    text = path.read_text().strip()
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        lines[0] = "### " + lines[0][2:]
    for index, line in enumerate(lines):
        if line.startswith("## "):
            lines[index] = "#### " + line[3:]
    return "\n".join(lines)


def render_module(module: dict[str, object], lessons: list[Path]) -> str:
    title = str(module["title"])
    outcome = str(module["outcome"])
    practice = list(module["practice"])  # type: ignore[arg-type]
    parts = [
        f"## Module {module['number']} — {title}",
        "",
        f"**Hands-on outcome:** {outcome}",
        "",
        str(module["diagram"]).strip(),
        "",
    ]
    parts.extend(render_lesson(path) for path in lessons)
    parts.extend(
        [
            "### Module practice check 📝",
            "",
            "> [!TIP]",
            "> Answer these before moving to the next module:",
            ">",
        ]
    )
    parts.extend(
        f"> {index}. {question}" for index, question in enumerate(practice, start=1)
    )
    parts.append("")
    return "\n".join(parts)


def build() -> str:
    lesson_paths = sorted(LESSON_DIR.glob("lesson-*.md"), key=lesson_number)
    expected = list(range(1, 49))
    actual = [lesson_number(path) for path in lesson_paths]
    if actual != expected:
        raise ValueError(f"Expected lessons {expected}, found {actual}")

    parts = [
        "# LLM & Agent Evaluation Lab — From Offline Evidence to Production-Oriented Assurance",
        "",
        "<!-- GENERATED FILE. Edit course/lesson-scripts or FUNDAMENTALS.md, then run `uv run python scripts/build_guide.py`. -->",
        "",
        "This is the complete learner-facing course in one reading path. The lesson scripts remain the editable recording source; this guide omits speaker notes and recording-only instructions so learners do not need to jump between folders.",
        "",
        "## Start here",
        "",
        "This course is a build-along path for learning how to evaluate and observe LLM applications and agents, using Claude as a running provider example. You will connect a declared decision to representative cases, evidence, evaluator layers, telemetry, security controls, monitoring, and a bounded release action.",
        "",
        "If you are new to evaluation work, start with the [fundamentals](FUNDAMENTALS.md) below. If you want the shortest working path, read Module 1 and run [Lab 1](labs/01-semantic-outcomes/README.md) before continuing.",
        "",
        "### Companion repositories",
        "",
        "- [Claude Architect Lab](https://github.com/julie-elkins/claude-architect-lab) — prerequisite patterns for agent loops, tools, configuration, prompting, context, and reliability.",
        "- [Agent Assurance Harness](https://github.com/julie-elkins/agent-assurance-harness) — the public offline harness used by this course to demonstrate evidence contracts, evaluator controls, and release-boundary checks.",
        "",
        "### Learning path",
        "",
        "```mermaid",
        "%%{init: {\"theme\":\"base\",\"themeVariables\":{\"background\":\"#F7F1E8\",\"primaryTextColor\":\"#16324F\",\"lineColor\":\"#2F6B8A\",\"fontFamily\":\"ui-sans-serif, system-ui, sans-serif\"}}}%%",
        "flowchart LR",
        "    A[\"Declare the decision\"] --> B[\"Design the cases\"]",
        "    B --> C[\"Choose evaluator layers\"]",
        "    C --> D[\"Inspect agent behavior\"]",
        "    D --> E[\"Release, revise, or hold\"]",
        "    classDef cream fill:#F7F1E8,stroke:#16324F,color:#16324F,stroke-width:2px",
        "    classDef blue fill:#DCECF3,stroke:#2F6B8A,color:#16324F,stroke-width:2px",
        "    classDef orange fill:#F5D8C4,stroke:#D97941,color:#16324F,stroke-width:2px",
        "    classDef sage fill:#DCE8D8,stroke:#6F8F72,color:#16324F,stroke-width:2px",
        "    class A cream",
        "    class B,C blue",
        "    class D orange",
        "    class E sage",
        "```",
        "",
        "## Quick start",
        "",
        "```bash",
        "uv run python labs/01-semantic-outcomes/run_lab.py",
        "```",
        "",
        "The required labs are offline and synthetic. They require no Claude API key and demonstrate the path from transport status to a bounded release decision, then from an agent trace to security controls, telemetry health, an incident, and a regression case.",
        "",
        "## Continue learning",
        "",
        "- [Julie’s YouTube channel](https://www.youtube.com/@JulieElkins) — optional video walkthroughs.",
        "- [Julie’s public site](https://julie-elkins.github.io) — projects, learning paths, and design principles.",
        "- [Agent Systems Design Guide](https://github.com/julie-elkins/agent-systems-design-guide) — shared design reasoning and report vocabulary.",
        "- [Apple Platform Agent Quality Lab](https://github.com/julie-elkins/apple-platform-agent-quality-lab) — native macOS implementation of the evaluation boundary.",
        "- [OpenTelemetry GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/) — provider-neutral trace and metric vocabulary; verify the current convention status before recording.",
        "- [Phoenix](https://github.com/Arize-ai/phoenix) — optional local observability backend for trace inspection.",
        "- [Langfuse](https://github.com/langfuse/langfuse) — optional comparison point for trace, evaluation, dataset, and experiment workflows.",
        "",
        "### Runnable labs 🔬",
        "",
        "- [Lab 1: Transport success is not task success](labs/01-semantic-outcomes/README.md)",
        "- [Lab 2: Build a case set before you trust the score](labs/02-case-design/README.md)",
        "- [Lab 3: Layer the evaluator before you trust the judge](labs/03-automated-evaluators/README.md)",
        "- [Lab 4: Evaluate the path, not only the final answer](labs/04-agent-behavior/README.md)",
        "- [Lab 5: Turn evaluation evidence into a release decision](labs/05-release-capstone/README.md)",
        "- [Lab 6: Observe the agent before you trust the dashboard](labs/06-production-observability/README.md)",
        "- [Lab 7: Test the agent security boundary](labs/07-security-controls/README.md)",
        "- [Lab 8: Build the local telemetry vertical slice](labs/08-telemetry-vertical-slice/README.md)",
        "",
        "### Optional live-Claude extension",
        "",
        "The required path stays offline and deterministic. If you want to attach one live Claude observation, use the [optional bounded live-Claude adapter guide](labs/optional-live-claude-adapter/README.md) only after declaring request, time, token, spend, model, revision, and privacy limits.",
        "",
        "## Fundamentals 📘",
        "",
        render_fundamentals(),
        "",
        "## Course map",
        "",
        "| Module | Lessons | Learner outcome |",
        "|---|---:|---|",
    ]

    for module in MODULES:
        parts.append(f"| {module['number']}. {module['title']} | {module['start']}–{module['end']} | {module['outcome']} |")

    parts.extend(
        [
            "",
            "The course uses the cream visual system documented in [course/VISUAL-SYSTEM.md](course/VISUAL-SYSTEM.md). The [glossary](GLOSSARY.md) is a quick reference for evaluation terms.",
            "",
        ]
    )

    for module in MODULES:
        paths = [path for path in lesson_paths if int(module["start"]) <= lesson_number(path) <= int(module["end"])]
        parts.append(render_module(module, paths))

        if module["number"] == 1:
            parts.extend(
                [
                    "## Lab 1: Transport success is not task success 🔬",
                    "",
                    "The first runnable lab is included here so you can complete the course's initial hands-on path without leaving the guide.",
                    "",
                    render_lab(ROOT / "labs" / "01-semantic-outcomes" / "README.md"),
                    "",
                ]
            )
        elif module["number"] == 2:
            parts.extend(
                [
                    "## Lab 2: Build a case set before you trust the score 🔬",
                    "",
                    "This lab is included here so you can practice representative cases, calibration, held-out measurement, and negative controls without leaving the guide.",
                    "",
                    render_lab(ROOT / "labs" / "02-case-design" / "README.md"),
                    "",
                ]
            )
        elif module["number"] == 3:
            parts.extend(
                [
                    "## Lab 3: Layer the evaluator before you trust the judge 🔬",
                    "",
                    "This lab is included here so you can inspect deterministic checks, structured judge output, independent semantic evidence, and pairwise bias without leaving the guide.",
                    "",
                    render_lab(ROOT / "labs" / "03-automated-evaluators" / "README.md"),
                    "",
                ]
            )
            parts.extend(
                [
                    "#### Related implementation",
                    "",
                    "The automated evaluator patterns in this module are implemented and demonstrated in the [Agent Assurance Harness](https://github.com/julie-elkins/agent-assurance-harness). Use the course lesson for the decision logic, then open the harness when you want to inspect the reusable control.",
                    "",
                ]
            )
        elif module["number"] == 4:
            parts.extend(
                [
                    "## Lab 4: Evaluate the path, not only the final answer 🔬",
                    "",
                    "This lab is included here so you can inspect claim support, safety boundaries, tool behavior, state changes, and recovery without leaving the guide.",
                    "",
                    render_lab(ROOT / "labs" / "04-agent-behavior" / "README.md"),
                    "",
                ]
            )
            parts.extend(
                [
                    "#### Related implementation",
                    "",
                    "The factuality, content-assurance, and trajectory patterns in this module build on the public [Agent Assurance Harness](https://github.com/julie-elkins/agent-assurance-harness).",
                    "",
                ]
            )
        elif module["number"] == 5:
            parts.extend(
                [
                    "## Lab 5: Turn evaluation evidence into a release decision 🔬",
                    "",
                    "This capstone lab is included here so you can compare a baseline and variant, inspect uncertainty and high-risk slices, rehearse rollback, and complete a release report without leaving the guide.",
                    "",
                    render_lab(ROOT / "labs" / "05-release-capstone" / "README.md"),
                    "",
                ]
            )
        elif module["number"] == 6:
            parts.extend(
                [
                    "## Lab 6: Observe the agent before you trust the dashboard 🔬",
                    "",
                    "This lab is included here so you can inspect a provider-neutral trace contract, operational signals, privacy boundaries, incident findings, and the trace-to-test-case loop without requiring a live provider.",
                    "",
                    render_lab(ROOT / "labs" / "06-production-observability" / "README.md"),
                    "",
                ]
            )
        elif module["number"] == 10:
            parts.extend(
                [
                    "## Lab 7: Test the agent security boundary 🛡️",
                    "",
                    "This lab is included here so you can threat-model an agent, inspect authority and data boundaries, and test security evidence without using live credentials or production data.",
                    "",
                    render_lab(ROOT / "labs" / "07-security-controls" / "README.md"),
                    "",
                ]
            )
        elif module["number"] == 11:
            parts.extend(
                [
                    "## Lab 8: Build the local telemetry vertical slice 📡",
                    "",
                    "This lab is included here so you can follow evidence from instrumentation through collection, redaction, local storage, query, alerting, and regression-case creation.",
                    "",
                    render_lab(ROOT / "labs" / "08-telemetry-vertical-slice" / "README.md"),
                    "",
                ]
            )
            parts.extend(
                [
                    "#### Related implementation",
                    "",
                    "The release workflow builds on the public [Agent Assurance Harness](https://github.com/julie-elkins/agent-assurance-harness), including its benchmark reporting, change-impact, run-manifest, and rollback-rehearsal patterns. The earlier [Claude Architect Lab](https://github.com/julie-elkins/claude-architect-lab) remains useful for refreshing agent loops, tool boundaries, and context before evaluating release behavior.",
                    "",
                ]
            )

    parts.extend(
        [
            "## Repository map",
            "",
            "- `GUIDE.md` — this generated learner path.",
            "- `FUNDAMENTALS.md` — prerequisite concepts and readiness check.",
            "- `GLOSSARY.md` — concise definitions of recurring terms.",
            "- `course/lesson-scripts/` — editable lesson and recording source.",
            "- `labs/` — runnable learner labs.",
            "- `slides/` — PowerPoint source and recording assets.",
            "- `labs/06-production-observability/` — offline trace and incident observability lab.",
            "- `labs/07-security-controls/` — synthetic security boundary and assurance controls lab.",
            "- `labs/08-telemetry-vertical-slice/` — local instrumentation, collection, query, and monitor-health lab.",
            "- `course/VISUAL-SYSTEM.md` — colors and diagram conventions.",
            "- `scripts/build_guide.py` — reproducible guide builder.",
            "",
            "## What this course does not prove ⚠️",
            "",
            "The course uses public synthetic examples and an offline-first path. Its results do not establish live Claude quality, production safety, business impact, or learner adoption outside the declared scenario. The security, observability, and assurance tracks teach production-oriented control paths, not a guarantee that any deployed system is secure, compliant, observable, or operationally complete. A release decision remains bounded by its revision, case set, evidence, evaluator configuration, control coverage, telemetry completeness, and date.",
            "",
            "To rebuild this guide after editing the source files:",
            "",
            "```bash",
            "uv run python scripts/build_guide.py",
            "```",
            "",
        ]
    )
    return "\n".join(parts)


if __name__ == "__main__":
    OUTPUT.write_text(build())
    print(f"Wrote {OUTPUT}")
