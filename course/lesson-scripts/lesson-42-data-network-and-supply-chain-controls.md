# Lesson 42: Data, Network, and Supply-Chain Controls

Module: 10 — Security and assurance controls
Suggested runtime: 12–15 minutes
Primary lab: Lab 7 — Test the agent security boundary

## Learner objective

By the end of this lesson, you can evaluate data boundaries, network egress,
output validation, and dependency or tool provenance as separate controls.

## Slide and recording plan

1. **Data boundary** — tenant, classification, and purpose.
2. **Network boundary** — approved destinations and egress policy.
3. **Output boundary** — validate before a downstream side effect.
4. **Supply-chain boundary** — record tool and dependency revisions.
5. **Demo: inspect planted Lab 7 security failures**.

## Speaker script

A data boundary answers which information this run may read, transform, or
return. Tenant isolation is an explicit check: a successful lookup in the wrong
tenant is a security failure, not a useful result.

Network egress is another boundary. A tool should have an approved destination,
method, and purpose. The fact that a URL is reachable does not make it an
authorized destination. Test denied destinations and unexpected redirects with
synthetic names.

Output validation is the control between model text and a side effect. Parse the
structure, validate the values, check authorization, and apply idempotency or
approval before writing. A syntactically valid output can still request a
dangerous or duplicate action.

Supply-chain evidence includes the tool definition revision, dependency
revision, model revision, and policy revision. Without those identities, a
failure may be impossible to reproduce.

## Demo notes

- Review Lab 7 tenant, egress, output-validation, and provenance findings.
- Keep all destinations and identifiers synthetic.

## Learner practice

Choose one tool and define its allowed tenant, network destination, output
schema, tool revision, and dependency revision.

## What this lesson does not prove

Recording a policy field does not prove that a network gateway, validator, or
dependency scanner enforced it.
