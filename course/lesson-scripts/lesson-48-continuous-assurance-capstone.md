# Lesson 48: Continuous Assurance Capstone

Module: 11 — Continuous assurance and production implementation
Suggested runtime: 15–20 minutes
Primary lab: Lab 8 — Build the local telemetry vertical slice

## Learner objective

By the end of this lesson, you can connect security controls, telemetry
health, evaluation evidence, incident response, and a bounded release decision.

## Slide and recording plan

1. **The complete assurance loop**.
2. **Security finding versus telemetry failure**.
3. **Evidence completeness and uncertainty**.
4. **Release, hold, revise, rollback, or escalate**.
5. **Final learner report**.

## Speaker script

Continuous assurance is the loop that keeps a decision honest after the first
evaluation. It combines security controls, application behavior, telemetry
health, evaluator quality, human review, incident response, and change history.

The capstone must distinguish three things: the agent may have failed, the
monitor may have failed, or the evidence may be incomplete. Those states require
different actions. A missing trace is not proof of a safe run, and a blocked
tool is not proof that the overall workflow is unusable.

Write the release decision only after checking control coverage, telemetry
completeness, high-risk findings, drift signals, and ownership. The decision
should name what changed, what evidence was inspected, what remains uncertain,
and what action follows.

## Demo notes

- Run Labs 7 and 8.
- Complete one combined report with security findings, telemetry health,
  evaluation results, incident action, and regression case.
- Recording boundary: synthetic evidence only.

## Learner practice

Produce a bounded report with: decision, revision, security controls, telemetry
health, evaluation findings, uncertainty, owner, rollback trigger, and next
review date.

## What this lesson does not prove

The capstone does not certify a deployed agent as secure, observable, reliable,
or compliant. It demonstrates the evidence and ownership structure required for
those claims to be investigated.
