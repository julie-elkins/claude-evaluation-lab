# Lab 1: Transport success is not task success 🔬

This lab teaches semantic outcome evaluation. Semantic outcome means whether the
requested task actually reached its declared goal; it is separate from
transport status, which only says whether a request returned successfully.

## What you will learn

You will compare a naive workflow with a guarded workflow. Both receive a
synthetic transport response with status `ok`, but only the guarded workflow
checks whether the returned context is usable before continuing.

## Why this matters

If an evaluator treats `HTTP 200` or another successful request status as proof
that the task worked, an empty or incomplete result can be reported as a pass.
That can hide wasted retries, missing evidence, or an unsafe downstream action.

## Starting state

The runnable behavior lives in the public Agent Assurance Harness. The course
wrapper does not copy the harness implementation; it checks out or locates the
declared harness revision and runs the existing teaching lab.

## Run it

From this repository:

```bash
uv run python labs/01-semantic-outcomes/run_lab.py
```

You can provide a different local harness checkout explicitly:

```bash
uv run python labs/01-semantic-outcomes/run_lab.py \
  --harness-root ../agent-assurance-harness
```

## Expected result

The output should show:

- both paths with transport status `ok`;
- the naive path ending in a failed evaluation;
- the guarded path ending in a completed evaluation;
- the naive path exceeding its synthetic retry or cost boundary; and
- human approval remaining outside the automated result.

The wrapper also prints the harness revision used for the lab.

## Workflow map

```text
synthetic request
       |
       v
bounded executor
       |
       v
transport status: ok
       |
       v
semantic outcome check
    /             \
usable context   empty context
    |                 |
complete        stop and escalate
```

## Evidence to inspect

Compare these fields in the JSON output:

- `transport_status`
- `semantic_outcome`
- `retry_count`
- `estimated_cost_usd`
- `finding_status`
- `missing_evidence`

The key observation is that transport success appears in both paths. The
semantic evaluation separates the two.

## Try the failure

Read the naive path as a deliberately degraded control. It treats repeated
transport success as progress even though the context remains empty. The lab
should catch that behavior rather than allowing a green-looking result.

## Troubleshooting

1. Confirm that `uv` is installed.
2. Confirm that the harness checkout exists beside this repository or pass
   `--harness-root`.
3. Confirm that the harness is at the pinned revision shown by the wrapper.
4. Run the underlying harness lab directly from its repository root if you need
   to separate course setup problems from harness behavior.

## What this does not prove

This is an offline synthetic teaching control. It does not establish live
Claude quality, production observability, business impact, or the correctness
of a workflow outside this declared scenario.

## Optional extension

Write down one evaluation in your own system that currently treats a successful
request as proof of task completion. Name the evidence that would be required
to distinguish transport success from semantic success.
