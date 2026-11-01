# Lesson 37: Turning Traces into Evaluation Cases

Module: 9 — Continuous Evaluation and Production Capstone
Suggested runtime: 10–12 minutes
Primary lab: Lab 6 — Observe the agent before you trust the dashboard

## Learner objective

By the end of this lesson, you can turn a production-style trace finding into
a bounded evaluation case without copying sensitive content.

## Slide and recording plan

1. **A trace is an observation, not yet a reusable test**.
2. **Classify the failure** — task, safety, tool, state, cost, privacy, or
   instrumentation.
3. **Minimize and synthesize** — preserve the decision boundary, not the raw
   payload.
4. **Add to the right data role** — calibration, regression, or held-out.
5. **Demo: inspect Lab 6 `trace_to_case`**.

## Speaker script

Production telemetry becomes useful to evaluation when a finding can be
reproduced as a case. Start by classifying the finding. Was the task wrong, the
tool unauthorized, the state unchanged, the cost above budget, the trace
incomplete, or the capture policy unsafe?

Then minimize the case. Keep the input structure, boundary condition, expected
behavior, evidence requirement, and decision consequence. Remove secrets,
customer content, private identifiers, and raw tool payloads. A synthetic case
can preserve the failure mechanism without preserving the data that caused it.

Choose the data role. A newly discovered failure may belong in a regression set
so the known problem cannot return. It may also need a calibration case if the
rubric is unclear. Keep it out of a held-out measurement set when it was used
to shape the evaluator.

In the demo, inspect `trace_to_case`. The lab proposes a case identifier and
next evaluator, but a human still owns the decision to accept, transform, or
discard the case.

The cost of never converting production findings into tests is repeated
incidents. The cost of copying traces directly into a dataset is leakage,
privacy exposure, and an evaluation set that nobody can safely share.

## Demo notes

- Run Lab 6 and inspect each trace-to-case record.
- Show the link between `reason_code` and `next_evaluator`.
- Recording boundary: explain the transformation without displaying raw
  production content.

## Learner practice

Take one synthetic trace finding and write:

1. the failure mechanism;
2. the minimum safe case input;
3. the expected outcome;
4. the evidence requirement; and
5. the dataset role.

## What this lesson does not prove

A regression case protects against a known failure mechanism. It does not prove
coverage of all future failures or preserve the original production context.
