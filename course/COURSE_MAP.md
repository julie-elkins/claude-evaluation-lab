# Course map

Start with the generated [learner guide](../GUIDE.md). It contains the
fundamentals, all 48 learner-facing lessons, all eight runnable labs, diagrams, and
module practice checks in one reading path. This file remains the compact
authoring map; the lesson scripts remain the editable recording source.

## Working title

**LLM & Agent Evaluation Lab: From Offline Evidence to Production-Oriented Assurance**

## Learner promise

By the end of the course, learners will be able to design an evaluation
workflow for an LLM application or agent, run it against representative test
cases, interpret the evidence, and explain what the result does and does not
prove. Claude provides the running provider examples, while the evaluation
contracts are designed to remain useful across providers. The advanced track
connects those evaluations to production-oriented assurance: telemetry, security
controls, monitoring, incident response, and the trace-to-test-case feedback
loop.

## Audience and prerequisites

The course is for developers, solutions architects, AI product teams, technical
leaders, and other practitioners who need to evaluate LLM behavior. Learners
should be comfortable reading JSON and running command-line examples. Python
experience is helpful but not required for the introductory labs.

## Modules and lessons

The course is organized as eleven modules and 48 lessons. The first five
modules teach evaluation foundations; the remaining modules connect evaluation
evidence to security controls and production-oriented assurance without making
live provider access a prerequisite.

### Module 1 — Evaluation foundations

1. What an evaluation is—and what it is not
2. Declaring the decision before choosing the metric
3. Transport status versus semantic outcome
4. Evidence contracts and terminal states

Hands-on outcome: identify a false pass in the existing teaching lab.

### Module 2 — Evaluation cases and human review

5. Building representative evaluation cases
6. Golden datasets, calibration sets, and held-out cases
7. Rubrics and reviewer calibration
8. Inter-rater agreement and disagreement review
9. Human-rating cost, speed, and agreement sessions

Hands-on outcome: create a small reviewed evaluation set, rubric, and
disagreement-review record.

### Module 3 — Automated evaluation

10. Deterministic checks
11. Reference-based metrics: METEOR, BLEU, and ROUGE
12. Why reference metrics miss valid variation
13. LLM-as-a-judge: inputs, scores, and rationales
14. Structured outputs and parseable evaluator results
15. Pointwise and pairwise judging
16. Judge bias: position, verbosity, and self-enhancement
17. Judge best practices, calibration, and evaluator layers
18. Independent breakers and negative controls

Hands-on outcome: compare a deterministic check, a judge result, human
calibration evidence, and a deliberately degraded case.

### Module 4 — Factuality, safety, and agents

19. Claim extraction and evidence support
20. Factuality evaluation for Claude responses
21. Weighted factuality and partial error
22. Safety, refusal, and prompt-injection evaluation
23. Tool routing, tool hallucination, and tool descriptions
24. Tool arguments, context, and state changes
25. Evaluating multi-step agent trajectories and recovery

Hands-on outcome: evaluate an agent workflow without allowing a plausible final
answer to hide a failed path, unsafe action, or missing evidence.

### Module 5 — Regression and release decisions

26. Benchmark categories: knowledge, reasoning, coding, safety, and agents
27. Benchmark contamination, Goodhart's law, and Pareto tradeoffs
28. Baselines, variants, uncertainty, high-risk slices, and evaluator layers
29. Revision binding, drift, release decisions, rollback, and monitoring
30. Capstone: produce an evaluation report and release recommendation

Hands-on outcome: run a bounded comparison and write a decision that names
blocking failures, uncertainty, and limitations.

### Module 6 — Production observability foundations

31. Observability versus evaluation
32. The agent telemetry model and trace contract

Hands-on outcome: define what a production trace must contain before it can
support debugging or an evaluation decision.

### Module 7 — Instrumentation and operational signals

33. OpenTelemetry spans and semantic conventions
34. Metrics, budgets, and service-level objectives

Hands-on outcome: map agent behavior to traces, metrics, budgets, and
actionable service-level objectives.

### Module 8 — Privacy, monitoring, and incident response

