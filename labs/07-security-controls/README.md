# Lab 7: Test the agent security boundary 🛡️

This lab teaches security as a set of observable controls around an agent:
trust boundaries, identity, least privilege, tenant scope, network egress,
output validation, approval, telemetry access, audit evidence, red-team
detection, and bounded stopping.

The fixtures are synthetic and harmless. No credentials, live endpoints, raw
provider payloads, or production data are used.

## What you will learn

You will inspect:

- trust-boundary and threat-model evidence;
- principal, resource scope, action scope, and approval;
- credential exposure and secret boundaries;
- tenant and network egress policy;
- output validation before a side effect;
- tool and dependency provenance;
- domain-source ownership, freshness, and missing-data behavior;
- telemetry access, retention, deletion, and audit evidence; and
- idempotency and stale-state controls;
- red-team cases that connect an attack hypothesis to an expected control and
  regression case; and
- resource-budget and stopping controls.

## Run it

From the repository root:

```bash
uv run python labs/07-security-controls/run_lab.py
```

To save a local report:

```bash
uv run python labs/07-security-controls/run_lab.py --output /tmp/security-report.json
```

## Expected result

The suite should pass because it catches planted failures. The candidate release
decision should be `block` because the synthetic set contains unauthorized,
cross-tenant, secret-exposure, unsafe-output, provenance, and missing-approval
cases.

## Workflow map

```text
asset and actor
      |
      v
trust boundary ---> identity and least privilege
      |                    |
      v                    v
data and network ---> validated side effect
      |
      v
telemetry privacy ---> audit and response
```

## Evidence to inspect

Review:

- `control_results`
- `case_results`
- `negative_controls`
- `incident_findings`
- `red_team_cases`
- `coverage_summary`
- `candidate_release_decision`
- `evidence_template`

## Domain evidence extension

After the automated controls pass, create a small synthetic source contract for
one decision. Use three records:

1. a public course description;
2. an original learner answer; and
3. an AI-generated “understood” label.

Record the source owner, permitted purpose, provenance (where the evidence came
from), freshness, retention, and missing-data behavior. Keep the original answer
separate from the model label. If the answer is missing or conflicts with the
label, mark the decision `not_evaluated` or route it for human review rather
than treating the label as ground truth (a trusted reference for correctness).

This is a learner exercise over synthetic records; it is not a live learner
analytics integration and does not require private data.

## What this does not prove

The lab proves that the evaluator catches the declared synthetic control
failures and records a small red-team coverage map. It does not prove that an
identity provider, secret store, network gateway, validator, telemetry backend,
or deployed agent resists new attack patterns.

## Red-team workflow

For each synthetic red-team case, inspect:

1. the attack type and entry point;
2. the expected preventive or detective control;
3. the observed status and evidence;
4. the regression case identifier; and
5. the release consequence.

A blocked synthetic attack is evidence that the declared control was exercised.
An unblocked attack is a regression finding. Neither result is a universal
safety score.

> 🧭 **Take this forward**
>
> **Remember:** evaluate the harness around an agent—tools, permissions,
> policies, state, and evidence—not only the underlying model.
>
> **Try next:** name the authorization owner and the independent record holder
> for one consequential action.
>
> **Inspect:** the control result, authorization evidence, evidence source, and
> whether the executor could rewrite the record being used for the decision.
>
> **Do not infer:** a public incident report or a blocked synthetic attack is
> telemetry-backed proof of universal safety.

## Optional extension

Map each synthetic control to a real service boundary in a system you are
authorized to inspect. Do not copy credentials, private payloads, or private
logs into the course repository.
