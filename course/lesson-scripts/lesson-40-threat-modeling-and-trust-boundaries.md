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
4. **Red-team loop** — attack hypothesis, bounded test, evidence, and regression case.
5. **Control map** — place prevention, detection, and response controls.
6. **Demo: inspect Lab 7 security cases**.

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

Red teaming is adversarial evaluation: deliberately testing how an agent
behaves under hostile, manipulative, or boundary-seeking conditions. A useful
red-team exercise is not a collection of dramatic prompts. It is a bounded
workflow:

1. state the rules of engagement, allowed environment, and stop conditions;
2. choose an attack hypothesis and entry point;
3. run a harmless synthetic case against the declared control;
4. preserve the observed path, impact, and missing or effective control; and
5. turn a confirmed weakness into a regression case with an owner and release
   consequence.

Use attack categories to make coverage visible: indirect prompt injection,
jailbreak or refusal bypass, tool misuse, data exfiltration, privilege
escalation, unsafe side effect, resource exhaustion, and supply-chain or
dependency drift. The category is not the finding by itself. The finding must
say what happened, what evidence proves it, and what decision changes.

For each high-cost path, name a preventive control, a detection signal, and a
response action. If an untrusted field can cause an unauthorized write, the
control is not only “the model should resist.” It may also include tool
authorization, argument validation, approval, audit evidence, and rollback.

The red-team loop should end in engineering work. A successful attack becomes
a minimized regression case; a blocked attack becomes evidence that the
declared control was exercised; an ambiguous result becomes a human-review
case. Re-run the regression after model, prompt, skill, tool, policy, or
architecture changes. Do not report the number of attempted attacks as a
universal safety score.

## Demo notes

- Run Lab 7 and inspect the trust-boundary findings.
- Filter the report to `red_team_cases` and trace one attack hypothesis to its
  expected control and regression case.
- Show one blocked attack and one planted control failure; distinguish “the
  attack was detected” from “the deployed system is secure.”
- Keep examples synthetic and harmless.
- Recording boundary: do not demonstrate live exploitation or real credentials.

## Learner practice

Draw one workflow with four labels: asset, untrusted input, trust boundary, and
state-changing action. Add one preventive, detective, and response control.
Then complete a red-team record:

1. The attack hypothesis is…
2. The entry point is…
3. The expected control is…
4. The evidence of detection or failure is…
5. The regression case and release consequence are…

## What this lesson does not prove

A threat model and a red-team run do not prove that an implementation enforces
every control. They identify what was tested, what evidence was observed, and
who needs to own the next action. Passing a synthetic attack case does not
prove resistance to new attack patterns.
