# Source coverage matrix

This matrix is the completeness check for the course. It records where the
reviewed YouTube lecture and the current Agent Assurance Harness contribute to
the learner path.

The lecture is a historical conceptual source. It is not copied into the
scripts. The harness is the current operational source for evidence contracts,
negative controls, release decisions, and limits.

## YouTube lecture coverage

| Lecture area | Required learner concepts | Course location | Hands-on treatment |
| --- | --- | --- | --- |
| Introduction | Evaluation can mean output quality, latency, pricing, availability, or other system properties; this course must declare its scope. | Lessons 1–2 and 29 | Learner writes the decision and names out-of-scope properties. |
| Human evaluation | Human ratings are expensive, slow, and subjective. | Lessons 5–9 | Build a rubric, review cases, record disagreements, and decide when calibration is required. |
| Inter-rater agreement | Agreement rate can be misleading because raters may agree by chance; Cohen's kappa, Fleiss's kappa, and Krippendorff's alpha are examples. | Lessons 8–9 | Compare raw agreement with a chance-adjusted interpretation; state that the metric does not replace disagreement review. |
| Rule-based metrics | Fixed references can reduce repeated human work but require reference outputs. | Lessons 10–12 | Run a fixed-rule check and inspect its reference dependency. |
| METEOR, BLEU, and ROUGE | Precision, recall, n-gram overlap, ordering, brevity, and summarization use cases. | Lesson 11 | Use small synthetic examples and show why the formula is not a universal quality measure. |
| Reference limits | Paraphrases and stylistic variation can be valid even when lexical overlap is low; metric correlation with human judgment is imperfect. | Lesson 12 | Compare semantically equivalent responses with different wording. |
| LLM-as-a-judge | Judge inputs include prompt, response, and criteria; outputs may include score and rationale. | Lesson 13 | Create a judge contract and compare it with a human rubric. |
| Structured outputs | Constrained or structured output makes judge results parseable, but does not guarantee a valid judgment. | Lesson 14 | Validate a schema and then separately evaluate the judgment. |
| Judge variants | Pointwise judging evaluates one response; pairwise judging compares two responses and can produce preference data. | Lesson 15 | Run both forms on synthetic responses. |
| Judge bias | Position, verbosity, self-enhancement, and alignment bias can distort a judge. | Lesson 16 | Swap response order, normalize length, and compare judge output with human reference. |
| Judge best practices | Crisp criteria, binary scales where appropriate, rationale before score, calibration against humans, and low temperature for repeatability. | Lesson 17 | Record the calibration set, judge settings, and disagreement review. |
| Evaluation dimensions | Task performance includes usefulness, relevance, and factuality; alignment includes style, tone, and safety. | Lessons 2, 17, 20, and 22 | Separate dimensions instead of collapsing them into one score. |
| Factuality | Extract claims, check each claim against evidence, and aggregate partial correctness. | Lessons 19–21 | Use synthetic claims and approved evidence identifiers. |
| Agent evaluation | Decompose observe/plan/act or tool-call loops; evaluate routing, tool choice, arguments, execution, and final interpretation. | Lessons 23–25 | Reuse harness scenarios and inspect the trajectory, not only the final text. |
| Benchmarks | Knowledge, reasoning, coding, safety, and agent benchmarks answer different questions. | Lesson 26 | Compare benchmark categories with a custom-use-case evaluation. |
| Benchmark limits | Benchmark contamination, data leakage, Goodhart's law, Pareto tradeoffs, and model-profile differences. | Lesson 27 | Write a limitation statement and a cost/safety/quality comparison. |
| Final principle | A benchmark result does not decide whether a model is right for a particular use case. | Lessons 27–30 | Capstone requires a use-case decision and explicit limitations. |

## Current harness coverage

The current public `origin/main` tree is `2f95f4c`. Its tree matches the local
course pin `3d69db3`, so the course already includes the latest content change
from the evaluator-checklist work. The latest additions are explicitly mapped
below rather than left implicit in the repository.

