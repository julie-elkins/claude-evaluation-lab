# Lesson 45: Build a Local Telemetry Vertical Slice

Module: 11 — Continuous assurance and production implementation
Suggested runtime: 15–18 minutes
Primary lab: Lab 8 — Build the local telemetry vertical slice

## Learner objective

By the end of this lesson, you can follow one agent run from instrumentation
through collection, storage, query, alert, and evaluation case.

## Slide and recording plan

1. **Vertical slice** — one complete path from event to action.
2. **Instrumentation** — emit stable identifiers and revisions.
3. **Collection and processing** — validate, redact, and count loss.
4. **Backend query** — reconstruct the run and calculate signals.
5. **Alert to regression case**.

## Speaker script

A vertical slice is a complete working path across the system, not a separate
piece of each layer. This lesson follows one synthetic agent run from its
instrumented events to a local backend record, a dashboard-style query, an
alert, and a regression case.

The important design choice is to preserve identity across every stage. The
trace ID connects the workflow, model, tool, state, and terminal events. The
revision fields tell us which application, policy, model, and evaluator
produced the evidence.

The collector boundary is where we validate required fields, redact content,
and count rejected or dropped records. The backend is not allowed to silently
repair missing evidence. A missing terminal event should remain visible as
incomplete.

The final step connects operations to evaluation. A detected unauthorized tool
or missing telemetry path becomes a minimized, safe regression case rather than
an unstructured ticket.

## Demo notes

- Run Lab 8 and inspect each pipeline stage.
- Compare the healthy trace with the dropped-record case.
- Optional extension: map the emitted fields to an OpenTelemetry collector and
  a local backend.

## Learner practice

Draw the six stages: instrument, collect, process, store, query, and act. Add
one failure mode and one evidence field at each stage.

## What this lesson does not prove

The local vertical slice proves the control path is runnable, not that a
production collector or backend has sufficient scale, durability, or access
control.