35. Redaction, retention, and access boundaries
36. Alerts, incidents, rollback, and ownership

Hands-on outcome: design a monitoring and incident path that preserves useful
evidence without treating raw prompts or tool payloads as automatically safe to
retain.

### Module 9 — Continuous evaluation and production capstone

37. Turning traces into evaluation cases
38. Connecting a bounded live Claude observation
39. Production observability capstone

Hands-on outcome: investigate a synthetic production trace, turn the failure
into a regression case, and make a bounded release or rollback decision.

### Module 10 — Security and assurance controls

40. Threat modeling and trust boundaries
41. Identity, least privilege, and secrets
42. Data, network, and supply-chain controls
43. Telemetry security and auditability
44. Monitor the monitor and resilience

Hands-on outcome: threat-model an agent, test authority and data boundaries,
protect telemetry evidence, and detect monitoring-path failure.

### Module 11 — Continuous assurance and production implementation

45. Build a local telemetry vertical slice
46. Drift, feedback, and evaluator recalibration
47. Side effects, concurrency, and human approval
48. Continuous assurance capstone

Hands-on outcome: follow telemetry from instrumentation to action, test drift and
side-effect controls, and produce a security-aware assurance decision.

## Production pattern

Every lesson will have:

- a short concept slide sequence;
- a learner objective;
- a runnable lab or guided inspection;
- a starting state;
- an expected result;
- a deliberately degraded or negative-control case;
- a troubleshooting section;
- a speaker script; and
- a statement of what the evidence does not prove.

## Currentness rule

The course separates durable evaluation principles from fast-changing examples.
Provider behavior, model names, benchmark versions, API syntax, and pricing
must be dated or verified before recording. The harness revision, evaluator
contract, and course examples must be recorded together so a later change can
trigger re-evaluation rather than silently reusing stale evidence.

## Source relationship

The Stanford lecture reviewed for this course provides conceptual reference
points such as human agreement, rule-based metrics, LLM-as-a-judge, factuality,
agent evaluation, benchmarks, and Goodhart's law. The lesson scripts will be
original and will not reproduce the lecture transcript.

The advanced track also uses Stanford's Engineering AI Agents course for agent
evaluation framing, DeepLearning.AI's Evaluating AI Agents course for
trace-to-evaluation workflows, Hugging Face's agent observability unit for the
observability/evaluation distinction, and OpenTelemetry's GenAI semantic
conventions for provider-neutral telemetry vocabulary. OWASP's GenAI Security
Project and NIST's Generative AI Profile inform the security and post-deployment
assurance extensions. These are reference points for design and currentness
checks, not copied course content.

## Continue learning

- [Julie’s YouTube channel](https://www.youtube.com/@JulieElkins) — optional video walkthroughs.
- [Julie’s public site](https://julie-elkins.github.io) — projects, learning paths, and design principles.
- [Agent Systems Design Guide](https://github.com/julie-elkins/agent-systems-design-guide) — shared design reasoning and report vocabulary.
- [Apple Platform Agent Quality Lab](https://github.com/julie-elkins/apple-platform-agent-quality-lab) — native macOS implementation of the evaluation boundary.
- [OpenTelemetry GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/) — provider-neutral trace and metric vocabulary; verify the current convention status before recording.
- [Phoenix](https://github.com/Arize-ai/phoenix) and [Langfuse](https://github.com/langfuse/langfuse) — optional observability backends for comparing local trace workflows.
- [Stanford Engineering AI Agents](https://cs329z.stanford.edu/) — agent evaluation and reliability framing.
- [Evaluating AI Agents](https://www.deeplearning.ai/courses/evaluating-ai-agents) — trace-to-evaluation and component-evaluation patterns.
- [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/bonus-unit2/what-is-agent-observability-and-evaluation) — observability and evaluation distinction.
- [OWASP GenAI Security Project](https://genai.owasp.org/llm-top-10/) — current threat categories and security control prompts.
- [NIST Generative AI Profile](https://www.nist.gov/itl/ai-risk-management-framework/ai-rmf-generative-ai-profile) — risk management and post-deployment assurance reference.
