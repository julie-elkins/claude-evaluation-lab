# Lesson 30: Capstone Evaluation Report

Module: 5 — Benchmarks, Release, and Capstone
Suggested runtime: 15–20 minutes
Primary lab: Complete the course evaluation report

## Learner objective

By the end of this lesson, you can produce a compact evaluation report that connects a declared decision to evidence, limitations, ownership, and a release action.

## Slide and recording plan

1. **The report answers one decision** — what is being decided and for whom.
2. **Evidence map** — cases, evaluators, findings, uncertainty, and high-risk slices.
3. **Decision and action** — release, revise, hold, escalate, or rollback.
4. **Limitations and ownership** — what the report does not prove and who acts next.
5. **Practice: complete and review the capstone report**.

## Speaker script

The capstone report is not a score dump. It is a decision record. Start with the decision: what are we deciding, what revision or workflow does it concern, and what risk matters most?

Then map the evidence. Include the case set, data roles, deterministic checks, semantic or human evaluation, agent trajectory findings, negative controls, high-risk slices, uncertainty, and any benchmark evidence. Preserve the underlying findings so a reader can see how the conclusion was reached.

State the decision and the action separately. “Release” is an action. “The variant meets the evidence contract for the bounded use case” is the conclusion that supports it. Other outcomes include revise, hold, escalate, or rollback. If evidence is missing or conflicting, say so instead of converting uncertainty into a pass.

Write limitations in operational terms. Explain what the evaluation did not test, which assumptions it relies on, and what future evidence is required. Name the owner, monitoring signal, rollback trigger, and review date. A report without ownership is a historical artifact; it does not control what happens next.

Use the course harness as the demonstration backbone. The learner’s final artifact should show how transport status is separated from semantic outcome, how evidence completeness is checked, how negative controls run, and how the release boundary is enforced. The report should be readable by someone who did not watch the lesson.

End with a practice-question placeholder for the final course deck. Ask learners to identify the strongest unsupported claim, the missing evidence item, the release-blocking finding, and the next safe action. These questions test decision reasoning rather than recall of metric names.

The cost of a weak capstone is that every earlier lesson remains disconnected. The report is where measurement becomes accountable action.

## Demo notes

- Use a course-owned Markdown or JSON report template.
- Run the offline showcase or launch-to-field example before filling the report.
- Include at least one planted failure and explain how it affected the decision.
- Recording boundary: label the report as a synthetic course artifact, not a production approval.

## Learner practice

Complete a report with these sections:

1. decision and scope,
2. revision and evidence contract,
3. case inventory and data split,
4. evaluator layers,
5. findings and high-risk slices,
6. negative controls,
7. limitations and uncertainty,
8. release or revision action,
9. owner, monitoring, and rollback trigger.

> **Learner checkpoint — peer-review the report**
>
> Have a peer review the report using three questions:
>
> 1. Can they identify the decision?
> 2. Can they trace each important claim to evidence?
> 3. Can they tell what the report does not prove?

## What this lesson does not prove

A complete report does not make an evaluation complete forever. The decision is bounded by its revision, cases, evidence, and date; changes to the system or risk environment require a new evaluation.
