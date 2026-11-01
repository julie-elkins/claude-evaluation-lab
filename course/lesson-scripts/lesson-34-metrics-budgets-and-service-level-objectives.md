# Lesson 34: Metrics, Budgets, and Service-Level Objectives

Module: 7 — Instrumentation and Operational Signals
Suggested runtime: 10–12 minutes
Primary lab: Lab 6 — Observe the agent before you trust the dashboard

## Learner objective

By the end of this lesson, you can separate operational signals from quality
evidence and define a service-level objective for an agent workflow.

## Slide and recording plan

1. **Signals are not decisions** — latency, tokens, cost, errors, and retries.
2. **Quality and operations interact** — a faster wrong answer is not an
   improvement.
3. **Budgets** — token, spend, time, retry, and side-effect limits.
4. **Service-level objectives** — explicit targets and windows.
5. **Demo: inspect the Lab 6 cost and retry findings**.

## Speaker script

An operational metric is a measurement of how the system ran. Examples include
latency, token usage, estimated cost, retry count, tool error rate, and
escalation rate. These signals help an owner detect a problem, but they do not
automatically answer whether the task was correct or safe.

A budget is a declared limit. It can bound time, tokens, spend, retries, loop
depth, or side effects. A service-level objective, or SLO, is an explicit target
for a service signal over a defined window. For example, a workflow may require
that 99 percent of bounded requests finish below a latency target while
high-risk tool failures remain zero.

Keep quality and operations separate in the report. A variant that lowers cost
but increases unauthorized actions has not improved the system for the stated
decision. Likewise, an evaluation may pass its quality criteria while exceeding
the cost ceiling that makes the workflow viable.

In the demo, inspect `trace-cost-spike-001` and `trace-retry-loop-001`. The
metrics remain visible, and the evaluator applies explicit thresholds. This is
why a dashboard should show both the measurement and the action rule.

The cost of aggregate metrics without slices is hidden risk. A healthy average
can hide a high-risk workflow that is slow, expensive, or unsafe every time.

## Demo notes

- Run Lab 6 and inspect `metrics`, `estimated_cost_usd`, and `retry_count`.
- Write one quality threshold and one operational threshold.
- Recording boundary: all budgets remain synthetic and illustrative.

## Learner practice

Define one bounded workflow contract with:

`latency_target`, `spend_limit`, `retry_limit`, `quality_threshold`,
`high_risk_blocking_rule`, and `owner`.

Explain which field would trigger an immediate hold.

## What this lesson does not prove

A synthetic threshold is not a production SLO. Real targets require traffic,
cost, risk, and user-outcome evidence from the environment where the workflow
operates.
