# Lesson 43: Telemetry Security and Auditability

Module: 10 — Security and assurance controls
Suggested runtime: 12–15 minutes
Primary lab: Lab 7 — Test the agent security boundary

## Learner objective

By the end of this lesson, you can protect evaluation and observability evidence
with classification, access, retention, deletion, and audit controls.

## Slide and recording plan

1. **Telemetry is data**.
2. **Classification** — metadata, redacted content, restricted content.
3. **Access boundary** — operator, developer, evaluator, and security roles.
4. **Deletion and evidence preservation**.
5. **Demo: inspect raw-content, access, and audit findings**.

## Speaker script

Telemetry is not automatically safe because it was emitted by a monitoring
library. Prompts, outputs, tool arguments, retrieved documents, and identifiers
can contain sensitive information. Start with the decision: retain only what is
needed to explain or evaluate it.

Classification makes the boundary operational. Metadata may be broadly visible.
Redacted content may support debugging. Restricted content may require a
separate access path. Content that must not be retained should be rejected at
the collection boundary, not merely hidden in a dashboard.

Access is part of auditability. Record who viewed or changed evidence, why,
which role authorized it, and whether the access was allowed. Deletion should
also be testable; a policy that says “delete after 30 days” is incomplete if no
one can verify deletion.

Incident evidence may need a preservation exception, but that exception should
have an owner, scope, expiration, and access log. Otherwise an incident becomes
an excuse to retain everything forever.

## Demo notes

- Inspect Lab 7 redaction, access, retention, and audit fields.
- Show that a complete task result can still fail the telemetry security check.

## Learner practice

Create a field policy with `data_class`, `purpose`, `access_role`,
`retention_period`, `deletion_check`, and `audit_required`.

## What this lesson does not prove

A synthetic field policy does not prove that a deployed telemetry backend
enforces access, deletion, or tamper resistance.
