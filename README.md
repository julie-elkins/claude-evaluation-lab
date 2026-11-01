# LLM & Agent Evaluation Lab

Hands-on lessons for building and interpreting LLM and agent evaluations, using
Claude as a running provider example, then connecting those evaluations to
production-oriented assurance.

This course uses the public
[Agent Assurance Harness](https://github.com/julie-elkins/agent-assurance-harness)
as its evaluation engine. The course repository is the learner-facing layer: it
explains the decisions, provides the lab path, and links each lesson to a
working example.

## What you will build

You will build an evaluation workflow that can distinguish:

- a request that returned successfully from a task that actually succeeded;
- an exact-rule check from a semantic check, which judges meaning rather than
  identical text;
- a model score from evidence that supports a release decision;
- a passing average from a blocking high-risk failure; and
- a benchmark result from evidence that your own use case works;
- a complete-looking trace from a trace that is complete enough to investigate;
- an operational signal from a quality or safety finding; and
- a production-style failure from a regression case that can be rerun.

## Start here

Read the [learner guide](GUIDE.md). It contains the fundamentals, all 48
learner-facing lessons, all eight runnable labs, diagrams, and module practice
checks in one reading path. You should not need to move between lesson folders
to follow the course.

The [Claude Architect Lab](https://github.com/julie-elkins/claude-architect-lab)
is the companion prerequisite course for agent loops, tools, configuration,
prompting, context, and reliability. The [Agent Assurance
Harness](https://github.com/julie-elkins/agent-assurance-harness) is the public
evaluation engine used by this course.

The [Agent Systems Design Guide](https://github.com/julie-elkins/agent-systems-design-guide)
defines the shared evaluation vocabulary. The
[Apple Platform Agent Quality Lab](https://github.com/julie-elkins/apple-platform-agent-quality-lab)
shows the same evidence boundary in a native macOS implementation.

For optional video walkthroughs and related projects, visit
[Julie’s YouTube channel](https://www.youtube.com/@JulieElkins) and
[Julie’s public site](https://julie-elkins.github.io).

## Prerequisites

- Python 3.11 or newer.
- [`uv`](https://docs.astral.sh/uv/) for running the course commands.
- Comfort reading JSON and using a terminal. Python experience is helpful but
  not required for the introductory labs.

The required labs are offline and synthetic, meaning they use bounded local
fixtures rather than live Claude requests. They do not require a Claude API key.

## Learning path

The course is organized as eleven modules and 48 lessons. The course map and
[source coverage matrix](course/SOURCE_COVERAGE_MATRIX.md) show how the
historical lecture concepts, current harness controls, and
production-assurance references map into the learner path.

1. Evaluation foundations
2. Human review and evaluation cases
3. Automated checks and LLM-as-a-judge
4. Factuality, safety, and agent evaluation
5. Regression, release decisions, and the capstone
6. Production observability foundations
7. Instrumentation and operational signals
8. Privacy, monitoring, and incident response
9. Continuous evaluation and the production capstone
10. Security and assurance controls
11. Continuous assurance and production implementation

## Course visual legend

The learner guide uses the cream visual system documented in
[course/VISUAL-SYSTEM.md](course/VISUAL-SYSTEM.md). These icons make the
purpose of each section visible while you move through the course:

- 📘 Fundamentals — prerequisite concepts and vocabulary.
- 🔬 Runnable lab — a hands-on experiment with synthetic evidence.
- 🧪 Learner practice — an action to complete after the lesson.
- 📝 Module practice check — questions to answer before moving on.
- ⚠️ Evidence limitation — what the result does not prove.
- 🛡️ Security control — authority, privacy, or side-effect boundary.
- 📡 Telemetry workflow — instrumentation, collection, monitoring, or alerting.

## Runnable labs

Run the labs in order. Each lab is self-contained, produces a fast local
result, includes a deliberately degraded case, and states what its evidence
does and does not prove.

1. [Semantic outcomes](labs/01-semantic-outcomes/README.md) — distinguish
   transport success from task success.
2. [Case design](labs/02-case-design/README.md) — build representative,
   calibrated, and held-out evaluation cases.
3. [Automated evaluators](labs/03-automated-evaluators/README.md) — layer
   deterministic checks, semantic checks, and judge-bias probes.
4. [Agent behavior](labs/04-agent-behavior/README.md) — evaluate factuality,
   safety, tool use, authorization, state, and recovery.
5. [Release capstone](labs/05-release-capstone/README.md) — compare revisions,
   inspect high-risk slices, and make a bounded release recommendation.
6. [Production observability](labs/06-production-observability/README.md) —
   inspect traces, operational signals, privacy boundaries, and incident
   evidence.
7. [Security controls](labs/07-security-controls/README.md) — test trust
   boundaries, least privilege, telemetry access, and side-effect controls.
8. [Telemetry vertical slice](labs/08-telemetry-vertical-slice/README.md) —
   follow local evidence from instrumentation through alerting and regression.

Optional:

- [Live-Claude adapter](labs/07-live-claude-adapter/README.md) — connect one
  live provider observation to the same evidence contract under explicit
  request, time, token, spend, and privacy limits.

## Quick start

Clone both repositories beside each other:

```bash
git clone https://github.com/julie-elkins/claude-evaluation-lab.git
git clone https://github.com/julie-elkins/agent-assurance-harness.git
cd claude-evaluation-lab
uv run python labs/01-semantic-outcomes/run_lab.py
```

The course wrapper uses the harness content tree from revision
`3d69db3cc45a86c832c53244f6c9fba55f4b16db`, which matches the current public
`origin/main` tree at `2f95f4c` as of the course audit. If you are working from
a local checkout, the wrapper verifies the pinned revision before running the
lab.

## What the first lab proves

The first lab shows a common evaluation failure: two workflows can both report
transport status `ok`, while only one produces usable task evidence. Transport
status describes the request boundary; semantic outcome describes whether the
declared task reached its goal.

The lab remains synthetic and metadata-only. It does not prove live Claude
quality, production monitoring, business impact, or safety outside the declared
scenario.

## Repository map

```text
GUIDE.md      generated learner guide for the full course
FUNDAMENTALS.md prerequisite concepts and readiness check
GLOSSARY.md   course vocabulary
course/       lesson source, map, and reusable templates
labs/         eight runnable learner labs plus an optional live adapter
slides/       slide outlines and recording guidance
scripts/      course validation and setup helpers
tests/        standard-library contract tests for the course labs
```

## Current status

Available now:

- the complete 48-lesson learner guide and recording scripts;
- eight offline, deterministic labs covering Modules 1–11;
- the source coverage matrix, fundamentals, glossary, and cream visual system;
- validation scripts for the generated guide; and
- a local CI contract that rebuilds the guide and runs every lab; and
- links to the companion design guide, Apple lab, harness, website, videos,
  OpenTelemetry, Phoenix, and Langfuse.

Reference courses and standards used for the advanced track:

- [Stanford Engineering AI Agents](https://cs329z.stanford.edu/) — agent
  evaluation and reliability framing.
- [Evaluating AI Agents](https://www.deeplearning.ai/courses/evaluating-ai-agents)
  — trace-to-evaluation and component-evaluation patterns.
- [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/bonus-unit2/what-is-agent-observability-and-evaluation)
  — the observability and evaluation distinction.
- [OWASP GenAI Security Project](https://genai.owasp.org/llm-top-10/) —
  security threat categories for generative AI systems.
- [NIST Generative AI Profile](https://www.nist.gov/itl/ai-risk-management-framework/ai-rmf-generative-ai-profile)
  — risk management and post-deployment assurance.

Planned or optional next steps:

- the full editable PowerPoint deck and lesson-by-lesson recording assets.

Synthetic lab results are learning evidence, not proof of live Claude quality,
production safety, or business impact.

The repository contains the learner guide, lesson scripts, lab implementations,
and recording guidance. The editable PowerPoint deck remains a separate
recording deliverable until it is added under `slides/`.
