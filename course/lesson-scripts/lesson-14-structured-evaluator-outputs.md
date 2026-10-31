# Lesson 14: Structured Evaluator Outputs

Module: 3 — Automated Evaluators
Suggested runtime: 10–12 minutes
Primary lab: Separate parseability from evaluator validity

## Learner objective

By the end of this lesson, you can distinguish a parseable evaluator response from a valid evaluation decision.

## Slide and recording plan

1. **Structure is a contract** — required fields, types, and allowed values.
2. **Three separate questions** — did the response arrive, parse, and make sense?
3. **Malformed versus wrong** — different findings and different fixes.
4. **Demo: valid JSON with an invalid judgment**.
5. **Practice: design a schema and an independent validator**.

## Speaker script

A structured evaluator output is a response in a defined format, such as JSON with a decision, score, reason code, and evidence references. Structure makes the result easier to parse, compare, store, and audit.

Structure is not validity. A response can be valid JSON with the wrong decision. It can also contain the right decision in malformed JSON that downstream code cannot safely consume. Keep these findings separate:

- transport failure: the evaluator did not return usable content;
- schema failure: the content cannot be parsed or violates the required shape;
- semantic failure: the content parses but the decision is wrong or unsupported.

This separation prevents a formatting fix from being mistaken for a quality fix. It also makes the failure owner clearer. A schema failure may need a parser or prompt change. A semantic failure may need better criteria, evidence, model choice, or human review.

Define allowed values and required relationships. If `decision` is `fail`, require at least one `failure_code`. If `decision` is `pass`, require the evidence references that justify the pass. A schema can express some of these rules, while a second validator checks the cross-field meaning.

In the demo, show a well-formed output that marks an unsupported answer as pass. The parser succeeds, but the independent evidence check fails. Then show malformed output that never reaches semantic evaluation. Two different problems are visible because the pipeline preserves the stages.

The cost of collapsing these stages is misleading operations data. A dashboard may show “evaluator completed” when all that happened was that a JSON parser accepted the response.

## Demo notes

- Use a small JSON schema with `decision`, `reason_code`, `evidence_ids`, and `confidence`.
- Validate field types and allowed values first.
- Run a semantic cross-check against the synthetic evidence.
- Recording boundary: keep confidence as an informational field unless a threshold has been validated.

## Learner practice

Design an evaluator schema with:

1. one required decision field,
2. two allowed decision values,
3. one required reason code,
4. evidence references,
5. one rule that the schema alone cannot prove.

Describe how the independent validator checks the fifth requirement.

## What this lesson does not prove

Structured output improves operational reliability; it does not make the evaluator correct. Parseability is necessary for a dependable pipeline, not sufficient for a trustworthy decision.
