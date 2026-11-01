# Lab 8: Build the local telemetry vertical slice 📡

This lab follows a synthetic agent run through instrumentation, collection,
redaction, local storage, dashboard-style queries, alerting, and regression-case
creation.

It is intentionally standard-library-only. The local pipeline makes the
control path runnable without requiring an OpenTelemetry package, collector,
vendor backend, API key, or network access. An optional extension maps the same
fields to a real local backend.

## What you will learn

You will inspect:

- stable trace and span identity;
- instrumentation and revision fields;
- collector validation and redaction;
- accepted, rejected, and dropped telemetry;
- local backend records and dashboard-style metrics;
- application findings versus telemetry-pipeline findings;
- alerts and candidate incidents; and
- trace-to-regression-case conversion.

## Run it

From the repository root:

```bash
uv run python labs/08-telemetry-vertical-slice/run_lab.py
```

To inspect every pipeline stage:

```bash
uv run python labs/08-telemetry-vertical-slice/run_lab.py --show-stages
```

To save a local report:

```bash
uv run python labs/08-telemetry-vertical-slice/run_lab.py --output /tmp/telemetry-report.json
```

## Expected result

The pipeline suite should pass because it catches:

- an unauthorized tool event;
- a raw-content event that must be redacted or rejected;
- a missing span;
- a dropped record;
- an exporter failure; and
- a monitoring rule that must not turn missing evidence into a green result.

The candidate release decision should be `block` because the synthetic run set
contains findings and telemetry-health failures.

## Workflow map

```text
instrument --> collect --> validate/redact --> store
     |            |             |              |
     v            v             v              v
 revisions    loss counts   privacy status   query
                                                  |
                                                  v
                                      alert --> incident --> case
```

## What this does not prove

The lab proves that a local deterministic pipeline can preserve and evaluate
declared telemetry boundaries. It does not prove production scale, durability,
network security, alert delivery, or backend access control.

## Optional real-backend extension

Map the local fields to OpenTelemetry GenAI semantic conventions, then run one
authorized local collector and backend. Record which fields were transformed,
dropped, sampled, or redacted. Keep this extension optional so the core course
remains reproducible.
