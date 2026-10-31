# Lesson 10: Deterministic Checks

Module: 3 — Automated Evaluators
Suggested runtime: 10–12 minutes
Primary lab: Add deterministic gates to the semantic-outcomes workflow

## Learner objective

By the end of this lesson, you can identify evaluation questions that should be answered by deterministic checks, meaning repeatable rules with the same result for the same evidence.

## Slide and recording plan

1. **What deterministic means** — fixed input and evidence produce a repeatable result.
2. **Good candidates** — schema, required fields, authorization, state transitions, latency, cost, and stop conditions.
3. **Hard gate versus diagnostic signal** — which failures block and which inform.
4. **Demo: inspect the harness controls** — show missing evidence and terminal-state checks.
5. **Practice: classify five checks**.

## Speaker script

A deterministic check is a repeatable rule that produces the same result when the relevant input and evidence are the same. It is the right tool when the question has an objective contract: is a required field present, is the tool authorized, did the workflow reach a terminal state, or did the request stay within a budget?

Deterministic checks are valuable because they are fast, explainable, and easy to rerun. They also create a stable foundation for more subjective evaluation. If a response is malformed, missing required evidence, or outside an authorization boundary, we should not ask a model-based judge to decide whether the output is acceptable. The basic contract is already broken.

Separate hard gates from diagnostic signals. A hard gate is a failure that blocks the decision, such as an unauthorized action or a missing required evidence field. A diagnostic signal helps us understand quality but may not block by itself, such as latency variation or a style preference. The choice depends on risk, and it should be written down rather than hidden in code.

In the harness, inspect how transport status, finding status, semantic outcome, missing evidence, retry count, and human approval are reported separately. That separation prevents a successful request from being mistaken for a successful evaluation. The control is useful because the failure remains visible even when the outer process completes normally.

Do not add deterministic checks simply to make the dashboard greener. A check is useful when it measures a requirement that would change the decision. The cost of choosing the wrong check is false assurance: the system passes a precise test while the actual risk remains unmeasured.

## Demo notes

- Run `labs/01-semantic-outcomes/run_lab.py`.
- Point out that both paths can transport successfully while their semantic outcomes differ.
- Inspect the structured summary and identify which fields are hard evidence.
- Recording boundary: do not imply that deterministic checks cover quality, factuality, or helpfulness by themselves.

## Learner practice

Classify these checks as hard gate, diagnostic signal, or not yet defined:

1. required evidence is present,
2. response is under a latency target,
3. response sounds professional,
4. tool call is authorized,
5. agent stopped after the required terminal state.

For each hard gate, write the exact failure consequence.

## What this lesson does not prove

Deterministic checks cannot judge every meaningful property. A workflow can satisfy its schema and authorization rules while still being factually wrong, unsafe, or unhelpful.
