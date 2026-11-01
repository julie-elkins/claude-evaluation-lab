# Lesson 36: Alerts, Incidents, Rollback, and Ownership

Module: 8 — Privacy, Monitoring, and Incident Response
Suggested runtime: 12–15 minutes
Primary lab: Lab 6 — Observe the agent before you trust the dashboard

## Learner objective

By the end of this lesson, you can turn an observability finding into an
owned incident, containment action, and follow-up evaluation case.

## Slide and recording plan

1. **A signal becomes an incident through a rule**.
2. **Severity and action** — distinguish investigation from containment.
3. **Ownership** — responder, approver, communicator, and evaluator owner.
4. **Rollback is a rehearsed path** — not a hope.
5. **Demo: inspect Lab 6 incident findings and actions**.

## Speaker script

An alert is a signal that crossed a declared threshold. An incident is an
operational condition that requires coordinated action. The difference matters:
without a rule, a dashboard produces attention but not ownership.

Define severity using consequence and urgency. An unauthorized tool action may
require an immediate hold even if the overall error rate is low. A moderate
latency increase may require investigation but not rollback. The threshold must
name the action, not only the color on a chart.

Name owners. One person or role investigates, another may approve containment,
someone communicates the status, and an evaluator owner converts the failure
into a case or control. In a small team, one person may hold several roles, but
the responsibilities still need to be visible.

Rollback is the ability to return to a known acceptable revision. Rehearsal
means testing that path before it is needed, including the trigger, owner,
change record, and evidence that the rollback completed.

In the demo, inspect the incident findings produced from the Lab 6 traces.
Notice that each finding contains a reason code, severity, and action. The next
step is not merely to close the alert; it is to create a regression case that
prevents the same failure from becoming invisible.

The cost of alerting without ownership is silent accumulation. The cost of
rollback without rehearsal is discovering during an incident that the recovery
path depends on the system that is failing.

## Demo notes

- Run Lab 6 and inspect `incident_findings`.
- Add an owner and rollback trigger to one finding.
- Recording boundary: use synthetic incident names and no live paging system.

## Learner practice

Complete an incident record:

`severity`, `trigger`, `owner`, `containment_action`, `rollback_trigger`,
`communication_owner`, `regression_case_id`, and `review_date`.

Explain why the action is proportionate to the failure cost.

## What this lesson does not prove

A written incident record does not prove that a real responder will act within
the target window. Operational readiness requires rehearsal, access, and
evidence that the runbook works in the deployed environment.
