# Lesson 24: Tool Arguments, Context, and State

Module: 4 — Factuality, Safety, and Agent Behavior
Suggested runtime: 12–15 minutes
Primary lab: Validate arguments and before/after state

## Learner objective

By the end of this lesson, you can evaluate whether a selected tool received the right arguments, context, authorization, and state transition.

## Slide and recording plan

1. **A valid call can still be wrong** — schema validity versus task correctness.
2. **Argument checks** — types, ranges, identity, location, and scope.
3. **Context, memory, and state** — what the agent knew, retained, and changed.
4. **Environment control** — reset or version state between cases.
5. **Demo: inspect a tool-call trace**.
6. **Practice: define before/after state assertions**.

## Speaker script

Tool selection is only the first decision. The agent must also provide arguments that are valid for the task, not merely valid for the schema. A syntactically valid account identifier can still refer to the wrong account. A valid location can still be outside the user’s authorization. A valid quantity can still exceed the allowed limit.

Check argument correctness at the level of the decision. Record the intended entity, location, scope, time, and authorization. Then compare those values with the actual tool call. Schema validation catches missing fields and wrong types; semantic argument checks catch the wrong target or unsafe scope.

Context matters because the same argument can mean different things in different sessions. Capture the relevant context the agent was allowed to use and the context it actually used. If a required location, identity, or previous approval is missing, the correct outcome may be escalation rather than guessing.

State matters because the agent may claim success without changing the expected system state. Record the state before the call, the requested transition, the tool result, and the state after the call. A successful response from the tool is not proof that the intended transition occurred.

Memory is part of state. Evaluate whether the agent wrote the right information,
retrieved the right information later, and handled stale or conflicting memory.
Reset or version the environment between cases so that one learner exercise
does not silently change the evidence for the next one.

In the demo, inspect a synthetic trace where the tool call passes schema validation but targets the wrong location. Then inspect a trace where the argument is correct but the expected state change is absent. These are different findings and require different fixes.

The cost of checking only the schema is dangerous precision: the system reports a valid call while performing the wrong action. The cost of ignoring state is false completion: the agent says the work is done when the system remains unchanged.

## Demo notes

- Use a synthetic tool with explicit before/after state.
- Show schema validation, semantic argument validation, authorization, and state assertion separately.
- Keep all identifiers fictional and deterministic.
- Recording boundary: do not connect the lab to a live account or production system.

## Learner practice

For one synthetic tool call, define:

`intended_target`, `authorized_scope`, `required_context`, `memory_before`,
`memory_after`, `environment_revision`, `expected_before_state`,
`expected_after_state`.

Create one passing trace and one trace that is schema-valid but semantically wrong.

## What this lesson does not prove

State assertions can miss delayed, partial, or externally caused changes. The evaluation needs a clear observation window and an escalation path for uncertain state.
