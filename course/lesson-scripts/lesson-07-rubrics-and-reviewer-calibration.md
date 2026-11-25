# Lesson 7: Rubrics and Reviewer Calibration

Module: 2 — Human Evaluation and Test Design
Suggested runtime: 10–12 minutes
Primary lab: Write and calibrate a one-dimension rubric

## Learner objective

By the end of this lesson, you can write a rubric with observable criteria, acceptable outcomes, and fail conditions, then use a calibration session to find disagreements before collecting a larger rating set.

## Slide and recording plan

1. **A rubric is an operating definition** — what reviewers check and what counts as failure.
2. **Weak versus strong criteria** — “good answer” compared with observable evidence.
3. **Rubric validity audit** — check that the scoring rule represents the decision before trusting its score.
4. **Calibration loop** — score, compare, discuss the rule, revise, repeat.
5. **Demo: score synthetic cases** — show why a criterion needs a boundary and why a missing criterion can hide a failure.
6. **Practice: write one binary and one graded criterion**.

## Speaker script

A rubric is an explicit scoring rule that tells a reviewer what to look for. It turns a vague question such as “is this response good?” into observable checks such as “does the response identify the required constraint, avoid an unsupported claim, and escalate when evidence is incomplete?”

Strong criteria describe behavior that another reviewer can inspect. They define the unit being judged, the evidence that supports a pass, the evidence that causes a fail, and what to do when the case is ambiguous. Weak criteria use broad adjectives such as helpful, professional, or high quality without explaining how to apply them. Those words can still be useful, but only after they are translated into observable behavior.

Binary criteria are often useful for safety boundaries, required fields, authorization, and evidence support. Graded criteria are useful when quality has meaningful levels, such as completeness or clarity. Do not use a five-point scale merely because it looks more sophisticated. If reviewers cannot distinguish the levels, the extra numbers create noise and false precision.

Calibration is a short agreement session before the full rating pass. Reviewers independently score a shared set, compare disagreements, and revise the rubric when the disagreement exposes an unclear rule. Calibration is not a vote that makes the majority automatically correct. The purpose is to improve the measurement definition and document the judgment that remains.

Keep criteria separate when they answer different questions. A response can be factually supported but unsafe, or safe but incomplete. Combining those dimensions into one score makes it harder to see what needs fixing and allows a strong dimension to hide a blocking failure.

Before expanding a benchmark or trusting an aggregate score, run a **rubric validity audit**. This asks whether the rubric represents the decision at all, not only whether reviewers can apply it consistently. Look for missing criteria, criteria that measure a different construct than the decision, verification rules without evidence, duplicate or bundled criteria, and vague wording. A rubric can be consistently applied and still miss the requirement that matters most.

In the demo, score the synthetic cases, including one where the answer passes the current rubric because it is complete and supported but still misses a critical actionability requirement. The aggregate score passes; the rubric-validity audit blocks the decision because the requirement is not represented. Then add the criterion or explicitly document why it is out of scope. The cost of skipping this audit is a precise score for the wrong question.

## Demo notes

- Use the synthetic evidence-support cases from the course repo.
- Show a rubric row with `criterion`, `pass_when`, `fail_when`, and `ambiguous_when`.
- Keep the final score separate from the short reason for the score.
- Show a rubric-validity audit with missing-criterion, misalignment, evidence,
  overlap, bundling, and vagueness checks.
- Recording boundary: do not present calibration labels as universal truth; they are course examples.

## Learner practice

Write a rubric for “the agent should not claim completion without completion evidence.” Include:

1. one binary criterion,
2. one acceptable example,
3. one failure example,
4. one ambiguous case,
5. the rule for resolving the ambiguous case.

Have a second reviewer score three cases and compare the disagreements.

Then audit the rubric against the decision: name one requirement that must block
the decision, identify where the rubric represents it, and record what happens
when the requirement is absent. Do not repair a missing criterion by increasing
the weight of an unrelated one.

## What this lesson does not prove

A clear rubric improves consistency; it does not prove that the rubric measures
the right construct. A passing aggregate can still be misleading when a
decision-relevant requirement is absent, bundled, or verified without evidence.
Some tasks require human review because context, harm, or domain meaning cannot
be reduced safely to a single rule.
