# Optional extension 🔬: Evaluate background memory consolidation

**Memory consolidation** is a background workflow that reads prior agent
sessions and writes a smaller, reusable representation for a later session.
Some systems describe this as “dreaming.” It is a state-changing workflow, not
an automatic quality improvement.

Use this extension after Lessons 24, 25, 32, 35, 37, and 46. It is optional
because the required course path remains offline, deterministic, and
provider-neutral.

## Why this needs its own evaluation

An agent can appear to improve because it remembers something useful. It can
also become less reliable because it remembered something stale, private,
contradictory, or irrelevant. The memory writer and the later agent therefore
form one stateful evaluation boundary.

The decision is not:

> Did the background job produce a plausible summary?

The decision is:

> Does the memory change improve the declared future workflow without creating
> unsafe state, privacy exposure, stale guidance, or unbounded cost?

## Compare a baseline with a treatment

Run the same task set under two conditions:

| Condition | Memory behavior | Purpose |
|---|---|---|
| Baseline | No newly consolidated memory, or the previous approved memory snapshot | Establishes what the agent can do without the candidate change |
| Treatment | The candidate consolidation workflow reads approved prior sessions and writes a versioned memory snapshot | Measures the effect of the change |

Keep the agent, task set, policy, tools, model revision, and environment
constant unless the decision explicitly concerns one of those changes. Use
fresh and held-out cases, meaning cases not used to design the consolidation
prompt or tune the memory schema.

Do not treat the memory writer's completion status as evidence that future
tasks improved. The later task is the unit that supplies that evidence.

## Evaluation surfaces

Evaluate the memory workflow at four connected surfaces:

1. **Write correctness** — did it store only information that was eligible,
   supported, and useful?
2. **Read correctness** — did the later agent retrieve the right memory for the
   task and ignore irrelevant memory?
3. **Task outcome** — did the later workflow complete the declared task more
   reliably?
4. **State safety** — did the change preserve authorization, privacy,
   tenant boundaries, retention, deletion, provenance, and rollback?

Useful observations include:

- task completion and semantic outcome;
- memory retrieval precision and recall;
- stale-memory rate;
- contradiction rate;
- unsupported-memory rate;
- unwanted personalization or cross-user leakage;
- memory write and read latency;
- token and storage cost;
- memory version and provenance;
- expiry, deletion, and rollback behavior; and
- human-review or escalation rate for ambiguous memory.

These are separate dimensions. A lower token cost does not compensate for
cross-tenant memory leakage, and a higher task-success rate does not prove that
the memory is safe to retain.

## Safety and privacy contract

Before running the treatment, declare:

- which transcripts or events may be read;
- which data classes must be redacted or excluded;
- who may write, read, correct, or delete memory;
- how memory is isolated by user, tenant, workflow, and environment;
- how each memory item points to bounded provenance;
- how stale or conflicting memory is detected;
- when memory expires;
- how a deletion request removes or invalidates derived memory;
- how an approved snapshot is rolled back; and
- what happens when the evidence is missing or ambiguous.

The public course uses synthetic identifiers and memory states only. Do not put
raw transcripts, personal data, credentials, or provider responses into the
repository.

## Negative controls

Add deliberately degraded cases that the evaluation must catch:

- a memory item with an expired source;
- a memory item copied across tenants;
- a memory item that contradicts the current policy;
- a memory item that contains unsupported personal information;
- a relevant memory item that is not retrieved;
- an irrelevant memory item that is retrieved and changes the plan;
- a deletion request that leaves derived state active; and
- a treatment that improves the aggregate score while regressing a high-risk
  held-out slice.

If these controls are not caught, the evaluation is not ready to support a
release decision.

## Optional exercise 🧪

Choose one synthetic workflow and write four lines:

1. The baseline condition is…
2. The treatment changes…
3. The most expensive plausible memory failure is…
4. The evidence that would justify adoption is…

Then define one held-out case and one deletion or rollback check. Report
whether the result is `completed`, `failed`, `blocked`, or
`not_evaluated`—and explain why.

## What this extension does not prove ⚠️

One controlled comparison does not prove that memory improves every task,
every user experience, or every future model revision. A cookbook example,
runtime, or reported cost is not a production guarantee. Re-run the comparison
when the memory schema, writer workflow, model, policy, data boundary, or
retrieval mechanism changes.

## Official reference

The [Anthropic Claude Cookbook example on dreaming with a dynamic
workflow](https://platform.claude.com/cookbook/managed-agents-cma-dreaming-with-a-dynamic-workflow)
is an implementation reference for a background memory workflow. Use it to
study the pattern, not as evidence that the pattern is safe or beneficial for
every use case.
