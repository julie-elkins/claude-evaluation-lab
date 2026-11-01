# Lesson 33: OpenTelemetry Spans and Semantic Conventions

Module: 7 — Instrumentation and Operational Signals
Suggested runtime: 10–12 minutes
Primary lab: Lab 6 — Observe the agent before you trust the dashboard

## Learner objective

By the end of this lesson, you can map an agent workflow to provider-neutral
spans and identify where a provider adapter must preserve meaning.

## Slide and recording plan

1. **Why a shared vocabulary matters** — portable evidence.
2. **Span kinds** — workflow, model, tool, state, evaluator, and event.
3. **Attributes** — identity, model, tokens, tool authorization, and outcome.
4. **Adapter boundary** — translate provider fields without changing the
   decision meaning.
5. **Demo: map the Lab 6 fields to an OpenTelemetry-shaped trace**.

## Speaker script

OpenTelemetry is a vendor-neutral way to represent and export telemetry. The
course uses it as a vocabulary and contract, not as a required dependency in
the offline path.

A span represents one timed operation inside a larger trace. For an agent, useful
spans may represent the workflow, a model call, a tool call, a state check, or
an evaluator. The names matter less than preserving the meaning: which
operation happened, which revision performed it, what it consumed, and what
result it produced.

Provider adapters are translation boundaries. A Claude-specific request ID,
tool-use record, or stop reason can be mapped to a provider-neutral field, but
the adapter must not silently drop authorization, terminal-state, cost, or
error meaning. Record the provider and adapter revision so a later reader can
tell what was transformed.

In the demo, compare the synthetic spans with the required evidence template.
Ask which fields can be queried across providers and which remain provider
extensions. A portable schema should make common decisions comparable without
pretending the providers behave identically.

The cost of skipping a shared vocabulary is lock-in and incomparable evidence.
The cost of pretending the vocabulary is complete is false portability: a
field can have the same name while representing a different event.

## Demo notes

- Open the Lab 6 trace inventory and the OpenTelemetry GenAI semantic
  conventions before recording.
- Map `workflow`, `model`, `tool`, `state`, and `event` spans.
- Recording boundary: verify current convention names before recording because
  standards and provider adapters change.

## Learner practice

Choose one provider-specific event and write:

1. the provider field;
2. the provider-neutral field;
3. the information that could be lost; and
4. the test that would detect the loss.

## What this lesson does not prove

Mapping fields to a standard does not prove that an exporter is configured
correctly or that a backend retains the fields. Validate the emitted trace,
not only the instrumentation code.
