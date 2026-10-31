# Lesson 25: Agent Trajectories and Recovery

Module: 4 — Factuality, Safety, and Agent Behavior
Suggested runtime: 12–15 minutes
Primary lab: Inspect a multi-step trajectory and recovery outcome

## Learner objective

By the end of this lesson, you can evaluate an agent trajectory, meaning the sequence of observations, decisions, tool calls, results, and recovery steps that produces the final outcome.

## Slide and recording plan

1. **The final answer is not the whole run** — observe, plan, act, recover.
2. **Trajectory evidence** — decisions, tools, arguments, state, and terminal outcome.
3. **Recovery versus retry** — a retry is not recovery unless the failure is addressed.
4. **Demo: guarded and unguarded paths**.
5. **Practice: annotate a trajectory and choose the final decision**.

## Speaker script

An agent trajectory is the ordered sequence of what the agent observed, decided, attempted, and recovered from. The final answer is only one view of that sequence. Two agents can produce the same final wording while one used an authorized path and the other made an unsafe or unsupported detour.

Evaluate the trajectory in stages: observation, planning, action, result, and recovery. Record which evidence was available at each stage, which tool was selected, what arguments were sent, how the result changed the next step, and whether the agent reached a valid terminal state.

Distinguish retry from recovery. A retry repeats an attempt. Recovery changes the plan or escalates because the previous attempt failed. Repeated retries can waste budget, duplicate side effects, or hide the fact that the agent has no safe next step.

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

`observation`, `decision`, `tool`, `arguments`, `result`, `recovery_action`, `terminal_state`.

Choose pass, fail, or escalate. Explain whether the final answer would change your decision and why.

## What this lesson does not prove

A captured trajectory is only as complete as the instrumentation. Missing events can make an unsafe path look safe, so evidence completeness is itself an evaluation criterion.
