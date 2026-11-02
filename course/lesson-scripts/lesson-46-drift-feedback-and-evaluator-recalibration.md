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
3. **Explicit and implicit feedback are signals, not automatic labels**.
4. **Human feedback and sampled review**.
5. **Triggering recalibration or a new case slice**.
6. **Demo: compare baseline and changed distributions**.

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

Feedback can also arrive indirectly. Explicit feedback means a rating,
comment, or human label. Implicit feedback means behavior such as a retry,
rephrased question, abandoned workflow, or repeated request. These signals can
help us find cases that deserve review, but none of them proves by itself that
the agent failed. A retry may mean the user is exploring. A missing rating may
mean the user was satisfied, busy, or unable to respond.

Before using feedback in an evaluation, record who generated it, how it was
sampled, what privacy boundary applies, and what alternative explanations
remain. Compare a sample of feedback-derived cases with calibrated human
review. Keep the original feedback signal separate from the evaluator label so
we can tell whether the problem is user experience, workflow behavior, or
measurement.

The full assurance loop is: establish an offline baseline, make a bounded
release, observe online signals, triage and review candidate failures, minimize
and sanitize the evidence, then add an appropriate regression or held-out case
before rerunning the offline evaluation. This loop turns monitoring into
learning without copying raw production content into a public dataset.

## Demo notes

- Use synthetic baseline and changed-case counts.
- Show a recalibration trigger without claiming a live production trend.
- Label one signal as explicit feedback and one as implicit feedback.
- Show why a feedback signal becomes a review candidate rather than an
  automatic pass/fail label.

## Learner practice

Define one drift signal, baseline window, review threshold, owner, and action.
State whether the action is sample, recalibrate, hold, or rollback.

Then complete the following for one feedback signal:

1. Is it explicit or implicit?
2. What behavior does it measure, and what does it not prove?
3. What sampling and privacy rule applies?
4. What alternative explanation could produce the same signal?
5. What human-review or evaluator check is required before it becomes a case?

## What this lesson does not prove

A synthetic distribution comparison does not establish that a deployed monitor
will detect real-world drift or that the chosen threshold is statistically
adequate. Synthetic feedback examples do not establish that live user behavior
is correctly labeled, representative, or safe to retain.
