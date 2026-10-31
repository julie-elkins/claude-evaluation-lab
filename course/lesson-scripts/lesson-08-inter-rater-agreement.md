# Lesson 8: Inter-Rater Agreement

Module: 2 — Human Evaluation and Test Design
Suggested runtime: 10–12 minutes
Primary lab: Compare raw agreement with disagreement analysis

## Learner objective

By the end of this lesson, you can explain inter-rater agreement, meaning how consistently reviewers score the same cases, and distinguish raw agreement from chance-adjusted agreement.

## Slide and recording plan

1. **Agreement is a measurement property** — not proof that the rubric is true.
2. **Raw agreement** — the percentage of matching ratings.
3. **Chance-adjusted measures** — Cohen’s kappa, Fleiss’s kappa, and Krippendorff’s alpha.
4. **Demo: same agreement, different base rates** — why one number is insufficient.
5. **Practice: inspect disagreement categories and revise the rubric**.

## Speaker script

Inter-rater agreement means how consistently different reviewers score the same cases. It tells us about the repeatability of the rating process. It does not, by itself, tell us whether the rubric captures the product requirement.

The simplest measure is raw agreement: count the cases where reviewers gave the same rating and divide by the total. Raw agreement is easy to explain, but it can look high when one rating dominates. If nearly every case is marked pass, reviewers can agree often even when the rubric does not help them distinguish the difficult cases.

Chance-adjusted measures account for some agreement that could happen because of the reviewers’ rating distributions. Cohen’s kappa is commonly used for two raters and categorical labels. Fleiss’s kappa extends the idea to multiple raters. Krippendorff’s alpha supports several data types and can handle missing ratings more flexibly. The exact choice should follow the design of the rating task; it should not be chosen because one statistic produces the most flattering result.

Treat the statistic as a signal for investigation. When agreement is low, inspect the disagreements. Are reviewers using different definitions? Is the case genuinely ambiguous? Is the evidence incomplete? Is one reviewer missing context? Each cause leads to a different fix.

Also report the underlying counts and the rating distribution. A single agreement number hides whether the disagreement is concentrated in high-risk cases. A release process should be especially cautious when the cases with the lowest agreement are the cases that can approve an unsafe action or hide missing evidence.

In the demo, compare two synthetic rating tables with similar raw agreement but different class distributions. Then inspect the disagreement categories. The point is not to memorize a threshold. The point is to avoid treating an agreement statistic as a substitute for reviewing what the raters actually disagreed about.

## Demo notes

- Use synthetic binary ratings only.
- Show raw agreement first, then a chance-adjusted statistic with its assumptions stated.
- Include the contingency table or category counts beside the headline number.
- Recording boundary: avoid presenting any informal kappa threshold as a universal release rule.

## Learner practice

Given two reviewer columns, calculate:

1. raw agreement,
2. the rating distribution for each reviewer,
3. the disagreement count by case type.

Write one decision: proceed, recalibrate, or escalate for adjudication. Support the decision with the disagreement pattern, not only the statistic.

## What this lesson does not prove

High agreement does not prove correctness, fairness, or safety. Reviewers can consistently apply a flawed rubric, and a statistic can hide disagreements concentrated in the most consequential cases.
