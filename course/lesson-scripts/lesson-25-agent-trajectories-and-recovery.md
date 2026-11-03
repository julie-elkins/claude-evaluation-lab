# Lesson 25: Agent Trajectories and Recovery

Module: 4 — Factuality, Safety, and Agent Behavior
Suggested runtime: 12–15 minutes
Primary lab: Inspect a multi-step trajectory and recovery outcome

## Learner objective

By the end of this lesson, you can evaluate an agent trajectory, meaning the sequence of observations, decisions, tool calls, results, and recovery steps that produces the final outcome.

## Slide and recording plan

1. **The final answer is not the whole run** — observe, plan, act, recover.
2. **The environment is part of the trajectory** — tools, context, memory, policy, and state.
3. **Trajectory evidence** — decisions, tools, arguments, state, and terminal outcome.
4. **Evaluation scope** — step, end-to-end, trajectory, and thread/session.
5. **Recovery versus retry** — a retry is not recovery unless the failure is addressed.
6. **Flat versus multi-agent architecture** — compare the whole task, not isolated subagents.
7. **Stopping criteria** — define when the run completes, refuses, fails, or escalates.
8. **Demo: guarded and unguarded paths**.
9. **Practice: annotate a trajectory and choose the final decision**.

## Speaker script

An agent trajectory is the ordered sequence of what the agent observed, decided, attempted, and recovered from. The final answer is only one view of that sequence. Two agents can produce the same final wording while one used an authorized path and the other made an unsafe or unsupported detour.

Record the environment alongside the trajectory: available tools, relevant
context and memory, policy revision, permissions, and state revision. Also
declare the stopping criteria before the run. Without those boundaries, a
trajectory cannot be compared fairly with another run, and a premature stop can
look like successful completion.

Evaluate the trajectory in stages: observation, planning, action, result, and recovery. Record which evidence was available at each stage, which tool was selected, what arguments were sent, how the result changed the next step, and whether the agent reached a valid terminal state.

Choose the evaluation scope deliberately. A step or unit evaluation checks one
model call, tool call, retrieval result, or state transition. An end-to-end
evaluation checks the complete task outcome. A trajectory evaluation checks the
ordered path. A thread or session evaluation groups multiple turns into one
continuing conversation or workflow session.

Thread-level evaluation matters when state persists across turns. Check whether
the agent remembers an earlier constraint, preserves authorization, handles
conflicting or stale memory, avoids repeating a side effect, and reaches a
conversation-level terminal state. One turn can look correct while the thread
fails because an earlier error contaminates later decisions.

Distinguish retry from recovery. A retry repeats an attempt. Recovery changes the plan or escalates because the previous attempt failed. Repeated retries can waste budget, duplicate side effects, or hide the fact that the agent has no safe next step.

Architecture is also part of the trajectory. A **subagent** is a secondary
agent invoked by a primary agent for specialized work. Compare a flat agent
with a subagent design at the end-to-end task level: did the user get the
expected outcome, were the tools and permissions correct, was the context
managed safely, and did the extra handoff improve the result enough to justify
its cost and latency? A subagent can look successful in isolation while the
primary agent still loses state, misroutes the result, or fails to complete the
user's task.

After a model upgrade, re-evaluate the architecture rather than assuming that
an old subagent remains useful. A stronger model may make a specialized
subagent, prompt branch, or context workaround unnecessary. Keep a subagent
when it provides a measured benefit such as parallel research, independent
verification, or a genuinely different context boundary. The decision belongs
to the end-to-end evidence, not to the existence of a polished subagent answer.

The final decision should include both the semantic outcome and the process findings. A run that reaches the right answer through an unauthorized tool may still fail. A run that safely escalates because evidence is missing may be the correct outcome even though it does not complete the original task.

In the demo, compare the guarded and unguarded semantic-outcomes paths. Inspect transport status, semantic outcome, missing evidence, retry count, approval requirement, and terminal state. The point is to show how the evidence contract keeps the final decision tied to the actual run.

The cost of evaluating only final answers is that process failures disappear. That matters most for agents, because the path can create side effects even when the final text looks acceptable.

## Demo notes

- Run `labs/01-semantic-outcomes/run_lab.py`.
- Show the JSON summary and map each field to a trajectory event.
- If using the harness examples, distinguish teaching-lab traces from production claims.
- Recording boundary: keep the run offline and synthetic; do not imply real-world side effects.

## Learner practice

Annotate a five-step synthetic trajectory with:

`environment_revision`, `policy_revision`, `memory_revision`, `observation`,
`decision`, `tool`, `arguments`, `result`, `recovery_action`,
`stopping_criteria`, `terminal_state`.

Add `thread_id`, `turn_index`, `conversation_terminal_state`, and the memory
or state carried from the previous turn. Choose whether you are evaluating a
step, end-to-end task, trajectory, or thread/session. Then choose pass, fail, or
escalate. For an architecture comparison, record whether the workflow is flat
or uses subagents, what evidence justifies the handoff, and whether the
end-to-end result improved after accounting for cost, latency, context, and
recovery. Explain whether the final answer would change your decision and why.

## What this lesson does not prove

A captured trajectory is only as complete as the instrumentation. Missing events can make an unsafe path look safe, so evidence completeness is itself an evaluation criterion. One successful subagent run does not prove that a multi-agent architecture is better than a flat design or will remain useful after a model upgrade.
