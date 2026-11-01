# Lesson 38: Connecting a Bounded Live Claude Observation

Module: 9 — Continuous Evaluation and Production Capstone
Suggested runtime: 10–12 minutes
Primary lab: Optional bounded live-Claude adapter

## Learner objective

By the end of this lesson, you can attach one live Claude observation to the
course evidence contract without making live access a learner prerequisite.

## Slide and recording plan

1. **Live access is an extension** — not a replacement for offline controls.
2. **Declare the bounds** — model, revision, request, time, token, spend, and
   privacy limits.
3. **Observe the agent loop** — preserve tool, stop, error, and terminal
   evidence.
4. **Keep provider behavior dated** — verify current official syntax before
   recording.
5. **Demo: inspect the adapter manifest and unavailable path**.

## Speaker script

The required course path stays offline because live calls add credentials,
cost, latency, changing model behavior, privacy obligations, and network
failure. A live observation is useful when it is bounded and clearly labeled
as one observation rather than a production conclusion.

Before running, declare the model identifier or date, decision target, case and
evaluator revisions, request limit, time limit, token limit, spend limit,
redaction policy, and human approval state. These fields make the observation
auditable and keep a recording from silently becoming an unbounded experiment.

Use the current official Claude documentation for syntax, SDK behavior, hooks,
stop reasons, and monitoring fields. Preserve provider-specific evidence at the
adapter boundary, then map it into the same report vocabulary used by the
offline labs.

If the request cannot run, record `unavailable` or `not_evaluated` according to
the declared rule. Do not silently retry until a convenient result appears.
The attempt and the retry limit are part of the evidence.

The cost of a live demo without bounds is a lesson that cannot be reproduced
and may spend money or expose data. The cost of treating one successful request
as a release result is false confidence.

## Demo notes

- Use `labs/07-live-claude-adapter/README.md`.
- Show the local manifest fields before any request is considered.
- Keep the example optional and use synthetic prompts and evidence.
- Recording boundary: verify official documentation immediately before
  recording provider syntax.

## Learner practice

Complete a local live-observation manifest with:

`provider`, `model`, `model_snapshot_or_date`, `decision_target`,
`request_limit`, `time_limit_seconds`, `token_limit`, `spend_limit_usd`,
`redaction_policy`, and `human_approval`.

Add the exact condition that should produce `unavailable`.

## What this lesson does not prove

One live observation does not prove model quality, generalization, production
safety, cost stability, or release readiness. It only extends the bounded
evidence contract with one provider observation.
