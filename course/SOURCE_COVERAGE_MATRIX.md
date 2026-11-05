# Source coverage matrix

This matrix is the completeness check for the course. It records where the
reviewed YouTube lecture and the current Agent Assurance Harness contribute to
the learner path.

The lecture is a historical conceptual source. It is not copied into the
scripts. The harness is the current operational source for evidence contracts,
negative controls, release decisions, and limits.

## Learner foundation coverage

These concepts are prerequisites for interpreting an agent evaluation. They are
introduced in `FUNDAMENTALS.md` and reinforced by the named lessons rather than
left as assumed measurement vocabulary.

| Foundation | Learner needs to understand | Course location | Hands-on treatment |
| --- | --- | --- | --- |
| Agent system under test | Request, environment, context and memory, tools, stopping criteria, scorer, trajectory, and final outcome. | Fundamentals; Lessons 5 and 25 | Write a case contract and annotate a bounded trajectory. |
| Three evaluation surfaces | Retrieval evidence, model response behavior, and agent orchestration are related but separate evaluation surfaces. | Fundamentals; Lessons 19, 23–25, and 37 | Classify one synthetic failure as retrieval, model, or agent-surface failure and name the evidence. |
| Agent development lifecycle | Define, build, test, release, deploy, monitor, and learn; the evidence and decision change by phase. | Fundamentals; Lessons 1, 29, 39, and 46 | Place a discovered failure in the lifecycle and turn it into a durable case. |
| Measurement foundations | Construct, validity, reliability, sensitivity, specificity, false positives, false negatives, and calibration. | Fundamentals; Lessons 7–9, 14, 16–18 | Compare workflow correctness, evaluator correctness, and evidence sufficiency. |
| Retrieval, memory, and environment | Retrieval recall, context relevance, context sufficiency, grounding, memory read/write, stale state, and environment reset. | Fundamentals; Lessons 19, 24, and 25 | Build a retrieval-and-claim table and compare before/after memory and state. |
| Memory consolidation | Background memory writing must be compared with a baseline and tested for retrieval, task benefit, stale or contradictory state, privacy, deletion, provenance, rollback, and cost. | Fundamentals; Lessons 24, 25, 32, 35, 37, and 46; optional extension | Compare synthetic baseline and treatment conditions with a held-out case and a deletion or rollback control. |
| Evaluation scope | Final-response, single-step, end-to-end, trajectory, and thread/session evaluation; turn-level success can differ from conversation-level success. | Fundamentals; Lessons 25, 32, and 39 | Label the evaluator scope and annotate a multi-turn synthetic trajectory with thread identity, memory, and conversation termination. |
| Sampling and uncertainty | Target population, case count, repeated runs, confidence intervals, effect size, practical significance, and high-risk slices. | Fundamentals; Lessons 6, 9, 27–30, and 46 | Write a matched comparison and interpret aggregate and slice results. |
| Failure analysis | Classify whether a finding came from data, model, prompt, retrieval, tool, policy, evaluator, or telemetry. | Lessons 29–30, 36–39, and 48 | Turn a failed case into a bounded cause hypothesis, owner, and next action. |

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
| Retrieval ranking | Ranking metrics such as NDCG@k can measure whether useful retrieved items appear near the top when ranking is part of the decision; they do not replace completeness, grounding, or task checks. | Fundamentals; Lessons 19 and 27 | Choose a ranking metric only when the declared decision requires it and pair it with evidence sufficiency. |
| Agent reliability across steps | Error propagation, uncertainty and evidence handoff, intermediate verification, stopping, asking, refusal, and escalation are distinct from final-answer accuracy. | Lessons 25 and 47 | Annotate a synthetic handoff with provenance, uncertainty, verification status, and a stop or escalation rule. |
| Benchmarks | Knowledge, reasoning, coding, safety, and agent benchmarks answer different questions. | Lesson 26 | Compare benchmark categories with a custom-use-case evaluation. |
| Benchmark limits | Benchmark contamination, data leakage, Goodhart's law, Pareto tradeoffs, and model-profile differences. | Lesson 27 | Write a limitation statement and a cost/safety/quality comparison. |
| Final principle | A benchmark result does not decide whether a model is right for a particular use case. | Lessons 27–30 | Capstone requires a use-case decision and explicit limitations. |

## Current harness coverage

