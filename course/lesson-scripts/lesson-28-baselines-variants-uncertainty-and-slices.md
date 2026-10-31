# Lesson 28: Baselines, Variants, Uncertainty, and Slices

Module: 5 — Benchmarks, Release, and Capstone
Suggested runtime: 12–15 minutes
Primary lab: Compare a baseline and a controlled variant

## Learner objective

By the end of this lesson, you can compare a baseline with a variant while preserving case alignment, uncertainty, and high-risk slices.

## Slide and recording plan

1. **Baseline versus variant** — change one meaningful factor at a time.
2. **Matched cases** — same inputs, evidence, and decision rules.
3. **Uncertainty** — repeated runs, confidence intervals, and unstable results.
4. **Slices** — inspect high-risk or boundary groups separately.
5. **Demo and practice: write a controlled comparison**.

## Speaker script

A baseline is the reference system or process against which a variant is compared. A variant is a changed model, prompt, tool policy, evaluator, or workflow. A useful comparison changes a defined factor and keeps the rest of the evaluation stable.

Use matched cases whenever possible. The baseline and variant should receive the same cases, evidence, instructions, and decision policy. If the case set changes at the same time as the system, we cannot tell what caused the result.

Uncertainty means the result could vary because of sampling, judge randomness, case mix, or run-to-run behavior. Repeated runs can reveal instability. Confidence intervals or other uncertainty summaries can communicate the likely range, but they do not fix biased sampling or a flawed evaluator.

Slices are subsets of cases grouped by a meaningful property, such as high-risk actions, missing context, long trajectories, or boundary conditions. An overall improvement can hide a regression in a high-risk slice. Report the slice result even when the aggregate is better.

In the demo, compare a baseline and variant on the same synthetic cases. Report overall outcomes, high-risk slice outcomes, failures caught by negative controls, and any change in cost or latency. The decision should not be based on a single average.

The cost of an uncontrolled comparison is an attribution error. We may ship a change because the score improved when the improvement actually came from easier cases, a changed evaluator, or random variation.

## Demo notes

- Use the harness controlled-variant comparison example.
- Show the pinned case set and evaluator configuration.
- Report both aggregate and slice results.
- Recording boundary: do not present illustrative uncertainty as statistical proof for a real deployment.

## Learner practice

Write a comparison plan for a baseline and one variant:

`change`, `held_constant`, `case_set`, `primary_metric`, `blocking_findings`, `high_risk_slices`, `repeat_count`, `decision_rule`.

Add one result pattern that would cause you to reject the variant despite an aggregate improvement.

## What this lesson does not prove

Matched comparisons improve attribution, but they do not prove generalization beyond the tested cases. Keep a held-out or newly sampled set for follow-up.
