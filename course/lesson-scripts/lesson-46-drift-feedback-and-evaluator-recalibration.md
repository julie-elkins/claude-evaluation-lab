# Lesson 46: Drift, Feedback, and Evaluator Recalibration

Module: 11 — Continuous assurance and production implementation
Suggested runtime: 12–15 minutes
Primary lab: Lab 8 — Build the local telemetry vertical slice

## Learner objective

By the end of this lesson, you can detect changes in traffic, behavior,
evaluator agreement, and user outcomes that require remeasurement.

## Slide and recording plan

1. **Drift is a decision problem**.
2. **Data, model, evaluator, and concept drift**.
3. **Human feedback and sampled review**.
4. **Triggering recalibration or a new case slice**.
5. **Demo: compare baseline and changed distributions**.

## Speaker script

Drift means that the relationship between the system, its inputs, its users, or
the decision rule changes over time. Data drift changes the input distribution.
Model drift changes behavior. Evaluator drift changes the measurement process.
Concept drift changes what counts as a correct or acceptable outcome.

Do not choose a threshold because it sounds familiar. Define the signal, the
comparison window, the consequence, and the owner. A distribution change may
trigger sampling and review rather than an automatic rollback.

Human feedback is part of the measurement loop. Sample normal and high-risk
cases, compare evaluator decisions with calibrated human labels, and inspect
new failure categories. If the evaluator is no longer aligned with the
decision, the result is measurement drift even if the score looks stable.

## Demo notes

- Use synthetic baseline and changed-case counts.
- Show a recalibration trigger without claiming a live production trend.

## Learner practice

Define one drift signal, baseline window, review threshold, owner, and action.
State whether the action is sample, recalibrate, hold, or rollback.

## What this lesson does not prove

A synthetic distribution comparison does not establish that a deployed monitor
will detect real-world drift or that the chosen threshold is statistically
adequate.
