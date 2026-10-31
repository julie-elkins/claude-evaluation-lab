# Lesson 27: Benchmark Limits and Tradeoffs

Module: 5 — Benchmarks, Release, and Capstone
Suggested runtime: 10–12 minutes
Primary lab: Write a benchmark limitations statement

## Learner objective

By the end of this lesson, you can identify contamination, Goodhart’s law, benchmark saturation, and Pareto tradeoffs when interpreting evaluation results.

## Slide and recording plan

1. **Benchmark fit** — relevance, coverage, freshness, and cost.
2. **Contamination** — test information may enter training or tuning.
3. **Goodhart’s law** — a target becomes less useful when optimized directly.
4. **Pareto frontier** — improvements in one dimension can cost another.
5. **Practice: write a limitation statement**.

## Speaker script

Benchmarks are useful because they make comparison easier, but they also create incentives to optimize for the score. Start by checking fit: does the benchmark represent the users, risks, workflow, and evidence conditions that matter to the decision?

Contamination means that benchmark examples or close variants may have entered training, tuning, or prompt development. Contamination can make a score look like general capability when it partly reflects familiarity with the test. We do not need to assume contamination to be cautious; we need to record what is known and what is not.

Goodhart’s law is the warning that when a measure becomes a target, it can stop being a good measure. A system can improve a benchmark score through patterns that do not improve the real task. This is why local cases, negative controls, and held-out examples remain important.

Performance also involves tradeoffs. The Pareto frontier is the set of options where improving one dimension, such as quality, cost, latency, or safety margin, would worsen another. There may be no single best model. The right choice depends on the decision and the risk tolerance.

In the demo, compare two synthetic system profiles. One has higher benchmark quality but higher latency and weaker evidence handling. The other has lower benchmark quality but stronger local controls. Choose which one fits a defined use case and document the tradeoff.

The cost of presenting a benchmark as a complete ranking is that stakeholders optimize the number instead of the system. A limitation statement protects the decision from that shortcut.

## Demo notes

- Use illustrative profiles and label them as synthetic.
- Show benchmark score, local failure rate, cost, latency, and safety findings separately.
- Do not claim that one metric determines the model choice.
- Recording boundary: avoid unverified current rankings or vendor comparisons.

## Learner practice

Write a five-sentence limitation statement covering:

1. what the benchmark measures,
2. what it does not measure,
3. possible contamination or freshness risk,
4. the local evidence needed,
5. the decision consequence of disagreement.

## What this lesson does not prove

A limitations statement improves honesty; it does not correct a poorly chosen benchmark. If the benchmark is irrelevant, the right action may be to replace it.
