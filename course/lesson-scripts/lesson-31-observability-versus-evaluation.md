# Lesson 31: Observability Versus Evaluation

Module: 6 — Production Observability Foundations
Suggested runtime: 10–12 minutes
Primary lab: Lab 6 — Observe the agent before you trust the dashboard

## Learner objective

By the end of this lesson, you can distinguish telemetry that explains what
happened from evaluation evidence that supports a decision.

## Slide and recording plan

1. **Observability asks what happened** — reconstruct the run.
2. **Evaluation asks whether it was acceptable** — apply a declared rule.
3. **A dashboard is not a release decision** — activity can look healthy while
   the agent violates a boundary.
4. **The production feedback loop** — trace, review, case, regression, decision.
5. **Demo: classify the Lab 6 trace results**.

## Speaker script

Observability is the practice of collecting enough telemetry to explain what a
system did. Telemetry includes traces, events, and metrics. Evaluation is the
separate practice of applying criteria to behavior so an owner can decide what
to do.

A trace can show that an agent selected a tool, sent arguments, received an
error, retried twice, and eventually stopped. That is useful evidence about the
path. It does not by itself prove that the tool was authorized, that the final
answer was correct, or that the workflow is safe to release.

An evaluation can say that the tool was unauthorized or that the required state
change did not occur. It cannot explain the finding if the trace omitted the
tool span, the authorization context, or the state before and after the call.
The production control therefore needs both reconstruction evidence and
judgment evidence.

In the demo, run Lab 6 and compare the healthy trace with the planted failures.
Point out that the metrics remain visible even when the candidate release
decision is blocked. A cost number is a signal; a declared spend threshold is
the rule that turns the signal into an action.

The cost of confusing observability with evaluation is a dashboard that proves
the system was busy but cannot support a safe decision. The cost of collecting
telemetry without a privacy boundary is a different failure: the evidence may
be useful but unsafe to retain or share.

## Demo notes

- Run `uv run python labs/06-production-observability/run_lab.py`.
- Compare `case_results`, `metrics`, and `candidate_release_decision`.
- Recording boundary: use synthetic trace identifiers and do not show raw
  prompts or production payloads.

## Learner practice

Create a two-column table for one agent workflow:

| Observability can show | Evaluation must decide |
|---|---|
|  |  |

Add one field that is required for both columns and explain why.

## What this lesson does not prove

A complete trace does not prove that the behavior was acceptable. A passing
evaluation does not prove that the trace captured every event. Production
confidence requires both a declared evaluation boundary and evidence that the
instrumentation is complete enough for that boundary.
