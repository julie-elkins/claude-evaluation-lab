# Lesson 15: Pointwise and Pairwise Judging

Module: 3 — Automated Evaluators
Suggested runtime: 10–12 minutes
Primary lab: Choose a judging design for a comparison task

## Learner objective

By the end of this lesson, you can distinguish pointwise judging, which scores one answer against criteria, from pairwise judging, which chooses between two answers.

## Slide and recording plan

1. **Pointwise judging** — one response, one rubric, one decision.
2. **Pairwise judging** — two responses, one preference.
3. **When the designs answer different questions**.
4. **Demo: compare two candidate answers**.
5. **Practice: select the design and record its limitation**.

## Speaker script

Pointwise judging evaluates one response against a rubric. It works well when the question is whether an answer meets an absolute requirement: did it include the required evidence, avoid an unauthorized action, or follow the requested format?

Pairwise judging compares two responses and asks which is better for the stated criterion. It is useful for model or prompt comparisons when a direct preference is easier to express than an absolute score. The output is relative: answer A is preferred to answer B under this criterion and this context.

The two designs are not interchangeable. A pairwise winner may still fail an absolute safety or evidence requirement. Conversely, a pointwise score can tell us that both answers pass, but not which is more useful when choosing between variants. Preserve the absolute checks even when pairwise preference is convenient.

Position matters in pairwise judging. If the same two answers are shown in the opposite order, a preference change is a signal of position bias. Randomize or counterbalance order, record the order, and inspect whether the result changes.

In the demo, compare two synthetic answers: one concise and supported, one more detailed but containing an unsupported claim. Ask the pairwise judge which is better for usefulness, then run a pointwise evidence check. This shows why “preferred” and “acceptable” are separate decisions.

The cost of using pairwise results as a release gate is that a winner can be the least bad option. The system may improve relative to a baseline while still failing the requirement users depend on.

## Demo notes

- Use the same task and evidence for both candidate answers.
- Run the pairwise comparison in both orders if a judge is available.
- Preserve the pointwise evidence and safety results.
- Recording boundary: do not treat a pairwise preference as a universal quality ranking.

## Learner practice

For each question, choose pointwise, pairwise, or both:

1. Does the response contain required evidence?
2. Which prompt version is more useful?
3. Is the tool call authorized?
4. Which answer is clearer while both remain factually supported?

State the failure that would be invisible if you used only your chosen design.

## What this lesson does not prove

Pairwise judging can improve sensitivity to relative differences, but it remains vulnerable to position, verbosity, and judge-preference bias.
