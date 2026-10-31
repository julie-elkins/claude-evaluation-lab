# Lesson 21: Weighted Factuality and Partial Error

Module: 4 — Factuality, Safety, and Agent Behavior
Suggested runtime: 10–12 minutes
Primary lab: Compare unweighted and risk-weighted aggregation

## Learner objective

By the end of this lesson, you can aggregate claim-level factuality without allowing many low-risk claims to hide one high-risk error.

## Slide and recording plan

1. **Why averages can mislead** — one answer, several claims, unequal consequences.
2. **Weights and blocking claims** — risk is part of the decision.
3. **Partial error** — useful for diagnosis, not permission to ignore critical failures.
4. **Demo: same claims, different risk policy**.
5. **Practice: write the aggregate decision rule**.

## Speaker script

An answer-level factuality score often aggregates several claim-level results. A simple average treats every claim as equally important. That is easy to compute, but it can hide a critical error among many harmless statements.

Risk-weighted aggregation gives higher weight to claims whose failure has greater consequence. Another option is a blocking rule: any unsupported claim in a protected category fails the evaluation, while low-risk unsupported claims trigger review or reduce the diagnostic score.

Weights are a policy choice, not a fact discovered by the model. Document what the weights mean, who owns them, and when they are reviewed. Do not use weights to make an inconvenient failure disappear. If a high-risk claim is wrong, the decision should remain visible even when the overall score is high.

Partial error is still useful. It tells us how much of the answer was supported and which claims caused the problem. Use it for diagnosis, prioritization, and trend analysis. Do not let “mostly correct” become an automatic approval rule when the remaining error can change a user action.

In the demo, create two answers with the same number of unsupported claims but different risk profiles. Compare an unweighted average, a weighted score, and a blocking rule. The right policy depends on the decision, but the risk difference should never be hidden by a single average.

The cost of a poor aggregation rule is asymmetric. It can approve a response that is broadly plausible but wrong at the exact point where a user needs reliable guidance.

## Demo notes

- Use three synthetic claims with low, medium, and high risk.
- Show the per-claim table beside all aggregate views.
- Make the blocking rule explicit before running the example.
- Recording boundary: do not present illustrative weights as a universal formula.

## Learner practice

Define an aggregation policy for five claims:

- two low-risk,
- two medium-risk,
- one high-risk.

Specify the weights, the blocking conditions, and the escalation condition. Test the policy against an answer with one unsupported high-risk claim.

## What this lesson does not prove

Weighted scores still depend on judgment about risk. They make the policy explicit; they do not make the policy objectively correct.
