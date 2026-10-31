# Lab 5: Turn evaluation evidence into a release decision 🔬

This lab is the course capstone. It connects benchmark interpretation, a
controlled baseline-versus-variant comparison, uncertainty, revision binding,
rollback, monitoring, and a decision report.

## What you will learn

You will compare two synthetic revisions on the same cases, inspect a high-risk
slice, measure repeated-run variation, explain benchmark limitations, rehearse
rollback, and produce a bounded release recommendation.

## Why this matters

A variant can improve the overall score while making a high-risk case worse.
Old evidence can also look reusable after a policy, model, tool, or evaluator
revision changes. A release decision must preserve the case set, revisions,
findings, limitations, owner, and recovery action.

## Starting state

The lab is self-contained and uses public synthetic data only. It does not call
Claude, the network, a benchmark provider, or a deployment system.

The baseline and variant use the same six cases and evaluator revision. Only the
policy revision changes. The variant improves the aggregate score but regresses
the high-risk slice, so the correct capstone decision is `hold`.

## Run it

From the repository root:

```bash
uv run python labs/05-release-capstone/run_lab.py
```

To save the synthetic capstone report:

```bash
uv run python labs/05-release-capstone/run_lab.py \
  --output /tmp/claude-evaluation-capstone.json
```

To inspect the comparison cases:

```bash
uv run python labs/05-release-capstone/run_lab.py --show-cases
```

## Expected result

The report should show:

- the baseline and variant share a case set and evaluator revision;
- only the policy revision changes;
- the variant has a higher aggregate score;
- the variant has a lower high-risk slice score;
- repeated runs show non-zero score variation;
- each repeated run identifies the failed case IDs that produced its score;
- revision change requires a rerun rather than reusing old evidence;
- task correctness and safety remain separate dimensions;
- latency, cost, user outcomes, and evaluator validity are marked
  `not_evaluated` rather than invented;
- rollback rehearsal passes without deployment writes;
- monitoring includes an owner and action threshold; and
- human approval remains pending and separate from the automated result; and
- the capstone decision is `hold`, with the action `do not release variant-r2`.

The lab should exit with code `0`. The zero exit code means the release controls
behaved as expected; it does not approve a real release.

## Workflow map

```text
baseline + variant
        |
        v
matched cases and fixed evaluator
        |
        +--> aggregate comparison
        +--> high-risk slices
        +--> repeated-run uncertainty
        +--> revision-impact check
        |
        v
release decision
   /       |       \
release   hold   rollback
   |        |       |
monitor   revise   restore last-known-good
```

## Evidence to inspect

Review these fields in the JSON output:

- `revisions`
- `comparison.baseline_score`
- `comparison.variant_score`
- `comparison.variant_score_range`
- `comparison.high_risk_regression`
- `negative_controls`
- `release_contract`
- `dimensions`
- `uncertainty`
- `rollback_rehearsal`
- `monitoring_plan`
- `capstone_report`

The key observation is that the aggregate improvement does not override the
high-risk slice regression. The report keeps both facts visible.

## Try the failure

The lab plants two release hazards:

1. the variant improves the overall score but regresses a high-risk case; and
2. the policy revision changes while older evidence remains tied to the
   baseline policy.

The controls must catch both. The first causes a hold. The second requires a
rerun against the changed revision.

## Troubleshooting

1. Confirm that you are running the command from the course repository root.
2. Confirm that `uv` is installed with `uv --version`.
3. If an assertion fails after editing cases, inspect the baseline and variant
   revision dictionaries and the high-risk slice values.
4. The rollback rehearsal is metadata-only; it does not deploy, delete, or
   modify a real system.

## Evidence template

Copy this structure into your own notes:

```text
decision_target:
report_vocabulary_revision:
case_set_revision:
evaluator_revision:
baseline_revision:
variant_revision:
changed_fields:
release_contract:
aggregate_result:
high_risk_slice_result:
uncertainty:
dimensions:
benchmark_limitations:
blocking_findings:
rollback_trigger:
rollback_owner:
monitoring_signal:
human_approval_state:
release_decision:
next_step:
```

## What this does not prove

This is an offline synthetic teaching control. It does not establish live model
quality, benchmark ranking, production drift, rollback speed, or safety outside
the declared cases.

## Optional extension

Change one of the normal cases so the variant improves the aggregate score
without changing the high-risk slice. Then compare that result with the current
hold decision and document what additional evidence would be needed before
release.

For the harness-side patterns behind this lab, see the public
[benchmark reporting tool](https://github.com/julie-elkins/agent-assurance-harness/blob/main/tools/benchmark_report.py),
[change-impact example](https://github.com/julie-elkins/agent-assurance-harness/tree/main/examples/change-impact),
[rollback rehearsal](https://github.com/julie-elkins/agent-assurance-harness/blob/main/tools/rollback_rehearsal.py),
and [run-manifest examples](https://github.com/julie-elkins/agent-assurance-harness/tree/main/examples/run-manifest).

For the shared status meanings behind the report, see the
[Agent Systems Design Guide vocabulary](https://github.com/julie-elkins/agent-systems-design-guide/blob/main/REPORT_VOCABULARY.md).
For a native platform implementation, compare the
[Apple Platform Agent Quality Lab](https://github.com/julie-elkins/apple-platform-agent-quality-lab).
