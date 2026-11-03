# Lesson 37: Turning Traces into Evaluation Cases

Module: 9 — Continuous Evaluation and Production Capstone
Suggested runtime: 10–12 minutes
Primary lab: Lab 6 — Observe the agent before you trust the dashboard

## Learner objective

By the end of this lesson, you can turn a production-style trace finding into
a bounded evaluation case without copying sensitive content.

## Slide and recording plan

1. **A trace is an observation, not yet a reusable test**.
2. **Classify the root cause before editing** — prompt, model, environment,
   tool, code, orchestration, evaluator, or data.
3. **Replay the failure point, then validate from the beginning**.
4. **Minimize and synthesize** — preserve the decision boundary, not the raw
   payload.
5. **Add to the right data role** — calibration, regression, or held-out.
6. **Trace-to-evaluator design skill** — inspect evidence, find patterns, and
   draft a use-case-specific evaluator.
7. **Demo: inspect Lab 6 `trace_to_case`**.

## Speaker script

Production telemetry becomes useful to evaluation when a finding can be
reproduced as a case. Start by classifying the finding. Was the task wrong, the
tool unauthorized, the state unchanged, the cost above budget, the trace
incomplete, or the capture policy unsafe? Before editing a prompt, classify the
likely root cause as a prompt, model, environment, tool, code, orchestration,
evaluator, or data problem. The same visible failure can have different fixes,
and changing the prompt first can hide the actual defect.

Use a failure-point replay as a diagnostic filter. Replay means rerunning from
the turn where the failure occurred while holding earlier history fixed. It is
cheap and useful for testing whether a proposed edit affects that decision, but
it cannot reveal a new divergence earlier in the run. Any promising change must
then run from the beginning on the matched case set before it supports a
release or architecture decision.

Then minimize the case. Keep the input structure, boundary condition, expected
behavior, evidence requirement, and decision consequence. Remove secrets,
customer content, private identifiers, and raw tool payloads. A synthetic case
can preserve the failure mechanism without preserving the data that caused it.

Choose the data role. A newly discovered failure may belong in a regression set
so the known problem cannot return. It may also need a calibration case if the
rubric is unclear. Keep it out of a held-out measurement set when it was used
to shape the evaluator.

The optional [Trace-to-Evaluator Design
Skill](../TRACE_TO_EVALUATOR_SKILL.md) makes this reasoning repeatable. It
profiles trace completeness, groups recurring failure mechanisms, drafts an
evaluator contract, proposes minimized or synthetic cases, and checks the
evaluator against negative controls. It is a design assistant, not an approval
authority. The human owner still decides whether the evaluator measures the
right construct and whether the data may be retained or shared.

In the demo, inspect `trace_to_case`. The lab proposes a case identifier and
next evaluator, but a human still owns the decision to accept, transform, or
discard the case. Show the root-cause hypothesis, diagnostic replay result, and
full-validation result separately.

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
2. the root-cause hypothesis;
3. the minimum safe case input;
4. the expected outcome;
5. the evidence requirement;
6. the diagnostic replay scope and result;
7. the full-validation plan;
8. the dataset role;
9. the evaluator layer that should detect it; and
10. the negative control that would challenge a false pass.

## What this lesson does not prove

A regression case protects against a known failure mechanism. It does not prove
coverage of all future failures, prove that a prompt was the root cause, or
preserve the original production context. A replay alone is not full validation.
