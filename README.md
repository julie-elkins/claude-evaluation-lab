# LLM & Agent Evaluation Lab

Hands-on lessons for building and interpreting LLM and agent evaluations, using
Claude as a running provider example and Codex as an optional coding-agent
evaluation boundary, then connecting those evaluations to production-oriented
assurance.

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
- a prompt failure from an environment, tool, code, orchestration, evaluator,
  or model failure;
- a cheap diagnostic replay from full end-to-end validation; and
- an isolated subagent result from evidence that the whole architecture
  improved the user's task.
- a candidate change that improves tuning cases from a change that generalizes
  to held-out cases; and
- an accuracy result from a reliable process that preserves uncertainty,
  verifies important intermediate steps, and stops or escalates safely; and
- a red-team attempt from a complete security-evaluation loop that turns an
  observed weakness into a regression case.

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

For the companion research record, see the
[response-quality measurement study](https://github.com/julie-elkins/llm-eval-validity/tree/main/research/response-quality).
The course teaches the design and execution patterns; the research repository
records the frozen provider results and their narrower claim boundary.

For optional video walkthroughs and related projects, visit
[Julie’s YouTube channel](https://www.youtube.com/@JulieElkins) and
[Julie’s public site](https://julie-elkins.github.io).

## Prerequisites

- Python 3.11 or newer.
- [`uv`](https://docs.astral.sh/uv/) for running the course commands.
- Comfort reading JSON and using a terminal. Python experience is helpful but
  not required for the introductory labs.

The required labs are offline and synthetic, meaning they use bounded local
fixtures rather than live Claude or Codex requests. They do not require a
provider API key.

## Reuse and licensing

Runnable code is licensed under the [MIT License](LICENSE). Educational
material—including lessons, diagrams, lab explanations, and slide guidance—is
licensed under [Creative Commons Attribution 4.0 International](CONTENT-LICENSE.md).
This split keeps software reuse permissive while requiring attribution when
course content is reused or adapted.

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
   inspect high-risk slices, evaluate a candidate optimization against held-out
   cases, and make a bounded release recommendation.
6. [Production observability](labs/06-production-observability/README.md) —
   inspect traces, operational signals, privacy boundaries, and incident
   evidence.
7. [Security controls](labs/07-security-controls/README.md) — test trust
   boundaries, least privilege, telemetry access, side-effect controls, and
   the synthetic red-team-to-regression workflow.
8. [Telemetry vertical slice](labs/08-telemetry-vertical-slice/README.md) —
   follow local evidence from instrumentation through alerting and regression.

Optional:

- [Optional live-Claude adapter](labs/optional-live-claude-adapter/README.md) —
  connect one live provider observation to the same evidence contract under explicit
  request, time, token, spend, and privacy limits.
- [Optional Codex coding-agent evaluation](labs/optional-codex-agent-adapter/README.md) —
  evaluate repository scope, commands, tests, patch evidence, safety, and
  human review without requiring live Codex access.
- [Optional Trace-to-Evaluator Design Skill](course/TRACE_TO_EVALUATOR_SKILL.md) —
  inspect approved or synthetic traces, identify recurring failure mechanisms,
  classify root-cause hypotheses, use replay as a diagnostic filter, require
  full validation, and draft a use-case-specific evaluator without treating
  the recommendation as production approval.

## Quick start

Clone both repositories beside each other:

```bash
git clone https://github.com/julie-elkins/claude-evaluation-lab.git
git clone https://github.com/julie-elkins/agent-assurance-harness.git
cd claude-evaluation-lab
uv run python labs/01-semantic-outcomes/run_lab.py
```

The course wrapper uses the harness content tree from revision
`5afed78`, which is the current public
`origin/main` tree as of the course audit. If you are working from a local
checkout, the wrapper verifies the pinned revision before running the lab.

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
labs/         eight runnable learner labs plus optional provider extensions
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
- a CI contract that rebuilds the guide, runs the contract tests, and runs all
  eight required labs; and
- links to the companion design guide, Apple lab, harness, website, videos,
  OpenTelemetry, Phoenix, Langfuse, LangSmith, and the optional Codex
  coding-agent track.
- an optional memory-consolidation evaluation extension that compares a
  background memory workflow with a baseline using held-out cases, safety
  controls, provenance, deletion, rollback, and cost evidence.

Reference courses and standards used for the advanced track:

- [Stanford Engineering AI Agents](https://cs329z.stanford.edu/) — agent
  evaluation and reliability framing.
- [Evaluating AI Agents](https://www.deeplearning.ai/courses/evaluating-ai-agents)
  — trace-to-evaluation and component-evaluation patterns.
- [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/bonus-unit2/what-is-agent-observability-and-evaluation)
  — the observability and evaluation distinction.
- [Building Reliable Agents with LangSmith](https://academy.langchain.com/courses/take/building-reliable-agents)
  — tracing, thread grouping, offline and online evaluation, evaluators, and
  production feedback loops. This is an optional comparison point, not a
  required hosted-backend lab.
- [Claude evaluation guidance](https://docs.anthropic.com/en/docs/build-with-claude/define-success)
  and [Claude Code skills](https://docs.anthropic.com/en/docs/claude-code/slash-commands)
  — success criteria, graders, skill evaluation, and model-upgrade re-baselining.
- [OpenAI agent evaluations](https://developers.openai.com/api/docs/guides/agent-evals)
  and [trace grading](https://developers.openai.com/api/docs/guides/trace-grading)
  — traces, graders, datasets, evaluation runs, and trace-level inspection.
- [OpenAI Evals API lifecycle notice](https://developers.openai.com/api/docs/guides/evals/)
  — a reminder to check provider lifecycle status; the platform became
  read-only on October 31, 2026 and is scheduled to shut down on November 30,
  2026, so it is not a required course dependency.
- [Meta AI Research](https://ai.meta.com/research) — optional Muse research and
  safety material for comparing agentic-task, reliability, preparedness, and
  evaluation framing. This is not a live Muse adapter or a course benchmark.
- [Anthropic Claude Cookbook: Dreaming with a dynamic workflow](https://platform.claude.com/cookbook/managed-agents-cma-dreaming-with-a-dynamic-workflow)
  — optional implementation reference for background memory consolidation.
- [Codex skills](https://developers.openai.com/codex/skills/create-skill),
  [`AGENTS.md`](https://developers.openai.com/codex/guides/agents-md), [Codex
  evals](https://developers.openai.com/codex/use-cases/ai-app-evals), and
  [Promptfoo](https://github.com/promptfoo/promptfoo) — instruction scope,
  coding-agent skills, evaluation-suite workflows, and runner options. The
  older OpenAI Evals repository is historical context, not a required course
  dependency.
- [LangSmith evaluation](https://docs.langchain.com/langsmith/evaluation),
  [automation rules](https://docs.langchain.com/langsmith/rules), and
  [annotation queues](https://docs.langchain.com/langsmith/annotation-queues) —
  offline/online evaluation, review routing, and dataset promotion.
- [LangGraph](https://docs.langchain.com/langgraph) — durable execution and
  human-in-the-loop state boundaries.
- [OWASP GenAI Security Project](https://genai.owasp.org/llm-top-10/) —
  security threat categories for generative AI systems.
- [NIST Generative AI Profile](https://www.nist.gov/itl/ai-risk-management-framework/ai-rmf-generative-ai-profile)
  — risk management and post-deployment assurance.
- [Promptfoo](https://github.com/promptfoo/promptfoo), [garak](https://github.com/NVIDIA/garak),
  [PyRIT](https://github.com/Azure/PyRIT), and
  [Giskard](https://github.com/Giskard-AI/giskard) — optional red-team and
  adversarial-testing references. They are not required dependencies because
  tool interfaces and attack corpora change quickly.

Research reading that informs the evaluation design:

- [Measurement to Meaning: A Validity-Centered Framework for AI Evaluation](https://arxiv.org/abs/2505.10573)
  — construct validity, decision scope, and evidence boundaries.
- [Establishing Best Practices for Building Rigorous Agentic Benchmarks and the Agentic Benchmark Checklist (ABC)](https://arxiv.org/abs/2507.02825)
  — task setup, reward design, environment, benchmark, and reporting discipline.
- [No Free Labels: Limitations of LLM-as-a-Judge Without Human Grounding](https://arxiv.org/abs/2503.05061)
  — human grounding and calibration for model-based judges.
- [Quantifying Variance in Evaluation Benchmarks](https://arxiv.org/abs/2406.10229)
  — repeated measurement and uncertainty.
- [Agent Evaluation Reliability](https://arxiv.org/abs/2610.00651)
  — why more cases do not automatically repair a weak instrument.
- [Measuring AI Ability to Complete Long Software Tasks](https://arxiv.org/abs/2503.14499)
  — human-anchored task duration and reliability thresholds for long-horizon work.
- [A Live Benchmark and Automated Evaluation for Generative Research Synthesis](https://arxiv.org/abs/2508.20033)
  — knowledge synthesis, retrieval quality, and citation verifiability.
- [Do Agent Benchmarks Measure Capability?](https://arxiv.org/abs/2607.22368)
  — protocol validity and shortcut-resistant scoring.
- [Towards a Science of AI Agent Reliability](https://arxiv.org/abs/2602.16666)
  — distinct dimensions of agent reliability.
- [Harness Self-Evolution for Long-Horizon Terminal Agents](https://arxiv.org/abs/2610.27435)
  — harness changes, long-horizon behavior, and repeated-run measurement.
- [Trial by Trace: Benchmarking AI Agent Harnesses for Reliability and Failure Attribution](https://arxiv.org/abs/2610.32285)
  — harness-level reliability and task-level failure attribution.
- [Beneath the Surface: What We Overlook When We Talk About Agent Evolution](https://arxiv.org/abs/2611.07624)
  — hidden regressions, cost, and preservation-aware interpretation of aggregate gains.
- [The Horizon Gap](https://arxiv.org/abs/2608.06663)
  — distinctions among long-horizon planning, memory, execution, training, and evaluation.

These readings are evidence about evaluation design, not proof that the
course's synthetic labs measure the same constructs. The course keeps
long-horizon reliability, professional-task quality, research synthesis, and
user outcomes as separate measurement surfaces.

Separate recording deliverable:

- the full editable PowerPoint deck and lesson-by-lesson recording assets are
  maintained separately from this learner-facing repository.

Synthetic lab results are learning evidence, not proof of live Claude quality,
production safety, or business impact.

The repository contains the learner guide, lesson scripts, lab implementations,
and recording guidance. The editable PowerPoint deck remains a separate
recording deliverable.
