# Lesson 9: Human-Rating Cost and Agreement Sessions

Module: 2 — Human Evaluation and Test Design
Suggested runtime: 10–12 minutes
Primary lab: Design a small human-review plan

## Learner objective

By the end of this lesson, you can design a human-review plan that balances cost, speed, and confidence without pretending that automation has removed the need for judgment.

## Slide and recording plan

1. **Why human review is still needed** — context, harm, ambiguity, and new failure modes.
2. **The cost model** — reviewer time, calibration time, adjudication, and rework.
3. **A staged review plan** — calibrate, sample risk, automate stable checks, escalate uncertainty.
4. **Demo: estimate a review budget** — compare full review with risk-based sampling.
5. **Practice: write the escalation rule**.

## Speaker script

Human review is expensive because it consumes attention, context, and coordination. A realistic plan includes the time to train reviewers, score cases, discuss disagreements, adjudicate difficult cases, and update the rubric when the task changes.

That cost does not mean human review should be removed. Human judgment is often the reference process for ambiguous quality, safety, factuality, and harm-related decisions. The useful question is how to spend that judgment where it changes the decision most.

Use a staged plan. Begin with a calibration session on representative and high-risk cases. Automate stable checks that are objective, such as required fields, schema validity, tool authorization, or a known stop condition. Route uncertain, high-impact, or novel cases to human review. Sample normal cases enough to detect drift, but do not spend the same review budget on every case when the risks are different.

Agreement sessions are not only a quality-control step. They are a discovery mechanism. Disagreements often reveal missing criteria, confusing evidence, or a new failure mode. Capture the resolution and the reason so the rubric can be updated without relying on memory.

Make the escalation rule explicit. For example: “If a case is high risk, evidence is conflicting, or the reviewer cannot apply the rubric without an unstated assumption, the case requires adjudication.” This rule makes the review boundary visible. Without it, reviewers quietly resolve difficult cases differently, and the final score mixes measurement with personal judgment.

In the demo, compare full review with risk-based review. Include calibration and adjudication in both estimates. The cheapest plan is not automatically the best plan; a plan that misses a release-blocking failure is more expensive than the review time it saved.

## Demo notes

- Use a synthetic estimate such as cases × minutes per case plus calibration and adjudication.
- Show how a smaller high-risk sample can be more informative than a uniform sample.
- Mark all cost figures as illustrative.
- Recording boundary: do not present the example budget as a forecast for a real organization.

## Learner practice

Design a review plan for 100 cases:

- 20 high-risk cases,
- 60 normal cases,
- 20 novel or ambiguous cases.

Specify how many cases receive automated checks, human review, and adjudication. State the rule that moves a case from one tier to another and the consequence if the plan under-samples a risk.

## What this lesson does not prove

Risk-based sampling improves focus, but it can miss an unrecognized risk category. Keep a mechanism for discovering new failures and periodically review whether the sampling policy still matches the product.
