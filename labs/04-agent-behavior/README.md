# Lab 4: Evaluate the path, not only the final answer 🔬

This lab teaches agent-behavior evaluation. An agent trajectory is the ordered
sequence of observations, decisions, tool calls, results, and recovery steps
that produces an outcome.

## What you will learn

You will evaluate:

- claim-level factuality;
- safe refusal and prompt-injection resistance;
- tool routing;
- tool-argument correctness;
- before-and-after state; and
- recovery to a valid terminal state.

Each area has a synthetic positive case and a deliberately degraded case that
the evaluator should catch.

## Why this matters

A final answer can sound correct while the claims are unsupported, the unsafe
request was not refused, the wrong tool was selected, the tool targeted the
wrong resource, or the expected state change never happened. Evaluating only the
final text hides the path that created the risk.

## Starting state

The lab is self-contained and uses public synthetic data only. It does not call
Claude, the network, or a provider API. The case inventory models a bounded
agent task with claims, safety boundaries, tools, and state transitions.

## Run it

From the repository root:

```bash
uv run python labs/04-agent-behavior/run_lab.py
```

To inspect the synthetic cases:

```bash
uv run python labs/04-agent-behavior/run_lab.py --show-cases
```

## Expected result

The summary should show:

- supported claims passing and an unsupported high-risk claim failing;
- an unsafe request without refusal being caught;
- a refused request without an explained boundary or safe redirect being caught;
- a followed prompt injection being caught;
- a missed tool and wrong tool arguments being caught;
- an unauthorized tool call being caught;
- a missing state transition being caught;
- a trajectory that reaches the expected state through an unauthorized tool
  being caught; and
- a recovered trajectory passing; and
- `evaluator_suite_status: "passed"` with
  `candidate_release_decision: "block"`.

The evaluator suite passes because it catches the planted failures. The
candidate decision is blocked because the synthetic agent behavior contains
failures that must be fixed before release.

## Workflow map

```text
claims -----> factuality check --------\
request ----> safety boundary ----------\
task -------> tool routing -------------> findings
tool call --> arguments and authority --/
state ------> before/after assertion ---/
trace ------> recovery and terminal state
                         |
                         v
                 release or block
```

## Evidence to inspect

Review these fields in the JSON output:

- `evaluator_revision`
- `case_results`
- `negative_controls`
- `evaluator_suite_status`
- `candidate_release_decision`
- `evidence_template`

Within each case result, inspect the `reason_code` and the evidence-specific
details. The same final answer can be acceptable or unacceptable depending on
whether its claims, tools, authorization, and state evidence support it.
Claim results retain evidence identifiers so a reviewer can trace a finding back
to an evidence artifact rather than trusting only a status label.

## Try the failure

The deliberately degraded cases include:

- `factuality-unsupported-001`: an unsupported high-risk claim;
- `unsafe-refusal-missed-001`: an unsafe request that was not refused;
- `prompt-injection-followed-001`: an untrusted instruction was followed;
- `tool-routing-missed-001`: the required tool was not selected;
- `tool-arguments-wrong-target-001`: the selected tool received semantically
  wrong arguments;
- `tool-unauthorized-001`: the selected tool was outside the allowed authority;
- `state-change-missing-001`: the tool returned but the expected state did not
  change.
- `unsafe-refusal-unhelpful-001`: the request was refused without an explained
  boundary or safe redirect.
- `trajectory-unauthorized-tool-001`: the final state looks correct, but the
  path used an unauthorized tool.

The evaluator must catch all of them. `trajectory-recovery-001` demonstrates
that recovery is more than retrying: the path ends in the expected verified
state.

## Troubleshooting

1. Confirm that you are running the command from the course repository root.
2. Confirm that `uv` is installed with `uv --version`.
3. If an assertion fails after editing a case, compare its
   `expected_decision` with the evaluator category and reason code.
4. Keep state identifiers synthetic; the lab must not connect to a live account
   or tool.

## Evidence template

Copy this structure into your own notes:

```text
decision:
evaluator_revision:
case_ids:
claim_findings:
claim_evidence_ids:
safety_findings:
tool_findings:
state_and_trajectory_findings:
negative_controls_caught:
human_review_required:
candidate_release_decision:
limitations:
```

## What this does not prove

This is an offline synthetic teaching control. It does not establish live Claude
factuality or safety, broad prompt-injection resistance, production tool
authorization, or real-world state correctness.

## Optional extension

Add one case where evidence is ambiguous rather than unsupported, and make the
expected outcome `escalate` instead of `fail`. Then add one case where a tool
call is authorized and schema-valid but targets the wrong tenant or location.

For the harness-side patterns behind this lab, see the public
[content-assurance implementation](https://github.com/julie-elkins/agent-assurance-harness/blob/main/src/agent_reliability_lab/content_assurance.py),
[scenario registry](https://github.com/julie-elkins/agent-assurance-harness/blob/main/src/agent_reliability_lab/scenarios.py),
and [agent-workflow teaching lab](https://github.com/julie-elkins/agent-assurance-harness/tree/main/examples/agent-workflow-teaching-lab).
