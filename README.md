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

The first lab is intentionally offline. It gives you a fast result without a
Claude API key, so you can understand the evaluation contract before paying for
live model calls.

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
course/       learner guide, lesson map, and reusable templates
labs/         runnable learner labs
slides/       PowerPoint source and recording assets
scripts/      course validation and setup helpers
examples/     small supporting examples
```

## Status

The repository currently contains the course scaffold, Module 1 lesson scripts,
and the first runnable lab. The source coverage matrix now captures the
complete lesson requirements. The remaining build phases are the Module 2–5
scripts, runnable lab extensions, PowerPoint deck, and optional live-Claude
extension.
