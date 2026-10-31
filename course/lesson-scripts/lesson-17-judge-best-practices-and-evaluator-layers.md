# Lesson 17: Judge Best Practices and Evaluator Layers

Module: 3 — Automated Evaluators
Suggested runtime: 12–15 minutes
Primary lab: Assemble a layered evaluator

## Learner objective

By the end of this lesson, you can combine deterministic checks, semantic judges, human review, and agent-level checks without allowing one layer to hide another layer’s failure.

## Slide and recording plan

1. **A layered evaluator** — different checks answer different questions.
2. **Judge best practices** — crisp criteria, evidence, reproducibility, and calibration.
3. **The independent layers** — contract, semantic, human, and trajectory.
4. **Demo: trace one case through the layers**.
5. **Practice: assign each criterion to its strongest layer**.

## Speaker script

A layered evaluator uses multiple kinds of evidence because no single evaluator sees every failure. Deterministic checks answer contract questions. A semantic judge can assess meaning against a rubric. Human review handles ambiguity and high-impact cases. Agent-level checks inspect the trajectory, meaning the sequence of observations, decisions, tool calls, and recovery steps that led to the final answer.

Good judge practice starts before the prompt is written. Define crisp criteria, provide the relevant evidence, use binary decisions where a boundary is genuinely binary, and keep the criteria separate from style preferences. Ask for a structured result with a short criterion-linked justification. Calibrate against trusted examples and check reproducibility across repeated runs.

Then add independent controls. A judge should not be the only component deciding whether its own output is valid. A deterministic evidence check can challenge a claimed pass. A human can review high-risk or ambiguous cases. A trajectory check can reveal that the final answer looks correct only because the agent used an unauthorized tool or skipped a required confirmation.

Keep failures attributable. If the schema is invalid, report a schema finding. If the schema is valid but the answer is unsupported, report a semantic finding. If the answer is supported but the agent violated an authorization rule, report a policy or trajectory finding. One aggregate score may be useful for a summary, but it should not replace the underlying findings.

In the demo, trace one synthetic case through the layers and stop when a release-blocking failure is found. The evaluation does not need to run every expensive layer after a decisive gate fails, but it should record what was skipped and why.

The cost of a single-layer evaluator is blind spots. The cost of a badly composed layered evaluator is duplicated work or contradictory results. The design goal is not “more checks”; it is independent evidence tied to the decision.

## Demo notes

- Use the current harness checklist and the evaluator-layer examples.
- Show contract, semantic, and agent-level findings as separate records.
- Mark which layer is authoritative for each criterion.
- Recording boundary: avoid presenting the layered design as a guarantee of safety.

## Learner practice

Assign the strongest evaluation layer to each criterion:

1. required JSON field,
2. evidence supports the answer,
3. action was authorized,
4. answer is useful for a novel case,
5. trajectory recovered after a tool failure.

Explain what independent layer would challenge each assignment.

## What this lesson does not prove

Layering reduces blind spots but does not eliminate them. The layers can share the same flawed data, assumptions, or model family, so independence must be considered explicitly.
