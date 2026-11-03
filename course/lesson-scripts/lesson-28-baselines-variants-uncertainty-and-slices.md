# Lesson 28: Baselines, Variants, Uncertainty, and Slices

Module: 5 — Benchmarks, Release, and Capstone
Suggested runtime: 12–15 minutes
Primary lab: Compare a baseline and a controlled variant

## Learner objective

By the end of this lesson, you can compare a baseline with a variant while preserving case alignment, uncertainty, and high-risk slices.

## Slide and recording plan

1. **Baseline versus variant** — change one meaningful factor at a time.
2. **Matched cases** — same inputs, evidence, and decision rules.
3. **Uncertainty in plain numbers** — sample size, repeated runs, confidence intervals, and effect size.
4. **Slices** — inspect high-risk or boundary groups separately.
5. **Model upgrades and architecture changes** — re-test prompts, skills, tools, and subagents.
6. **Demo and practice: write a controlled comparison**.

## Speaker script

A baseline is the reference system or process against which a variant is compared. A variant is a changed model, prompt, tool policy, evaluator, or workflow. A useful comparison changes a defined factor and keeps the rest of the evaluation stable.

An architecture variant may be a flat agent, a primary agent with subagents, or
a primary agent using skills and tools instead of a separate agent. A **model
upgrade** is a change to the model revision that can alter reasoning, tool
calling, context use, cost, and the value of existing prompts or subagents.
Record these as explicit changes. Do not preserve old scaffolding merely because
it once improved an older model.

Use matched cases whenever possible. The baseline and variant should receive the same cases, evidence, instructions, and decision policy. If the case set changes at the same time as the system, we cannot tell what caused the result.

Uncertainty means the result could vary because of sampling, judge randomness, case mix, or run-to-run behavior. Repeated runs can reveal instability. Confidence intervals or other uncertainty summaries can communicate the likely range, but they do not fix biased sampling or a flawed evaluator.

For a simple comparison, report the number of cases, the baseline result, the
variant result, the change between them, and the uncertainty around the
estimate. A confidence interval is a range around an estimate, not a guarantee
that the true value is inside it. An effect size describes how much the result
changed; practical significance asks whether that change affects the decision.
For nondeterministic agents, repeat the same case and report how often the
desired outcome appears rather than treating one successful run as stable.

Slices are subsets of cases grouped by a meaningful property, such as high-risk actions, missing context, long trajectories, or boundary conditions. An overall improvement can hide a regression in a high-risk slice. Report the slice result even when the aggregate is better.

In the demo, compare a baseline and variant on the same synthetic cases. Report overall outcomes, high-risk slice outcomes, failures caught by negative controls, and any change in cost or latency. The decision should not be based on a single average.

For a model or architecture upgrade, use a two-stage check. First, use a
failure-point replay as a **diagnostic filter**, meaning a cheap rerun that
holds earlier history fixed and tests whether the proposed change affects the
known decision. Then run the promising change from the beginning on the full
matched case set. Replay can miss an earlier divergence, so it is not sufficient
validation by itself.

The cost of an uncontrolled comparison is an attribution error. We may ship a change because the score improved when the improvement actually came from easier cases, a changed evaluator, or random variation.

## Demo notes

- Use the harness controlled-variant comparison example.
- Show the pinned case set and evaluator configuration.
- Report both aggregate and slice results.
- Recording boundary: do not present illustrative uncertainty as statistical proof for a real deployment.

## Learner practice

Write a comparison plan for a baseline and one variant:

`change`, `held_constant`, `case_set`, `case_count`, `primary_metric`,
`baseline_result`, `variant_result`, `uncertainty_summary`, `effect_size`,
`blocking_findings`, `high_risk_slices`, `repeat_count`, `model_revision`,
`prompt_revision`, `skill_set`, `architecture`, `subagent_policy`,
`diagnostic_replay_result`, `full_validation_result`, `decision_rule`.

Add one result pattern that would cause you to reject the variant despite an aggregate improvement.

## What this lesson does not prove

Matched comparisons improve attribution, but they do not prove generalization beyond the tested cases. A replay result does not prove full-run safety, and a model upgrade that improves the aggregate score does not prove that every skill, prompt, subagent, or tool remains useful. Keep a held-out or newly sampled set for follow-up.
