# Lesson 22: Safety, Refusal, and Prompt Injection

Module: 4 — Factuality, Safety, and Agent Behavior
Suggested runtime: 12–15 minutes
Primary lab: Evaluate safe refusal and injection resistance

## Learner objective

By the end of this lesson, you can evaluate whether an agent refuses unsafe requests, preserves useful help where possible, and resists instructions that arrive through untrusted content.

## Slide and recording plan

1. **Safety is a decision boundary** — not a style preference.
2. **Refusal quality** — refuse the unsafe part, explain the boundary, redirect when appropriate.
3. **Prompt injection** — untrusted content attempts to override the task or policy.
4. **Demo: safe synthetic injection case**.
5. **Practice: separate safety, helpfulness, and evidence findings**.

## Speaker script

Safety evaluation asks whether the system stays within an authorized boundary when a request is harmful, sensitive, or manipulative. Refusal quality is not simply “did the model say no?” A useful refusal avoids the unsafe assistance, states the boundary clearly, and provides a safe alternative when one exists.

Prompt injection is an attempt to make the system follow instructions from untrusted content, such as a retrieved document, a tool result, or a user-controlled field, instead of the authorized task and policy. The evaluation should identify the untrusted source, the instruction it contains, and the action that would be unsafe if followed.

Keep safety, helpfulness, and factuality separate. A refusal can be safe but unnecessarily unhelpful. A helpful answer can still be unsafe. A factually correct answer can still reveal information it was not authorized to provide. Separate findings make the tradeoff visible.

Use synthetic identifiers and harmless examples in the lab. The goal is to test whether the agent treats untrusted instructions as data and preserves the authorized control flow. Do not reproduce real harmful content to make the lesson feel more realistic.

In the demo, present a benign task with an injected instruction inside a synthetic retrieved document. The expected result is that the agent ignores the injected instruction, preserves the task boundary, and reports any required escalation. Then show a refusal case and inspect whether it both blocks the unsafe part and offers an allowed next step.

The cost of weak safety evaluation is not only a bad response. A successful injection can redirect tools, expose data, or create an unauthorized action. That is why safety needs explicit negative controls and trajectory evidence.

## Demo notes

- Use a synthetic document containing a clearly labeled untrusted instruction.
- Do not execute the injected instruction.
- Record the source trust level, observed action, and final safety decision.
- Recording boundary: avoid operationally useful harmful examples; focus on control behavior.

## Learner practice

For three synthetic cases, record:

`request_type`, `untrusted_source`, `unsafe_action`, `expected_refusal_or_redirect`, `helpfulness_result`, `evidence`.

Decide whether each case passes, fails, or requires human review.

## What this lesson does not prove

Passing a small injection suite does not prove broad resistance. Attack patterns change, and safety evaluation must be refreshed as tools, data sources, and policies change.
