# Optional live-Claude adapter

This is an optional extension for learners who want to connect the course
evidence contract to a live Claude request. It is not required for the course
and is intentionally separate from the eight offline labs.

## Why this is optional

Live provider calls add cost, latency, changing model behaviour, credentials,
privacy obligations, and network failure. The offline labs remain the required
path because they are deterministic and reproducible. A live result is an
additional observation, not a replacement for the synthetic negative controls
or the evidence contract.

## Before you run a live request

Declare these fields in a local, uncommitted run manifest:

```text
provider: Anthropic
model: <verify the current supported model before recording>
model_snapshot_or_date: <record the exact model identifier or date>
decision_target: <one bounded workflow decision>
case_set_revision: <case set identifier>
evaluator_revision: <evaluator identifier>
request_limit: <maximum request count>
time_limit_seconds: <maximum elapsed time>
token_limit: <maximum input and output budget>
spend_limit_usd: <maximum estimated spend>
redaction_policy: <what is removed before the request>
human_approval: pending
```

Use the current official Anthropic documentation for the request syntax and
model identifiers when recording the lesson. Do not copy an old API example
into the course and present it as current.

## Data boundary

Use synthetic prompts and synthetic evidence first. Do not send secrets,
credentials, personal data, customer content, private prompts, or raw
production traces. Redact logs before saving them, and define the retention
period for any provider response.

## Evidence to preserve

Keep the live adapter as one evaluator or transport layer in the same report
used by the offline path. Preserve:

- the exact model identifier or model date;
- request and response metadata needed to explain the run;
- the case, evidence, evaluator, and prompt revisions;
- transport status separately from semantic outcome;
- token and estimated-cost usage;
- refusal, unavailable, skipped, and not-evaluated states; and
- the independent check that can challenge a fluent false pass.

If the provider call cannot run, record `unavailable` or `not_evaluated`
according to the report vocabulary. Do not silently retry without preserving
the attempt and the bounded retry rule.

## What this extension proves

It shows how to attach one live Claude observation to the course's evidence
contract under explicit limits.

## What it does not prove

One live request or a small live sample does not prove model quality,
production safety, generalization, cost stability, or release readiness. The
offline negative controls, representative cases, independent checks, and human
approval boundary still apply.
