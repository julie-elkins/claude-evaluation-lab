# Lesson 5: Representative Evaluation Cases

Module: 2 — Human Evaluation and Test Design
Suggested runtime: 10–12 minutes
Primary lab: Extend the case inventory for the semantic-outcomes lab

## Learner objective

By the end of this lesson, you can explain why an evaluation case is evidence about a decision, not merely an example prompt, and build a small case set that includes normal, boundary, missing-information, conflicting-information, and failure paths.

## Slide and recording plan

1. **The evaluation case is the unit of evidence** — prompt, context, expected behavior, observed result, and decision.
2. **A useful case set has shape** — normal, boundary, missing, conflicting, unauthorized, and failure cases.
3. **Coverage is a claim** — show a case matrix with rows for scenarios and columns for expected outcome, evidence, and risk.
4. **Demo: inspect the starter case inventory** — begin from the synthetic semantic-outcomes examples.
5. **Practice: add three cases** — one boundary case, one missing-evidence case, and one recovery case.

## Speaker script

An evaluation case is a deliberately chosen situation used to test a decision. It is more than a prompt and a model response. A useful case records the input, relevant context, expected behavior, observed behavior, evidence, and the decision that follows.

That distinction matters because a collection of interesting examples can still leave the important paths untested. If every example is a normal success, the evaluation may tell us that the system works when nothing goes wrong. It does not tell us whether the system handles ambiguity, missing context, conflicting evidence, authorization boundaries, or recovery after a failed action.

Start with a small case matrix. Include normal cases first, then boundary cases where the expected behavior changes at a limit. Add missing-information cases, conflicting-information cases, unauthorized-request cases, and explicit failure or recovery cases. These categories are not a universal checklist for every product. They are a starting point for making the risks visible before we decide how much coverage is enough.

For each case, write the expected semantic outcome in plain language. A semantic outcome is the meaning of what happened, such as “the agent escalated because evidence was incomplete,” rather than only a transport result such as “the request returned successfully.” If the expected outcome is not written down, a reviewer can unconsciously grade the answer against a moving target.

The goal is not to maximize the number of cases. The goal is to make the decision defensible. A small, risk-based set that includes the paths most likely to change the release decision is more useful than a large set of low-risk happy paths. The cost of getting this wrong is false confidence: the dashboard looks green while the untested boundary is where users are harmed or work is lost.

In the demo, inspect the existing synthetic cases and identify which decision each one supports. Then add three cases without changing the evaluator. This separates test-design work from evaluator tuning. If a case cannot be linked to a decision, either rewrite it or mark it as exploratory rather than presenting it as release evidence.

## Demo notes

- Start in `labs/01-semantic-outcomes/README.md` and `run_lab.py`.
- Show the existing normal, empty-context, and guarded escalation paths.
- Open `AGENT_EVALUATION_CHECKLIST.md` and connect case selection to the checklist’s scenario coverage.
- Do not imply that the current small case set proves production readiness.
- Recording boundary: show synthetic identifiers and expected outcomes only; do not use private customer prompts.

## Learner practice

Create a case table with these columns:

`case_id`, `risk`, `input_condition`, `expected_semantic_outcome`, `required_evidence`, `failure_if_missing`.

Add one case for a normal path, one for missing evidence, one for conflicting evidence, one for an unauthorized action, and one for recovery after a failed attempt. Mark which cases are release-blocking and explain why.

## What this lesson does not prove

Representative cases do not prove that the sample reflects every production user or every future failure mode. They make the tested decision more credible; they do not eliminate sampling risk.
