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
5. **Final decision** — release, hold, revise, rollback, or escalate.

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
8. release, hold, revise, rollback, or escalate action; and
9. limitations and next evidence.

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
validation remain outside this synthetic course artifact.