| Harness area | Required learner concepts | Course location | Reused harness material |
| --- | --- | --- | --- |
| Decision and requirements | Task, decision, failure cost, allowed sources/actions, terminal states. | Lessons 1–4 | `AGENT_EVALUATION_CHECKLIST.md` |
| Test cases and golden data | Representative coverage, expected outcomes, negative controls, calibration/held-out separation, failure-to-test loop. | Lessons 5–9 and 28 | Checklist and scenario packs |
| Deterministic evaluation | Correctness, schema, tool choice, arguments, authorization, state change, latency, cost, stop conditions. | Lessons 10, 23–25, and 28 | Synthetic scenario packs and teaching lab |
| Semantic evaluation | Groundedness, relevance, unsupported claims, grader validity, and explicit abstention. | Lessons 13–22 | Content-assurance packs and evaluator checklist |
| Evaluator layers | Deterministic checks cover schemas, tools, authorization, evidence, latency, and cost; semantic or agent grading must be calibrated or abstain. | Lessons 17 and 28 | Latest `Evaluator layers` checklist row |
| Behavioral and trajectory evaluation | Multi-turn state, recovery, consistency, safety, and prompt injection. | Lessons 22–25 | Scenario packs, shadow execution, and agent workflow lab |
| Trace and observability | Trace completeness, revision binding, privacy boundary, and visible skipped/refused/failed states. | Lessons 4, 28–29, and 31–48 | Run manifests, evidence provenance, Labs 6–8 |
| Controlled comparison | Correctness, safety, tool-call correctness, latency, cost, and user outcomes remain separate; thresholds and rerun policy precede interpretation. | Lessons 28–30 | Latest `Controlled variant comparison` checklist row |
| Change management | Revision impact, stale evidence, reauthorization, release ownership, containment, and rollback. | Lesson 29 | Change-impact examples, reauthorization, ship gate, rollback rehearsal |
| Monitoring and feedback | Production feedback, user outcomes, freshness, drift, telemetry health, and limitations. | Lessons 29 and 34–48 | Monitorability workbench, Labs 6–8, trace-to-case loop, and checklist |
| Teaching workflow | Demo, hands-on lab, quick reference, feedback signal, and human approval boundary. | Every module and capstone | `SHOWCASE.md` launch-to-field path |

## Production observability coverage

| Production area | Required learner concepts | Course location | Hands-on treatment |
| --- | --- | --- | --- |
| Observability versus evaluation | Telemetry explains execution; evaluation judges behavior against a decision. | Lessons 31–32 | Classify trace evidence and evaluation evidence in Lab 6. |
| Trace contract | Stable identity, revisions, spans, events, terminal state, and completeness. | Lesson 32 | Inspect complete and incomplete synthetic traces. |
| Instrumentation vocabulary | Workflow, model, tool, state, evaluator, and terminal spans with provider-neutral meaning. | Lesson 33 | Map Lab 6 fields to OpenTelemetry-shaped conventions. |
| Operational signals | Latency, tokens, cost, retries, errors, budgets, and SLOs. | Lesson 34 | Trigger synthetic spend and retry controls. |
| Privacy boundary | Redaction, retention, access ownership, and public-data limits. | Lesson 35 | Catch a raw-content trace and write a retention rule. |
| Incident response | Alert thresholds, severity, ownership, containment, rollback, and review. | Lesson 36 | Turn Lab 6 findings into incident records. |
| Continuous evaluation | Trace sampling, failure classification, safe minimization, regression cases, drift review, and release decisions. | Lessons 37–39 and 46–48 | Generate trace-to-case candidates, recalibrate, and complete the capstone. |
| Live provider extension | Bounded model, request, time, token, spend, privacy, and approval limits. | Lesson 38 and optional adapter | Keep live access separate from the required path. |
| Security threat model | Assets, actors, entry points, trust boundaries, consequences, and preventive, detective, and response controls. | Lesson 40 and Lab 7 | Draw a synthetic abuse path and inspect control coverage. |
| Identity and authority | Principal, least privilege, tenant scope, credential isolation, approval, and audit evidence. | Lesson 41 and Lab 7 | Catch over-privileged, secret-exposing, and missing-approval cases. |
| Data, network, and supply chain | Tenant boundaries, egress policy, output validation, tool provenance, dependency revision, and side-effect protection. | Lessons 42 and 47; Lab 7 | Run synthetic boundary, provenance, idempotency, and stale-state failures. |
| Telemetry security | Classification, access role, retention, deletion, evidence preservation, and auditability. | Lesson 43 and Lab 7 | Keep a complete task result separate from a secure telemetry result. |
| Monitor health and resilience | Received, accepted, rejected, dropped, delayed, and exported telemetry; alert quality; bounded fallback. | Lesson 44 and Lab 8 | Break the local telemetry path and preserve `unavailable` or `not_evaluated`. |
| Local telemetry implementation | Instrumentation, collection, redaction, local storage, query, alert, incident, and regression case. | Lesson 45 and Lab 8 | Trace one synthetic run across all pipeline stages. |
| Drift and recalibration | Data, model, evaluator, and concept drift; human feedback; sampling; recalibration. | Lesson 46 | Compare synthetic distributions and declare a review action. |
| Continuous assurance | Security, telemetry health, evaluation, incidents, ownership, and release action remain connected. | Lesson 48 and Labs 7–8 | Produce one combined assurance report with bounded claims. |

## Completeness rule

A topic is not considered included merely because it appears in this table. It
must also have a lesson explanation, a slide anchor, and either a runnable lab,
a guided inspection, or an explicit reason it remains conceptual.
