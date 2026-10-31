# Lab 2: Build a case set before you trust the score 🔬

This lab teaches evaluation-case design. An evaluation case is one test
situation with its input, expected behavior, observed result, evidence, and
decision consequence.

## What you will learn

You will create and inspect a small synthetic case set with golden cases,
calibration cases, and held-out cases. You will apply a rubric, compare two
reviewers, resolve a seeded disagreement, and verify that a deliberately
degraded case is caught.

## Why this matters

If the cases are not representative, the score can be precise but irrelevant.
If calibration cases leak into the held-out set, the result can look better
than it is. If a negative control passes, the evaluator is not proving the
failure it claims to measure.

## Starting state

The lab is self-contained and uses only public synthetic data. It does not call
Claude, the network, or a provider API. The case set models one decision:

> Do not report task completion when completion evidence is missing.

The lab uses three data roles:

- **Golden** cases establish trusted examples for the rubric.
- **Calibration** cases help reviewers align their interpretation.
- **Held-out** cases measure the rubric after calibration without tuning on those
  cases.

For the harness-side pattern behind this lab, see the public [evaluation
checklist](https://github.com/julie-elkins/agent-assurance-harness/blob/main/AGENT_EVALUATION_CHECKLIST.md)
and its [monitorability example](https://github.com/julie-elkins/agent-assurance-harness/tree/main/examples/monitorability).

## Run it

From the repository root:

```bash
uv run python labs/02-case-design/run_lab.py
```

To inspect the synthetic case inventory:

```bash
uv run python labs/02-case-design/run_lab.py --show-cases
```

## Expected result

The summary should show:

- 8 total cases split into golden, calibration, and held-out roles;
- one seeded calibration disagreement;
- raw agreement below 1.0 before the rubric boundary is clarified;
- no overlap between calibration and held-out case IDs;
- the robust evaluator classifying every held-out case correctly;
- the robust evaluator catching `held-out-negative-001`; and
- the weak evaluator missing that negative control because it ignores evidence.

The lab should exit with code `0`. The zero exit code means the lab assertions
passed; it does not mean a real system is ready for release.

## Workflow map

```text
synthetic case inventory
          |
          v
golden examples ---> rubric
                          |
calibration cases ---> reviewer agreement ---> clarify boundary
                          |
held-out cases ------> final measurement ---> catch negative control
```

## Evidence to inspect

Review these fields in the JSON output:

- `split_counts`
- `rubric.revision`
- `calibration.raw_agreement`
- `calibration.disagreements`
- `leakage_check`
- `held_out.robust_results`
- `held_out.negative_control`
- `evidence_template`

The key observation is that the held-out result is not read until the seeded
calibration disagreement is made explicit and the split-overlap check passes.

## Try the failure

The negative control is `held-out-negative-001`. It claims completion without
evidence. The robust evaluator must return `fail`; the intentionally weak
evaluator must miss it. This is a negative control, meaning a deliberately bad
case that checks whether the evaluator can detect the failure it claims to
measure.

The lab also plants a reviewer disagreement on
`calibration-boundary-001`. The response says the task is ready for review, not
that it is complete. The disagreement is resolved by clarifying that review
readiness is not a completion claim.

## Troubleshooting

1. Confirm that you are running the command from the course repository root.
2. Confirm that `uv` is installed with `uv --version`.
3. If Python reports a syntax error, confirm that the repository is using
   Python 3.11 or newer.
4. If the assertions fail after you edit the cases, inspect the expected labels,
   split IDs, and seeded disagreement before changing the evaluator.

## Evidence template

Copy this structure into your own notes:

```text
decision:
case_set_revision:
rubric_revision:
golden_case_ids:
calibration_case_ids:
held_out_case_ids:
reviewer_ids:
raw_agreement:
disagreements:
disagreement_action:
negative_control_id:
negative_control_caught:
limitations:
```

## What this does not prove

This is an offline synthetic teaching control. It does not establish live Claude
quality, agreement among real reviewers, coverage of your production case
distribution, or the correctness of a release threshold.

## Optional extension

Copy the case inventory into your own project and add:

1. one conflicting-evidence case;
2. one unauthorized-action case; and
3. one recovery case.

Keep the new cases in a separate local file and add a split-overlap assertion
before using them as held-out evidence.
