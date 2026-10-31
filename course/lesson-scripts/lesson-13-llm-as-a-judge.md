# Lesson 13: LLM-as-a-Judge

Module: 3 — Automated Evaluators
Suggested runtime: 10–12 minutes
Primary lab: Build a structured judge input and compare it with a rubric

## Learner objective

By the end of this lesson, you can describe the inputs and controls needed for an LLM-as-a-judge evaluator, meaning a language model that scores another model’s output against stated criteria.

## Slide and recording plan

1. **The judge contract** — task, response, criteria, evidence, and output schema.
2. **A judge is an evaluator, not an oracle** — it can be wrong and biased.
3. **Score plus brief justification** — structured evidence, not hidden reasoning.
4. **Demo: judge a supported and unsupported answer**.
5. **Practice: write a binary judge prompt**.

## Speaker script

An LLM-as-a-judge evaluator uses one language model to assess another output against explicit criteria. The judge input should identify the task, the response being evaluated, the relevant evidence, and the scoring rule. If the judge receives only the answer and a vague instruction to “rate quality,” the result is difficult to interpret and easy to steer accidentally.

Treat the judge as a measurement component with failure modes. It can miss a subtle factual error, reward fluent wording, follow an instruction inside the evaluated answer, or apply a criterion inconsistently. The judge’s output must therefore be checked, calibrated, and compared with independent evidence.

Ask for a structured decision and a brief justification tied to the rubric. A brief justification is an auditable explanation of which criterion was met or failed; it is not a request for hidden chain-of-thought or private internal reasoning. The evaluator should expose the evidence needed to review the decision, not an unrestricted stream of internal deliberation.

Prefer criteria that can be answered directly. Binary checks are often easier to calibrate than vague five-point quality scores. When a graded score is needed, define each level with observable boundaries and preserve the per-criterion results so the aggregate does not hide a blocking failure.

In the demo, give the judge one supported answer and one answer with a missing evidence item. Then compare the judge result with a deterministic evidence check. If the judge passes an unsupported answer, the result is a finding about the evaluator, not proof that the answer is acceptable.

The cost of treating a judge as an oracle is that the evaluation can become self-confirming. A fluent model judges a fluent model, the dashboard reports a number, and no independent control is present to expose the miss.

## Demo notes

- Use synthetic task, answer, evidence, criteria, and expected JSON.
- Show the raw judge output, parsed output, and independent evidence check separately.
- Include a malformed-output example as a transport or schema finding.
- Recording boundary: do not claim that a judge rationale is a proof of correctness.

## Learner practice

Write a binary judge contract for:

“Pass only if the response identifies the missing evidence and does not claim the task is complete.”

Specify the input fields, output fields, pass condition, and the independent check that would challenge the judge.

## What this lesson does not prove

A well-structured judge prompt does not guarantee accurate judgments. It improves inspectability and repeatability, but calibration and independent controls remain necessary.
