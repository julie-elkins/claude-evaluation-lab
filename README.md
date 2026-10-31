# Claude Evaluation Lab

Hands-on lessons for building and interpreting LLM evaluations with Claude.

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
- a benchmark result from evidence that your own use case works.

## Start here

Read the [learner guide](GUIDE.md). It contains the fundamentals, all 30
learner-facing lessons, all five runnable labs, diagrams, and module practice
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

The first five labs are offline and synthetic, meaning they use bounded local
fixtures rather than live Claude requests. They do not require a Claude API key.

## Learning path

The course is organized as five modules and 30 lessons. The course map and
[source coverage matrix](course/SOURCE_COVERAGE_MATRIX.md) show how the
historical lecture concepts and the current harness controls map into the
learner path.

1. Evaluation foundations
2. Human review and evaluation cases
3. Automated checks and LLM-as-a-judge
4. Factuality, safety, and agent evaluation
5. Regression, release decisions, and the capstone

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
labs/         five runnable learner labs
slides/       slide outlines and recording guidance
scripts/      course validation and setup helpers
examples/     small supporting examples
```

## Current status

Available now:

- the complete 30-lesson learner guide and recording scripts;
- five offline, deterministic labs covering Modules 1–5;
- the source coverage matrix, fundamentals, glossary, and cream visual system;
- validation scripts for the generated guide; and
- links to the companion design guide, Apple lab, harness, website, and videos.

Planned or optional next steps:

- the full editable PowerPoint deck and lesson-by-lesson recording assets; and
- an opt-in live-Claude extension with explicit request, time, token, and spend
  limits.

Synthetic lab results are learning evidence, not proof of live Claude quality,
production safety, or business impact.
