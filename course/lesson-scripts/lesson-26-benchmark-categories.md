# Lesson 26: Benchmark Categories

Module: 5 — Benchmarks, Release, and Capstone
Suggested runtime: 10–12 minutes
Primary lab: Map a benchmark category to a decision

## Learner objective

By the end of this lesson, you can distinguish benchmark categories and explain what question each category can and cannot answer.

## Slide and recording plan

1. **A benchmark is a test set with a claim** — not a universal quality score.
2. **Knowledge** — examples such as MMLU-style subject questions.
3. **Reasoning and coding** — examples such as AIME, PIQA, and SWE-bench-style tasks.
4. **Safety and agents** — examples such as HarmBench- and Tau-bench-style evaluations.
5. **Practice: map benchmark evidence to a product decision**.

## Speaker script

A benchmark is a named or repeatable test set used to compare systems against a defined task. The benchmark category tells us what capability is being sampled; it does not tell us whether the benchmark matches our product decision.

Knowledge benchmarks test subject or factual recall under a specified format. Reasoning benchmarks test problem solving or inference. Coding benchmarks test whether a system can modify or produce code under a defined task and verification process. Safety benchmarks test responses to harmful or policy-sensitive requests. Agent benchmarks test multi-step behavior, tool use, and task completion.

Examples discussed in the source lecture include MMLU-style knowledge tasks, AIME and PIQA-style reasoning tasks, SWE-bench-style coding tasks, HarmBench-style safety tasks, and Tau-bench-style agent tasks. Before recording, recheck the current benchmark names, versions, licensing, and task definitions. These resources evolve, and an old label can make the course sound more current than its evidence.

Map every benchmark result to a decision. A knowledge score may inform retrieval or subject-matter capability. It does not prove that the agent handles authorization or tool state. A coding score may inform repository task performance. It does not prove safe deployment into a particular codebase.

In the demo, choose one course decision and identify the benchmark category that could inform it. Then name the local evaluation evidence still required. The benchmark is an input to the decision, not the decision itself.

The cost of category confusion is overclaiming. Teams select a familiar benchmark, report an impressive number, and discover later that it did not measure the failure that mattered in their workflow.

## Demo notes

- Use benchmark names as examples, not as current rankings.
- Show a two-column map: benchmark question and product question.
- Keep the course’s own synthetic harness as the local evidence layer.
- Recording boundary: recheck benchmark facts and version details immediately before final recording.

## Learner practice

For each decision, select one useful benchmark category and one local check:

1. subject-matter knowledge,
2. safe refusal,
3. code change quality,
4. multi-step tool completion,
5. evidence-grounded answer.

Explain why the benchmark alone is insufficient.

## What this lesson does not prove

Benchmark performance is evidence about sampled tasks under benchmark conditions. It does not establish production fit, safety, or reliability for an untested workflow.
