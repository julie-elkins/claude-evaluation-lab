# Lesson 23: Tool Routing and Hallucinated Tools

Module: 4 — Factuality, Safety, and Agent Behavior
Suggested runtime: 12–15 minutes
Primary lab: Measure tool-selection failures

## Learner objective

By the end of this lesson, you can evaluate tool routing, meaning whether the agent selects the right available tool, and distinguish missed tools from invented or unauthorized tools.

## Slide and recording plan

1. **The routing decision** — whether a tool is needed and which tool fits.
2. **Failure categories** — missed tool, wrong tool, hallucinated tool, unauthorized tool.
3. **Tool-router recall** — the proportion of eligible cases where the required tool was selected.
4. **Demo: inspect a synthetic tool catalog**.
5. **Practice: write routing cases and expected findings**.

## Speaker script

Tool routing is the decision about whether a tool is needed and, if so, which available tool should be called. Evaluate it before evaluating the tool result. If the agent chose the wrong tool, a perfect tool implementation cannot repair the decision.

Use distinct failure categories. A missed tool means the agent should have called an available tool but did not. A wrong tool means it called an available tool that cannot satisfy the task. A hallucinated tool means it named or attempted to call a tool that is not in the catalog. An unauthorized tool means the tool may exist but the current task is not allowed to use it.

Tool-router recall is the proportion of eligible cases where the required tool was selected. Recall is useful, but it should be paired with precision, meaning the proportion of selected tools that were appropriate, and with authorization checks. High recall that includes many unsafe or irrelevant calls is not a successful router.

The tool catalog is part of the evidence. Record the tool name, description, required inputs, authorization, and expected use. If the catalog is vague, a routing failure may actually be a specification failure. The evaluation should not blame the agent for a choice that the interface leaves ambiguous.

In the demo, inspect a small synthetic catalog and run cases for a supported lookup, a case where no tool is needed, an unavailable tool request, and an unauthorized tool. Record the expected routing decision before viewing the agent result.

The cost of ignoring routing is hidden work and unsafe side effects. The agent can appear capable because it produces fluent text while never using the required source or tool.

## Demo notes

- Use the public synthetic tool-routing examples.
- Show tool catalog metadata and authorization separately.
- Do not execute external tools or make live changes in the base lab.
- Recording boundary: use synthetic tool names and identifiers only.

## Learner practice

Create six routing cases:

1. required tool available,
2. no tool needed,
3. wrong tool selected,
4. tool missing,
5. hallucinated tool name,
6. unauthorized tool.

Define the expected finding and release consequence for each case.

## What this lesson does not prove

Correct routing does not prove correct tool arguments, safe execution, or successful recovery. It is one stage of the agent decision path.
