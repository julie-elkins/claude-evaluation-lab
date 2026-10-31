# Lesson 11: METEOR, BLEU, and ROUGE

Module: 3 — Automated Evaluators
Suggested runtime: 10–12 minutes
Primary lab: Compare reference-based scores with an evidence-based decision

## Learner objective

By the end of this lesson, you can explain what reference-based metrics measure and choose when a lexical-overlap metric is appropriate.

## Slide and recording plan

1. **Reference-based evaluation** — compare a generated answer with one or more references.
2. **METEOR** — token alignment with stemming and synonym-aware matching.
3. **BLEU** — n-gram precision with a brevity penalty.
4. **ROUGE** — overlap-oriented recall and sequence matching.
5. **Practice: identify a safe and unsafe use of each metric**.

## Speaker script

Reference-based metrics compare a generated response with one or more reference texts. They are useful when overlap with a known answer is part of the requirement, such as controlled text generation, translation experiments, or regression checks on a stable format.

METEOR uses token alignment and can account for stemming and some synonym relationships. BLEU is based largely on n-gram precision and includes a brevity penalty. ROUGE family metrics emphasize overlap, often using recall-oriented or sequence-based comparisons. The important point is not to memorize the names. The important point is that each score measures a particular kind of similarity.

A score is evidence only for the property it measures. If the requirement is “use the approved wording in a fixed template,” lexical overlap may be useful. If the requirement is “give a correct answer using any clear wording,” overlap can punish a valid paraphrase. If the requirement is “do not invent an unsupported claim,” overlap is not the relevant test at all.

Use reference metrics as one layer in a measurement stack. Pair them with deterministic checks, human review, or semantic evaluation when meaning matters more than wording. Keep the reference source and scoring configuration versioned so a future score can be reproduced.

Avoid turning a metric into a universal quality score. A higher number is not automatically a better answer if the answer is more verbose, more copied, or more similar to a flawed reference. The cost of using the wrong metric is optimization in the wrong direction: the system learns to resemble the reference while missing the actual user requirement.

## Demo notes

- Use two synthetic answers: one with high word overlap and one valid paraphrase.
- Compare the metric result with a rubric that checks meaning and evidence.
- Do not report a course-wide score threshold; keep the example illustrative.
- Recording boundary: metric behavior may vary by tokenizer and implementation; show the exact configuration used.

## Learner practice

For each requirement, choose reference overlap, deterministic checking, human review, or a combination:

1. exact JSON field names,
2. approved translation wording,
3. factual support for a claim,
4. concise explanation in the learner’s own words,
5. required refusal language.

Explain why the selected method measures the requirement.

## What this lesson does not prove

METEOR, BLEU, and ROUGE do not provide a general measure of truth, safety, usefulness, or agent reliability. Their value depends on the task and the reference set.
