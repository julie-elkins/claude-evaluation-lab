# Lesson 44: Monitor the Monitor and Resilience

Module: 10 — Security and assurance controls
Suggested runtime: 12–15 minutes
Primary lab: Lab 8 — Build the local telemetry vertical slice

## Learner objective

By the end of this lesson, you can detect telemetry loss, alert failure,
resource exhaustion, and unsafe fallback instead of treating silence as health.

## Slide and recording plan

1. **A quiet dashboard is ambiguous**.
2. **Telemetry health signals** — accepted, dropped, delayed, and rejected.
3. **Alert quality** — threshold, precision, recall, and ownership.
4. **Resilience** — rate limits, backpressure, fallback, and safe shutdown.
5. **Demo: break the local telemetry pipeline**.

## Speaker script

Monitoring the application is not enough. We also need to monitor whether the
monitoring path is receiving, preserving, and exporting evidence. A missing span
can mean a healthy run, a dropped event, a collector outage, or an instrumented
code path that never ran.

Add telemetry health signals: records received, records rejected, records
dropped, export latency, queue depth, and the age of the newest record. A
dashboard should distinguish “no failures observed” from “no evidence arrived.”

Alert quality has two sides. Precision asks how many alerts represent real
conditions. Recall asks how many planted or known conditions were detected.
Neither is meaningful without a declared consequence and review process.

Resilience includes rate limits, backpressure, bounded retries, safe fallback,
and shutdown. A fallback that bypasses authorization or logging is not a safe
fallback. A retry loop that protects availability by multiplying side effects
is also a failure.

## Demo notes

- Run Lab 8 with the dropped-record and exporter-failure cases.
- Show `unavailable` or `not_evaluated` rather than a green result when evidence
  is missing.

## Learner practice

Define five telemetry-health metrics, one alert rule, one fallback rule, and one
condition that must stop the workflow.

## What this lesson does not prove

The local pipeline demonstrates control logic; it does not prove capacity,
latency, availability, or alert delivery in a deployed environment.
