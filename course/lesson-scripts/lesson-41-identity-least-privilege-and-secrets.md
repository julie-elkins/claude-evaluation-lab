# Lesson 41: Identity, Least Privilege, and Secrets

Module: 10 — Security and assurance controls
Suggested runtime: 12–15 minutes
Primary lab: Lab 7 — Test the agent security boundary

## Learner objective

By the end of this lesson, you can evaluate whether an agent has the right
identity, tool scope, credential boundary, and approval evidence for an action.

## Slide and recording plan

1. **Identity is part of the evidence**.
2. **Least privilege** — the smallest authority that can complete the task.
3. **Credential isolation** — the model must not receive reusable secrets.
4. **Approval and audit** — authority before action, evidence after action.
5. **Demo: compare authorized and over-privileged synthetic traces**.

## Speaker script

Authentication answers “who is calling?” Authorization answers “what may that
identity do?” An agent evaluation needs both because a valid user request can
still be routed through an over-privileged service identity.

Least privilege means granting only the authority required for the declared
task. Evaluate the tool scope, resource scope, tenant scope, and action scope
separately. A tool can be valid but still unauthorized for this user, record, or
workflow state.

Secrets should remain behind a controlled service boundary. The model can
request an approved action, but the raw token, password, or signing key should
not become prompt content or ordinary trace content. Rotate credentials without
changing the learner’s synthetic evidence.

For a state-changing action, require an authority record before the call and an
audit record after it. If either is missing, the result is not a successful
security check just because the tool returned `ok`.

## Demo notes

- Inspect Lab 7 fields for `principal`, `authorized_scope`, `credential_exposure`,
  and `approval_id`.
- Compare a tool-success case with an authorization-failure case.

## Learner practice

Write an authorization contract containing `principal`, `resource_scope`,
`action_scope`, `approval_required`, `credential_boundary`, and `audit_event`.

## What this lesson does not prove

Synthetic authorization metadata does not prove that a deployed identity system,
secret store, or audit service enforces the same boundary.
