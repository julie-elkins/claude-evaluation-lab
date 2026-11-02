# Lesson 39: Production Observability Capstone

Module: 9 — Continuous Evaluation and Production Capstone
Suggested runtime: 15–20 minutes
Primary lab: Lab 6 — Observe the agent before you trust the dashboard

## Learner objective

By the end of this lesson, you can investigate a production-style agent trace,
create a regression case, and make a bounded operational decision.

## Slide and recording plan

1. **The capstone question** — can this evidence support the next action?
2. **Trace reconstruction** — what happened and what is missing?
3. **Operational findings** — quality, safety, cost, privacy, and telemetry.
4. **Incident to regression** — preserve the lesson without copying the data.
5. **Offline-to-online-to-offline assurance loop**.
6. **Online evaluator to action** — score, filter, review, investigate, and
   promote.
7. **Scale and triage** — sampling, grouping, prioritization, and cost control.
8. **Shadow and A/B evaluation boundaries**.
9. **Final decision** — release, hold, revise, rollback, or escalate.

## Speaker script

The production observability capstone connects the course's two evidence paths.
First, reconstruct the agent run from telemetry. Then evaluate the behavior
against the declared contract. Finally, decide what operational action follows.

Begin with completeness. Can we identify the workflow, revisions, spans,
terminal state, and privacy status? If not, mark the result
`not_evaluated` and explain what evidence is missing. Do not let a successful
transport or a fluent final answer fill the gap.

Next, inspect findings across dimensions. A tool may be unauthorized, a state
transition may be missing, a retry loop may exceed budget, or a raw payload may
violate the retention boundary. Keep these findings separate because they have
different owners and different fixes.

Convert the important failure into a safe regression case. Record the mechanism,
expected outcome, evidence requirement, and dataset role. Then make the
decision: release, hold, revise, rollback, or escalate. Name the owner,
monitoring signal, rollback trigger, and review date.

The production loop does not end when the dashboard turns green. Start with an
offline baseline, make a bounded release, observe online behavior, triage and
review candidate failures, minimize and sanitize the evidence, and add the
appropriate case to a regression or held-out set. Rerun the offline evaluation
before using the new evidence to support the next release decision.

In a production-oriented system, the online evaluator should lead to an
explicit action path. A trace arrives, an online evaluator scores or classifies
it, and an automation filters the result using a declared rule. The automation
may route the trace to human review, mark it as a dataset candidate, open an
investigation, or raise an alert. Preserve the input signal, evaluator
revision, rule, reason, owner, and resulting status; an automated route is not
the same thing as a verified label.

At larger volumes, add controls for sampling, grouping or clustering related
failure mechanisms, prioritizing high-risk cases, limiting evaluator cost and
latency, managing human-review queues, and defining when a reviewed case may
enter a regression or held-out dataset. The required lab remains small and
offline. This is the production design extension learners should be able to
describe before adopting a hosted backend.

Tools such as LangSmith, Phoenix, or Langfuse can host pieces of this workflow,
including traces, threads, datasets, evaluators, feedback, and automations.
The platform is an implementation choice; it does not establish that the
evaluator is valid or that the evidence supports a release decision.

There are two useful online comparison patterns. In **shadow testing**, a
candidate receives copied traffic but its result is not shown to the user and
its tools cannot create side effects. Shadow evidence can reveal unexpected
inputs and cost or latency changes, but it does not prove that the candidate is
safe to expose. In **A/B testing**, an assignment rule sends different users to
different versions. A/B results can compare outcomes, but they require privacy
controls, harm guardrails, predefined success criteria, and a rollback plan.

In the demo, run Lab 6 and complete the evidence template. The candidate
decision should be blocked because the trace set contains planted failures.
The learner's report should explain what would have to change before a bounded
release could be reconsidered.

The cost of a capstone that only displays a dashboard is that it stops before
accountability. The cost of a capstone that only writes an evaluation score is
that it cannot guide incident response. The useful artifact connects evidence
to action.

## Demo notes

- Run `uv run python labs/06-production-observability/run_lab.py --output
  /tmp/observability-report.json`.
- Fill the incident and regression sections from the report.
- State explicitly that the run is synthetic and offline.
- Show the offline-to-online-to-offline loop as a design pattern, not as a live
  traffic experiment.
- Show the online-evaluator action loop with a synthetic trace, a declared
  filter, and one routed action.
- Discuss sampling, failure grouping, high-risk prioritization, evaluator
  volume/cost limits, human-review queues, and dataset-promotion rules as
  optional production-scale extensions.
- Compare shadow testing and A/B testing in a short boundary table:
  who sees the result, whether side effects are allowed, what evidence is
  collected, and what safety controls are required.
- Recording boundary: do not imply the capstone represents a production
  deployment or live Claude quality.

## Learner practice

Complete a capstone report with:

1. decision and scope;
2. trace schema and revisions;
3. telemetry completeness;
4. operational signals and budgets;
5. privacy and retention boundary;
6. incident findings and owners;
7. regression cases created;
8. online-signal interpretation and feedback limitations;
9. online evaluator revision, routing rule, action owner, and resulting status;
10. scale controls for sampling, prioritization, review queues, and evaluator
    cost;
11. release, hold, revise, rollback, or escalate action; and
12. limitations and next evidence.

> **Learner checkpoint — review the capstone**
>
> Ask a peer:
>
> 1. Can they reconstruct the agent path?
> 2. Can they distinguish a missing trace from a failed task?
> 3. Can they identify the owner and next safe action?

## What this lesson does not prove

A completed capstone does not prove production readiness. It demonstrates a
repeatable reasoning path from telemetry to evaluation to action. Deployment,
access controls, real traffic, on-call response, and environment-specific
validation remain outside this synthetic course artifact. The course's
shadow and A/B discussion is conceptual; it does not authorize live traffic
experimentation or prove that a feedback signal is a valid outcome label.
