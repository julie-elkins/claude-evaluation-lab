# Lesson 6: Golden, Calibration, and Held-Out Data

Module: 2 — Human Evaluation and Test Design
Suggested runtime: 10–12 minutes
Primary lab: Label a small case split without leaking the answer

## Learner objective

By the end of this lesson, you can distinguish golden cases, calibration cases, and held-out cases, and explain why using the same examples to tune and prove an evaluator creates overconfidence.

## Slide and recording plan

1. **Three jobs, three data roles** — golden, calibration, and held-out.
2. **The leakage problem** — tuning and proving on the same cases.
3. **A practical split** — small reviewed set, calibration set, and untouched decision set.
4. **Demo: label the split metadata** — show what reviewers may see at each stage.
5. **Practice: identify leakage** — repair a flawed evaluation plan.

## Speaker script

Evaluation data has different jobs, and the jobs should not be silently mixed. A golden case is a case with a trusted expected label or outcome. It anchors what “correct” means. A calibration case is used to help reviewers or an evaluator apply the rubric consistently. A held-out case is kept away from tuning and used later to estimate how the method performs on cases it did not see during adjustment.

These roles can overlap in a carefully governed process, but they should be named explicitly. The important question is not whether a case has a label. The question is what decision the case is allowed to influence.

Suppose we tune a judge prompt until it agrees with reviewers on a set of 100 examples, then report that same agreement as proof that the judge is reliable. The result may be accurate on those examples, but the measurement is optimistic because the judge was adjusted against the answer key. This is a form of leakage: information from the proving set influenced the method being proved.

The safer pattern is to create a small, high-quality reviewed set for rubric design and calibration, then preserve a held-out set that is not used to tune prompts, thresholds, or case-selection rules. When the held-out result is poor, we learn that the method needs work. We should not quietly move the difficult cases into calibration and keep reporting the old result.

Golden cases are valuable, but they are not magical. The label still needs a reason, evidence, and an owner. A disputed golden label should be resolved or marked ambiguous; it should not be treated as unquestionable truth simply because it is in a file called “golden.”

In the demo, inspect the metadata rather than only the scores. Ask which cases influenced the rubric, which influenced the evaluator, and which are being used for the release decision. The cost of mixing these roles is a report that appears more precise than the evidence supports. That can delay the discovery of a bad evaluator until it is attached to a release.

## Demo notes

- Use a small synthetic table with `golden`, `calibration`, and `held_out` labels.
- Show an intentionally flawed split where the same case IDs appear in tuning and proof.
- Correct the metadata and rerun the comparison.
- Recording boundary: explain the concept with synthetic cases; do not expose unpublished evaluation sets.

## Learner practice

Take ten synthetic cases and assign them to:

- rubric design,
- reviewer calibration,
- held-out measurement.

Write one sentence explaining why each case is allowed to influence that stage. Identify any case that would create leakage if it appeared in both calibration and held-out sets.

## What this lesson does not prove

A held-out split reduces one important source of overconfidence, but it does not guarantee generalization. The held-out cases can still be unrepresentative, too easy, or too small to support a stable conclusion.
