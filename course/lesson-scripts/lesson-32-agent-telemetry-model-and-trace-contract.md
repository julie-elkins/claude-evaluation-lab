# Lesson 32: The Agent Telemetry Model and Trace Contract

Module: 6 — Production Observability Foundations
Suggested runtime: 10–12 minutes
Primary lab: Lab 6 — Observe the agent before you trust the dashboard

## Learner objective

By the end of this lesson, you can define a trace contract for an agent run and
identify when missing telemetry makes a result not evaluated.

## Slide and recording plan

1. **Trace hierarchy** — session, turn, workflow, model, tool, state, and
   terminal event.
2. **Required identity** — trace, session, workflow, model, agent, and
   evaluator revisions.
3. **Required path evidence** — observations, decisions, tools, arguments,
   results, and state transitions.
4. **Completeness is a control** — missing terminal or tool evidence stays
   visible.
5. **Demo: inspect the incomplete Lab 6 trace**.

## Speaker script

A production trace is not just a line of text. It is a structured record of the
agent path. The exact hierarchy can vary, but a useful teaching model is
session, turn, workflow, model call, tool call, state change, and terminal
event.

Every record needs stable identity. Capture the trace ID, session ID, workflow
name, model revision, agent or policy revision, and evaluator revision. These
fields bind the evidence to the system that produced it. Without revision
binding, a trace from yesterday can be mistaken for evidence about today's
workflow.

The trace also needs the path: what context was available, what decision was
made, which tool was selected, what arguments were sent, what result returned,
how state changed, and why the agent stopped. Do not capture more content than
the decision requires. Structure and privacy are part of the contract.

In the demo, inspect `trace-missing-terminal-001`. Its model span exists, but
the terminal state is absent. The correct outcome is `not_evaluated`, not pass
and not necessarily model failure. The evaluator lacks evidence that the
declared path reached its end.

The cost of a weak trace contract is an investigation that reconstructs the
most convenient story from incomplete events. The cost of an overly broad
contract is unnecessary data collection, storage cost, and privacy exposure.

## Demo notes

- Run Lab 6 with `--show-traces`.
- Compare the healthy trace with the missing-terminal trace.
- Highlight the required fields in `evidence_template`.
- Recording boundary: describe payload classes without displaying real content.

## Learner practice

Write a trace contract for one workflow with these fields:

`trace_id`, `session_id`, `workflow_name`, `model_revision`,
`agent_revision`, `span_id`, `span_kind`, `terminal_state`,
`redaction_status`.

Mark each field as required, conditional, or forbidden to retain in raw form.

## What this lesson does not prove

A trace schema does not guarantee that the application emits every event or
that timestamps and attributes are correct. Instrumentation itself requires
negative controls and periodic completeness checks.
