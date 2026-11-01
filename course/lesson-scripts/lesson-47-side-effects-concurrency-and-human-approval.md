# Lesson 47: Side Effects, Concurrency, and Human Approval

Module: 11 — Continuous assurance and production implementation
Suggested runtime: 12–15 minutes
Primary lab: Lab 7 — Test the agent security boundary

## Learner objective

By the end of this lesson, you can evaluate duplicate actions, concurrent
updates, idempotency, compensation, and human approval gates.

## Slide and recording plan

1. **A correct plan can still create a bad side effect**.
2. **Idempotency** — safe repetition of the same request.
3. **Concurrency** — competing reads and writes.
4. **Compensation** — what reverses a partial action.
5. **Approval and escalation**.

## Speaker script

An agent can produce the right text and still create harm through a duplicate
write, stale state, or partial workflow. Evaluate the side effect separately
from the model response.

Idempotency means repeating the same request does not create an additional
unintended effect. Require a stable action key and inspect whether the tool
recognized a duplicate. For concurrent workflows, record the state version
read, the version written, and whether the update was accepted.

Not every action is reversible. A compensation path is the declared action that
limits damage after a partial failure. If the action is high impact or
irreversible, require human approval before execution and preserve the approval
identity in the trace.

## Demo notes

- Run the Lab 7 duplicate, stale-state, and missing-approval cases.
- Keep state changes synthetic and non-destructive.

## Learner practice

Write an action contract with `idempotency_key`, `state_version`,
`approval_required`, `approval_id`, `compensation_action`, and `audit_event`.

## What this lesson does not prove

Synthetic side-effect checks do not prove transactional behavior or exactly-once
delivery in a distributed production system.
