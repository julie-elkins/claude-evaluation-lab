# Lesson 12: Why Reference Metrics Miss Valid Variation

Module: 3 — Automated Evaluators
Suggested runtime: 10–12 minutes
Primary lab: Find valid paraphrases and invalid high-overlap answers

## Learner objective

By the end of this lesson, you can recognize when a reference metric is insensitive to valid variation or overly tolerant of a misleading response.

## Slide and recording plan

1. **One reference is not the meaning** — valid answers can use different wording.
2. **False negatives** — correct paraphrases score lower.
3. **False positives** — copied words can hide unsupported meaning.
4. **Demo: three answers, two evaluation layers**.
5. **Practice: add a semantic and evidence check**.

## Speaker script

Reference metrics compare text, not the full meaning of the task. That creates two common errors. A valid paraphrase can receive a lower score because it uses different words. A misleading response can receive a higher score because it repeats words from the reference without satisfying the underlying requirement.

This is not an argument that reference metrics are useless. It is an argument for matching the metric to the decision. When wording is constrained, lexical overlap can be direct evidence. When the task allows variation, we need an additional check for meaning, support, or task completion.

A practical evaluation can separate three questions: did the answer use the required format, did it address the required meaning, and is the meaning supported by evidence? A reference score can help with the first question. It should not silently stand in for the other two.

Semantic evaluation means judging meaning rather than exact wording. It may use a rubric, a trained reviewer, or a language-model judge. It still needs criteria and evidence. Calling a judge “semantic” does not make it reliable automatically.

In the demo, compare three synthetic answers: an exact reference match, a valid paraphrase, and a response that copies phrases but makes an unsupported claim. The lesson is visible when the text score and the decision diverge. Investigate the divergence instead of forcing the semantic decision to follow the overlap score.

The cost of ignoring valid variation is that a system is trained toward one phrasing rather than the user’s goal. The cost of ignoring false positives is more serious: a polished answer can pass while making a decision the evidence does not support.

## Demo notes

- Keep the examples short and synthetic.
- Show the reference metric beside a rubric result and evidence-support result.
- Label disagreement as a measurement question, not as a metric bug.
- Recording boundary: do not claim that a model judge is automatically more accurate than a reference metric.

## Learner practice

Write three answers to one synthetic prompt:

1. exact reference wording,
2. valid paraphrase,
3. high-overlap answer with one unsupported claim.

For each answer, record the lexical result, semantic result, evidence result, and final decision.

## What this lesson does not prove

Semantic checks reduce one limitation of lexical overlap, but they introduce their own risks: judge bias, inconsistent prompts, and difficulty reproducing a human judgment.
