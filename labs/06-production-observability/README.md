# Lab 6: Observe the agent before you trust the dashboard 🔬

This lab teaches production-oriented agent observability using synthetic
traces. Observability means collecting enough telemetry—traces, events, and
metrics—to reconstruct what happened. Evaluation means applying a declared
rule to that evidence to support a decision. A dashboard without an evaluation
boundary can show activity without showing whether the workflow was safe or
successful.

## What you will learn

You will inspect:

- a provider-neutral trace contract;
- workflow, model, tool, state, and terminal spans;
- latency, token, cost, and retry signals;
- authorization and terminal-state findings;
- redaction and public-data boundaries;
- incident severity and ownership; and
- the trace-to-test-case feedback loop.

The fields are shaped like production telemetry, but the lab remains
offline-first and does not require an OpenTelemetry package, a collector, a
dashboard, a Claude API key, or network access.

## Why this matters

An evaluator can report that a task failed, but it cannot explain the failure if
the agent path was not captured. Conversely, a complete trace can explain what
happened without proving that the behavior met the product requirement. The
production control needs both: trace evidence for reconstruction and evaluation
evidence for judgment.

## Run it

From the repository root:

```bash
uv run python labs/06-production-observability/run_lab.py
```

To inspect the synthetic traces before evaluation:

```bash
uv run python labs/06-production-observability/run_lab.py --show-traces
```

To save a local report:

```bash
uv run python labs/06-production-observability/run_lab.py --output /tmp/observability-report.json
```

## Expected result

The report should show:

- one healthy trace passing;
- an unauthorized tool being caught;
- a missing terminal state becoming `not_evaluated`;
- a cost budget breach being caught;
- a retry loop being caught;
- raw content being rejected by the privacy boundary;
- metrics remaining separate from findings;
- incident findings with severity and action; and
- trace failures converted into regression-case candidates.

The observability suite passes because it catches the planted failures. The
candidate release decision is blocked because the synthetic trace set contains
failures that require investigation.

## Workflow map

```text
agent run
   |
   v
trace contract ----> spans and events ----> metrics
   |                       |                  |
   |                       v                  v
   |                 reconstruct path    budget signal
   v
privacy and completeness checks
   |
   v
evaluation findings ----> incident action ----> regression case
```

## Evidence to inspect

Review these fields:

- `trace_schema_revision`
- `case_results`
- `metrics`
- `incident_findings`
- `trace_to_case`
- `negative_controls`
- `candidate_release_decision`
- `evidence_template`

Within each trace result, inspect `status`, `reason_code`, `trace_id`, and
`span_names`. The status answers whether the declared check passed; the span
names explain what the trace contained.

## Try the failure

The deliberately degraded traces include:

- `trace-unauthorized-tool-001`: a tool span outside the authorized boundary;
- `trace-missing-terminal-001`: an incomplete trace with no terminal state;
- `trace-cost-spike-001`: a synthetic spend budget breach;
- `trace-retry-loop-001`: repeated tool errors beyond the retry limit; and
- `trace-raw-content-001`: content that was not redacted before retention.

The evaluator must catch all of them. The healthy trace demonstrates that a
complete, redacted, bounded path can pass the observability contract.

## Troubleshooting

1. Run the command from the repository root.
2. Confirm `uv --version` is available.
3. If the report exits non-zero, inspect the report; the lab intentionally
   returns non-zero only if the evaluator fails to catch a planted failure.
4. Keep trace identifiers synthetic and do not replace them with production
   session IDs or raw prompts.

## Evidence template

Copy this structure into your own notes:

```text
trace_schema_revision:
trace_ids:
workflow_name:
model_revision:
agent_revision:
terminal_states:
span_inventory:
latency_and_token_signals:
cost_and_retry_signals:
privacy_status:
incident_findings:
regression_cases_created:
candidate_release_decision:
limitations:
```

## What this does not prove

This is an offline synthetic observability control. It does not prove that a
live exporter captures every event, that a dashboard is correctly configured,
that a production SLO is achievable, that redaction is complete for every
payload, or that an incident owner will respond in time.

## Optional extension

Map the lab's fields to the current OpenTelemetry GenAI semantic conventions.
Then compare the same synthetic trace in one local backend, such as Phoenix or
Langfuse. Keep the backend optional and record which fields were transformed,
dropped, or redacted.
