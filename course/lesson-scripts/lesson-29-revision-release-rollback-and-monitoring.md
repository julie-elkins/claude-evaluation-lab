# Lesson 29: Revision, Release, Rollback, and Monitoring

Module: 5 — Benchmarks, Release, and Capstone
Suggested runtime: 12–15 minutes
Primary lab: Produce a release decision with rollback evidence

## Learner objective

By the end of this lesson, you can connect evaluation evidence to a revision, release, rollback, and monitoring decision.

## Slide and recording plan

1. **An evaluation is a change decision** — revision, release, hold, or rollback.
2. **Revision binding** — identify exactly what was tested.
3. **Rollback rehearsal** — prove the recovery path before release.
4. **Monitoring** — watch for drift, new failures, and evidence gaps.
5. **Demo: inspect a run manifest and rollback record**.

## Speaker script

An evaluation report matters because it supports a change decision. The possible outcomes are not only ship or do not ship. We may revise the system, release with a bounded rollout, hold for more evidence, or roll back after a failure.

Bind the evidence to a precise revision. Record the model or prompt version, tool catalog, evaluator configuration, case set, harness revision, and run timestamp. Without revision binding, a later reader cannot tell whether the evidence applies to the system that is actually running.

Rollback is the ability to return to a known acceptable state. A rollback rehearsal is a controlled test that proves the path exists and identifies who can trigger it. Rollback does not replace prevention; it limits the duration and impact of a bad release.

Monitoring is the ongoing observation of signals after release. Watch for new failure categories, changes in case mix, rising escalation, tool errors, latency or cost shifts, and evidence that the evaluator no longer reflects the workflow. Monitoring should include an owner and an action threshold.

In the demo, inspect a run manifest and rollback rehearsal record. Identify which revision was tested, what decision was made, what evidence would trigger rollback, and where the owner is named. The course harness’s launch-to-field and monitorability examples provide the pattern.

The cost of weak release evidence is not just a bad score. It is the inability to explain what changed, reproduce the result, or recover quickly when the system behaves differently in the field.

## Demo notes

- Use `examples/run-manifest`, `tools/rollback_rehearsal.py`, and the launch-to-field example.
- Show the exact revision identifiers without claiming they represent a production deployment.
- Show monitoring signals and the action threshold separately.
- Recording boundary: keep release and rollback entirely offline and synthetic.

## Learner practice

Draft a release record with:

`revision`, `case_set`, `evaluator_revision`, `blocking_findings`, `decision`, `rollback_trigger`, `rollback_owner`, `monitoring_signal`, `review_date`.

Add one condition that would move the decision from release to hold.

## What this lesson does not prove

A rehearsed rollback path does not guarantee instant recovery or prevent all impact. Monitoring is only useful when the signal is observable, the threshold is actionable, and an owner responds.