The current public `origin/main` tree is `b64f5ca`. Its tree matches the local
course pin `b64f5ca`, so the course includes the latest public checklist
additions from the evaluator-checklist work. The latest additions are explicitly
mapped below rather than left implicit in the repository.

| Harness area | Required learner concepts | Course location | Reused harness material |
| --- | --- | --- | --- |
| Decision and requirements | Task, decision, failure cost, allowed sources/actions, terminal states. | Lessons 1–4 | `AGENT_EVALUATION_CHECKLIST.md` |
| Test cases and golden data | Representative coverage, expected outcomes, negative controls, calibration/held-out separation, failure-to-test loop. | Lessons 5–9 and 28 | Checklist and scenario packs |
| Deterministic evaluation | Correctness, schema, tool choice, arguments, authorization, state change, latency, cost, stop conditions. | Lessons 10, 23–25, and 28 | Synthetic scenario packs and teaching lab |
| Semantic evaluation | Groundedness, relevance, unsupported claims, grader validity, and explicit abstention. | Lessons 13–22 | Content-assurance packs and evaluator checklist |
| Evaluator layers | Deterministic checks cover schemas, tools, authorization, evidence, latency, and cost; semantic or agent grading must be calibrated or abstain. | Lessons 17 and 28 | Latest `Evaluator layers` checklist row |
| Behavioral and trajectory evaluation | Multi-turn state, recovery, consistency, safety, prompt injection, thread contamination, and conversation termination. | Lessons 22–25 and 32 | Scenario packs, shadow execution, and agent workflow lab |
| Agent architecture comparison | Flat versus multi-agent paths, subagent handoffs, skill/tool alternatives, model-upgrade re-baselining, cost, latency, context, recovery, and end-to-end task outcome. | Lessons 25, 28, and 39 | Guided synthetic comparison; no new required live or runnable lab |
| Trace and observability | Trace completeness, revision binding, privacy boundary, and visible skipped/refused/failed states. | Lessons 4, 28–29, and 31–48 | Run manifests, evidence provenance, Labs 6–8 |
| Controlled comparison | Correctness, safety, tool-call correctness, latency, cost, and user outcomes remain separate; thresholds and rerun policy precede interpretation. | Lessons 28–30 | Latest `Controlled variant comparison` checklist row |
| Evaluation-driven optimization | Use an evaluation to choose a candidate change; separate tuning from held-out cases, check grader consistency, observed noise, and remaining headroom, apply hard safety/evidence constraints before comparing quality, cost, and latency, change one factor at a time, and accept, reject, or revert based on generalization. | Lessons 28–29 and Lab 5 | Synthetic optimization contract with a held-out high-risk regression, constrained candidate frontier, and fresh-case follow-up |
| Change management | Revision impact, stale evidence, reauthorization, release ownership, containment, and rollback. | Lesson 29 | Change-impact examples, reauthorization, ship gate, rollback rehearsal |
| Monitoring and feedback | Production feedback, user outcomes, freshness, drift, telemetry health, and limitations. | Lessons 29 and 34–48 | Monitorability workbench, Labs 6–8, trace-to-case loop, and checklist |
| Online evaluator action loop | Score or classify arriving traces, filter by a declared rule, and route to human review, dataset candidates, investigation, or alert. | Lessons 39 and 46; Fundamentals | Use a synthetic routing record that preserves evaluator revision, rule, reason, owner, and status. |
| Production-scale triage | Sampling, grouping failure mechanisms, high-risk prioritization, evaluator volume/cost controls, human-review queues, and dataset-promotion rules. | Lessons 39 and 46 | Design an optional scale extension without making live traffic or a hosted backend required. |
| Deployment readiness boundaries | Durable execution, sandboxing, context management, human approval, rollback, and trace completeness are runtime controls beyond an offline pass. | Fundamentals; Lessons 29, 41, 42, and 47 | Add one runtime control and its evidence to a release record. |
| Platform-neutral implementation mapping | LangSmith, Phoenix, Langfuse, Promptfoo, and OpenTelemetry can implement parts of the workflow; platform presence does not establish evaluator validity. | Lessons 32–34 and 39; README | Map final-response, single-step, trajectory, trace, dataset, and review concepts to optional backends while keeping the required learner path local and synthetic. |
| Stateful memory implementation mapping | Provider-specific background memory workflows should map to provider-neutral write, read, provenance, safety, deletion, and rollback evidence. | Optional memory-consolidation extension; Lessons 24, 35, 37, and 46 | Use the official cookbook as an implementation reference, then evaluate the declared workflow rather than copying its claims. |
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
| Trace-to-evaluator design | Trace evidence profiling, root-cause hypotheses, diagnostic replay, full validation, recurring failure mechanisms, evaluator-contract drafting, minimized case creation, negative controls, and human adoption decision. | Lesson 37; optional `TRACE_TO_EVALUATOR_SKILL.md` | Apply the workflow to synthetic Lab 6 traces; real traces remain private and approved. |
| Live provider extension | Bounded model, request, time, token, spend, privacy, and approval limits. | Lesson 38 and optional adapter | Keep live access separate from the required path. |
| Security threat model and red teaming | Assets, actors, entry points, trust boundaries, consequences, attack hypotheses, rules of engagement, preventive/detective/response controls, and attack-to-regression conversion. | Lesson 40 and Lab 7 | Draw a synthetic abuse path, inspect `red_team_cases`, and convert an unblocked attack into a regression case. |
| Identity and authority | Principal, least privilege, tenant scope, credential isolation, approval, and audit evidence. | Lesson 41 and Lab 7 | Catch over-privileged, secret-exposing, and missing-approval cases. |
| Data, network, and supply chain | Tenant boundaries, egress policy, output validation, tool provenance, dependency revision, and side-effect protection. | Lessons 42 and 47; Lab 7 | Run synthetic boundary, provenance, idempotency, and stale-state failures. |
| Telemetry security | Classification, access role, retention, deletion, evidence preservation, and auditability. | Lesson 43 and Lab 7 | Keep a complete task result separate from a secure telemetry result. |
| Monitor health and resilience | Received, accepted, rejected, dropped, delayed, and exported telemetry; alert quality; bounded fallback. | Lesson 44 and Lab 8 | Break the local telemetry path and preserve `unavailable` or `not_evaluated`. |
| Local telemetry implementation | Instrumentation, collection, redaction, local storage, query, alert, incident, and regression case. | Lesson 45 and Lab 8 | Trace one synthetic run across all pipeline stages. |
| Drift and recalibration | Data, model, evaluator, and concept drift; human feedback; sampling; recalibration. | Lesson 46 | Compare synthetic distributions and declare a review action. |
| Official provider guidance | Claude evaluations and skills, Codex skills and `AGENTS.md`, current Codex evaluation-suite guidance with optional Promptfoo execution, LangSmith evaluator scopes and review queues, LangGraph durable execution, and the developing OpenTelemetry GenAI conventions. | Fundamentals; Lessons 25, 28, 33, 37, and 39; README | Record provider documentation revision or retrieval date, map provider features to the provider-neutral evidence contract, and keep older platform references out of the required path. |
| Continuous assurance | Security, telemetry health, evaluation, incidents, ownership, and release action remain connected. | Lesson 48 and Labs 7–8 | Produce one combined assurance report with bounded claims. |

