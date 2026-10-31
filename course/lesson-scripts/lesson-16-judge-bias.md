# Lesson 16: Judge Bias

Module: 3 — Automated Evaluators
Suggested runtime: 10–12 minutes
Primary lab: Add bias probes to a judge comparison

## Learner objective

By the end of this lesson, you can identify position, verbosity, self-enhancement, and alignment bias in model-based judging and choose a control for each.

## Slide and recording plan

1. **Bias is a measurement failure** — the score changes for an irrelevant reason.
2. **Position bias** — first or second answer favored.
3. **Verbosity and self-enhancement bias** — longer or familiar answers favored.
4. **Alignment bias** — judge rewards agreement with its own preference.
5. **Demo and practice: run a bias probe**.

## Speaker script

Judge bias occurs when an evaluator’s decision changes because of a factor that should not matter to the rubric. A judge can prefer the first answer in a pair, reward a longer answer, favor an answer that resembles its own output, or reward agreement with a preferred style instead of checking the task requirement.

Position bias is tested by swapping the order of pairwise candidates. If the decision changes while the answers and criteria remain the same, the evaluation is unstable. Verbosity bias is tested by comparing answers with equivalent content at different lengths. Self-enhancement bias is tested by comparing a judge-produced answer with an independent answer of equal quality.

Alignment bias is broader: the judge may reward a response that agrees with its assumptions, tone, or preferred solution even when the rubric asks for evidence or correctness. The control is to anchor the decision to explicit criteria and evidence, not to a general impression.

Mitigations include blind labels, randomized order, concise criteria, binary checks where appropriate, repeated runs, and an independent breaker that targets likely false passes. Lowering randomness can improve repeatability, but it does not remove systematic bias. A stable biased judge is still biased.

In the demo, run one pairwise comparison in both orders and one pointwise comparison with a deliberately concise answer. Record the prompt, order, result, and observed bias. The purpose is not to prove the judge is unbiased from one probe. It is to make the risk measurable before relying on the score.

The cost of ignoring judge bias is especially high when the judge becomes the training signal. The system can be optimized toward the evaluator’s preference, causing the measured score to rise while the real requirement stays flat or gets worse.

## Demo notes

- Use synthetic answers that differ only in order or verbosity.
- Record the exact judge configuration for each run.
- Keep bias findings separate from answer-quality findings.
- Recording boundary: do not generalize a single probe into a claim about every model or task.

## Learner practice

Design one probe for each bias:

1. position,
2. verbosity,
3. self-enhancement,
4. alignment.

For each probe, name the irrelevant factor, the expected invariant, and the action if the result changes.

## What this lesson does not prove

No small probe suite can establish the absence of bias. It can expose known risks and justify stronger controls where the evaluation decision is consequential.
