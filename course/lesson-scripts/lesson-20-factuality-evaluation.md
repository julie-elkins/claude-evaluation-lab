# Lesson 20: Factuality Evaluation

Module: 4 — Factuality, Safety, and Agent Behavior
Suggested runtime: 12–15 minutes
Primary lab: Run a supported-versus-unsupported factuality check

## Learner objective

By the end of this lesson, you can design a factuality check that distinguishes supported, unsupported, contradicted, and unresolved claims.

## Slide and recording plan

1. **Factuality is evidence matching** — not fluency or confidence.
2. **The claim lifecycle** — extract, retrieve, compare, classify, decide.
3. **Evidence retrieval methods** — provided context, RAG, or web lookup.
4. **Demo: evaluate a synthetic response**.
5. **Practice: define the abstention path**.

## Speaker script

Factuality means that a claim is true or supported in the context of the decision. In this course, we evaluate it by linking claims to evidence rather than by trusting how confident or polished the answer sounds.

A factuality workflow has five steps: extract claims, gather the relevant evidence, compare each claim with that evidence, classify the result, and apply the decision rule. Retrieval-augmented generation, or RAG, means retrieving supporting context before generating an answer. RAG can improve access to evidence, but retrieval itself does not prove that the answer used the evidence correctly.

Use an explicit unresolved state. If evidence is missing, stale, conflicting, or outside the allowed source set, the evaluator should not force a pass or fail merely to complete the report. The correct outcome may be abstention, escalation, or a request for more evidence.

Separate evidence support from answer completeness. An answer can be factually supported but omit a required constraint. It can be complete in format but contain an unsupported claim. Each dimension should have its own finding and decision consequence.

In the demo, evaluate three synthetic claims against a small evidence pack. Show how the same workflow handles support, contradiction, and missing evidence. Then run the result through the course evidence contract so the final report carries the source IDs and terminal state.

The cost of treating factuality as a single confidence score is that uncertainty disappears. A high-confidence unsupported claim is still unsupported, and a low-confidence supported claim may only need clearer evidence presentation.

## Demo notes

- Use the public synthetic content-assurance examples or course-owned evidence.
- Show evidence IDs in every claim result.
- Keep live web retrieval out of the base lab unless the recording environment is controlled.
- Recording boundary: do not imply that a retrieved document is authoritative without checking its source and scope.

## Learner practice

Define the decision policy for:

1. all claims supported,
2. one unsupported low-risk claim,
3. one contradicted high-risk claim,
4. missing evidence,
5. conflicting evidence.

Specify pass, fail, or escalation for each and explain the cost of getting the policy wrong.

## What this lesson does not prove

Factuality evaluation is limited by the evidence set. If the evidence is incomplete, stale, or wrong, the evaluator can produce a confident but incorrect support judgment.