## Red-team coverage

The course uses **red teaming**, meaning bounded adversarial testing of an
agent's behavior under hostile, manipulative, or boundary-seeking conditions,
as a security-evaluation method rather than a universal score. The required
path covers these synthetic categories:

| Attack category | Learner treatment | Evidence |
| --- | --- | --- |
| Indirect prompt injection | Treat untrusted retrieved content as data, not authority. | Lab 7 blocked and unblocked synthetic cases. |
| Tool misuse and privilege escalation | Check authorization, scope, arguments, approval, and side effects. | Lessons 23–24, 41, and Lab 7. |
| Data exfiltration and tenant escape | Check credential, telemetry, tenant, and network boundaries. | Lessons 35, 40–43, and Lab 7. |
| Unsafe side effects | Require output validation, idempotency, compensation, and human approval. | Lessons 24, 41, 47, and Lab 7. |
| Resource exhaustion | Enforce budgets, retry bounds, and stopping criteria. | Lessons 34, 40, 44, and Lab 7. |
| Regression conversion | Turn a confirmed weakness into a versioned case with an owner and release consequence. | Lessons 29, 36–40, and Lab 7. |

Jailbreaks and vendor-specific attack corpora remain optional references. The
public required path does not run live attacks, use real credentials, or claim
broad resistance from a small synthetic suite.

## Completeness rule

A topic is not considered included merely because it appears in this table. It
must also have a lesson explanation, a slide anchor, and either a runnable lab,
a guided inspection, or an explicit reason it remains conceptual.
