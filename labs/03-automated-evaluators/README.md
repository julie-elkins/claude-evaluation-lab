# Lab 3: Layer the evaluator before you trust the judge 🔬

This lab teaches evaluator composition. An evaluator is a rule, program, model,
or human process that turns observed behavior into a finding. The lab shows why
one evaluator should not be allowed to hide another evaluator's failure.

## What you will learn

You will run three offline evaluator layers:

- a deterministic contract check for structured output;
- a synthetic judge that returns parseable JSON but can still be wrong; and
- an independent semantic check that verifies completion evidence.

You will also run a pairwise bias probe, where the same candidates are shown in
opposite orders to detect whether the judge changes its preference.

## Why this matters

A structured evaluator response can be valid JSON and still contain the wrong
decision. A judge can produce a convincing score while missing unsupported
evidence. A pairwise comparison can select a different winner when answer order
changes. If these failures are collapsed into one score, the release decision
can look cleaner than the evidence allows.

## Starting state

The lab is self-contained and uses only public synthetic data. It does not call
Claude, the network, or a provider API. The judge is a deterministic teaching
stub, not a live LLM-as-a-judge system.

The case set includes:

- a supported completion;
- malformed evaluator output;
- a fluent completion claim without evidence; and
- a safe escalation without a completion claim.

## Run it

From the repository root:

```bash
uv run python labs/03-automated-evaluators/run_lab.py
```

To inspect the synthetic cases:

```bash
uv run python labs/03-automated-evaluators/run_lab.py --show-cases
```

## Expected result

The summary should show:

- `malformed-001` caught by the deterministic contract layer;
- `unsupported-001` passed by the synthetic judge but caught by the independent
  semantic check;
- `position_bias_detected: true` after the pairwise order is reversed; and
- `release_decision: "block"` because the evaluator stack has known failures.

The lab should exit with code `0`. The zero exit code means the teaching
assertions passed; it does not mean a live judge is accurate.

## Workflow map

```text
observed response
        |
        +--> deterministic contract check
        |
        +--> structured judge output --> parseability check
        |
        +--> independent evidence check
        |
        +--> pairwise order probe
                    |
                    v
             layered decision
```

## Evidence to inspect

Review these fields in the JSON output:

- `evaluator_layers`
- `case_results`
- `contract_failures`
- `judge_false_passes`
- `negative_control`
- `bias_probe`
- `release_decision`
- `release_reasons`

The key observation is that the judge result and the independent semantic
result are stored separately. A parseable `pass` is not allowed to overwrite an
independent `fail`.

## Try the failure

The negative control is `unsupported-001`. Its response claims completion
without evidence. The synthetic judge gives it a parseable pass because it
rewards fluent completion language. The independent semantic check returns
`fail`, exposing the judge false pass.

The malformed case is a separate failure. It does not reach semantic
interpretation because the deterministic contract layer cannot parse it safely.

The pairwise probe uses a seeded position-biased judge. It always prefers the
first presented candidate, so reversing the order changes the preferred
candidate. The correct action is to reject that judge as a release gate until
the bias is understood and controlled.

## Troubleshooting

1. Confirm that you are running the command from the course repository root.
2. Confirm that `uv` is installed with `uv --version`.
3. If an assertion fails after editing the cases, inspect the expected
   `contract_failures`, `judge_false_passes`, and `bias_probe` values before
   changing the evaluator.
4. Remember that this lab intentionally uses a deterministic judge stub; no
   Claude API key is needed.

## Evidence template

Copy this structure into your own notes:

```text
decision:
evaluator_revision:
case_set_revision:
contract_failures:
judge_false_passes:
independent_breaker_result:
pairwise_order_1:
pairwise_order_2:
bias_detected:
release_decision:
release_reasons:
limitations:
```

## What this does not prove

This is an offline synthetic teaching control. It does not establish live
LLM-as-a-judge accuracy, broad bias resistance, human agreement, production
monitoring, or release readiness.

## Optional extension

Replace the deterministic judge stub with a live Claude judge only after adding
explicit request, time, token, and spend limits. Preserve the deterministic
contract layer and independent semantic check so the live judge remains one
layer in the evaluation rather than becoming the release authority.

For the harness-side evaluator-validity pattern, see the public
[evaluator implementation](https://github.com/julie-elkins/agent-assurance-harness/blob/main/src/agent_reliability_lab/evaluators.py)
and its [evaluation checklist](https://github.com/julie-elkins/agent-assurance-harness/blob/main/AGENT_EVALUATION_CHECKLIST.md).
