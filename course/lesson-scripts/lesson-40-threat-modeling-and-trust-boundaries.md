# Lesson 40: Threat Modeling and Trust Boundaries

Module: 10 — Security and assurance controls
Suggested runtime: 12–15 minutes
Primary lab: Lab 7 — Test the agent security boundary

## Learner objective

By the end of this lesson, you can draw the trust boundaries around an agent
workflow and turn the highest-cost abuse paths into evaluation cases.

## Slide and recording plan

1. **Threat model** — identify assets, actors, entry points, and consequences.
2. **Trust boundary** — show where authority or data ownership changes.
3. **Abuse path** — connect untrusted input to a possible tool or data effect.
4. **Control map** — place prevention, detection, and response controls.
5. **Demo: inspect Lab 7 security cases**.

## Speaker script

A threat model is a structured description of what could go wrong, who could
cause it, what the system could expose or change, and which controls should
prevent or detect it. It is not a prediction of every attack. It is a way to
make the expensive paths visible before choosing tests.

Start with assets: credentials, customer data, state-changing tools, model
instructions, evaluation evidence, and service availability. Then identify
actors and entry points: users, retrieved documents, tool results, plugins,
network endpoints, and operators.

A trust boundary is the point where the authority, data sensitivity, or
ownership changes. A retrieved document is not trusted merely because the
agent can read it. A tool result is not an instruction merely because it came
from a registered tool. The evaluation should record that boundary explicitly.

For each high-cost path, name a preventive control, a detection signal, and a
response action. If an untrusted field can cause an unauthorized write, the
control is not only “the model should resist.” It may also include tool
authorization, argument validation, approval, audit evidence, and rollback.

## Demo notes

- Run Lab 7 and inspect the trust-boundary findings.
- Keep examples synthetic and harmless.
- Recording boundary: do not demonstrate live exploitation or real credentials.

## Learner practice

Draw one workflow with four labels: asset, untrusted input, trust boundary, and
state-changing action. Add one preventive, detective, and response control.

## What this lesson does not prove

A threat model does not prove that an implementation enforces every control. It
identifies what must be tested and who needs to own the evidence.
