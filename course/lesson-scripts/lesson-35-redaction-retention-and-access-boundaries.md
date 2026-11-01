# Lesson 35: Redaction, Retention, and Access Boundaries

Module: 8 — Privacy, Monitoring, and Incident Response
Suggested runtime: 10–12 minutes
Primary lab: Lab 6 — Observe the agent before you trust the dashboard

## Learner objective

By the end of this lesson, you can design a minimum-evidence telemetry policy
that supports investigation without treating raw agent content as harmless.

## Slide and recording plan

1. **Telemetry is data** — prompts, tool arguments, outputs, and identifiers
   may be sensitive.
2. **Classify before retaining** — metadata, redacted content, restricted
   content, and forbidden content.
3. **Minimum evidence** — preserve what supports the decision and remove what
   does not.
4. **Retention and access** — define duration, owner, and review.
5. **Demo: inspect the raw-content negative control**.

## Speaker script

Observability improves when we can see the path, but visibility creates a data
responsibility. Prompts, outputs, tool arguments, retrieved documents, user
identifiers, credentials, and state details may need different controls.

Start with the decision. If a tool-authorization finding only needs the tool
name, scope, authorization result, and revision, do not retain the raw
customer payload to prove the finding. Store synthetic or redacted identifiers
where they are enough.

Define classes before recording: safe metadata, redacted content, restricted
content, and content that must not be retained. Add retention duration, access
owner, deletion path, and review date. A retention policy is not complete if no
one can explain who can access the trace or how it disappears.

In the demo, inspect `trace-raw-content-001`. The run reached a terminal state,
but the privacy boundary failed. The correct action is not to celebrate the
successful completion; it is to hold the evidence path and investigate the
capture policy.

The cost of retaining too little is an investigation that cannot explain a
failure. The cost of retaining too much is privacy exposure and an unsafe
public artifact. The course chooses synthetic metadata for the required path.

## Demo notes

- Compare `redaction_status` across the Lab 6 traces.
- Show that privacy findings remain separate from task correctness.
- Recording boundary: never substitute real prompts, credentials, or customer
  payloads into the lab.

## Learner practice

For one trace field, record:

`data_class`, `purpose`, `retention_period`, `access_owner`, `redaction_rule`,
and `deletion_trigger`.

Mark whether the field belongs in a public teaching artifact.

## What this lesson does not prove

A redaction flag is not proof that every sensitive value was removed. Test
redaction with representative synthetic patterns and review the actual emitted
artifact.
