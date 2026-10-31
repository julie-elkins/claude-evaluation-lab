# Lesson 3: Transport status versus semantic outcome

**Module:** Evaluation foundations  
**Estimated runtime:** 10 minutes  
**Lab:** [Lab 1](../../labs/01-semantic-outcomes/README.md)

## Learner objective

By the end of this lesson, you can explain why a successful request does not
prove that the task succeeded, and you can inspect the evidence that separates
the two.

## Slide and recording plan

1. A green request can still contain an empty result.
2. Transport status and semantic outcome are different fields.
3. The naive path: retrying without usable evidence.
4. The guarded path: stop, record, and escalate.
5. Lab instructions and expected output.

## Speaker script

This is the first hands-on lab because it demonstrates the failure we will keep
returning to: a system can report transport success while the requested task
still failed.

Transport status describes the request boundary. For example, an HTTP request
may return status `200`, or an internal call may return `ok`. That tells us the
request completed at the transport layer. It does not tell us that the returned
context was usable, that the answer was relevant, or that an authorized state
change occurred.

Semantic outcome describes whether the task reached its declared goal. In this
lab, the synthetic task expects usable context. The naive path receives an
`ok` transport result with empty context. It treats that response as progress,
retries, and eventually exceeds its synthetic retry and cost boundaries.

The guarded path makes the missing evidence explicit. It records that the
transport succeeded but the semantic result is not usable. It stops rather than
turning an empty result into another apparently successful attempt, and it
escalates to a human approver.

Notice what the lab does not do. It does not call Claude. It does not claim to
measure live model quality. That is intentional. Before we add a model to the
loop, we want the evaluation contract to catch a failure we already understand.
An offline negative control is cheaper and easier to inspect than a live
experiment whose result is ambiguous.

Run the lab from the course repository:

```bash
uv run python labs/01-semantic-outcomes/run_lab.py
```

Look at six fields: transport status, semantic outcome, retry count, estimated
cost, finding status, and missing evidence.

The important comparison is not just that the guarded path is labeled
“completed.” It is that both paths show transport status `ok`, while the
semantic evaluation distinguishes the empty context from usable evidence.

This pattern generalizes. A model response can be valid JSON but contain the
wrong answer. A tool call can match the schema but target the wrong account. An
agent can reach a plausible final message after an unauthorized intermediate
step. The evaluation must inspect the property that matters to the decision.

For your own workflow, identify the first observable signal that says the task
is actually progressing. If that signal is absent, the correct action may be
clarification, refusal, retry, or escalation. It is not automatically success.

In the next lesson, we will name those terminal states and define the evidence
required before a result can move from observation to decision.

## Demo notes

Run the wrapper from the course repository. Read the JSON output and compare the
`naive` and `guarded` objects. Point out that the guarded path has no missing
evidence, while the naive path reports missing task-outcome and usage evidence.

Do not imply that `finding_status: completed` means the underlying task was
successful. In this scenario it means the evaluation completed its declared
guarded decision and escalated appropriately.

## Learner practice

Change the example in your notes: replace “empty context” with one failure from
your own system. What evidence would distinguish transport success from task
success?

## What this lesson does not prove

The synthetic lab proves only the declared behavior of this scenario and its
evaluation control. It does not establish live Claude quality or production
observability.
