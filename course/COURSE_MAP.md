# Course map

Start with the generated [learner guide](../GUIDE.md). It contains the
fundamentals, all 30 learner-facing lessons, all five runnable labs, diagrams, and
module practice checks in one reading path. This file remains the compact
authoring map; the lesson scripts remain the editable recording source.

## Working title

**Claude Evaluation Lab: Build Reliable LLM Evaluations from Scratch**

## Learner promise

By the end of the course, learners will be able to design an evaluation
workflow for a Claude application or agent, run it against representative test
cases, interpret the evidence, and explain what the result does and does not
prove.

## Audience and prerequisites

The course is for developers, solutions architects, AI product teams, technical
leaders, and other practitioners who need to evaluate LLM behavior. Learners
should be comfortable reading JSON and running command-line examples. Python
experience is helpful but not required for the introductory labs.

## Modules and lessons

The course is organized as five modules and 30 lessons. The count deliberately
matches the Claude Architect Lab pattern so this remains a hands-on, task-based
learning path rather than becoming one long lecture.

### Module 1 — Evaluation foundations

1. What an evaluation is—and what it is not
2. Declaring the decision before choosing the metric
3. Transport status versus semantic outcome
4. Evidence contracts and terminal states

Hands-on outcome: identify a false pass in the existing teaching lab.

### Module 2 — Evaluation cases and human review

5. Building representative evaluation cases
6. Golden datasets, calibration sets, and held-out cases
7. Rubrics and reviewer calibration
8. Inter-rater agreement and disagreement review
9. Human-rating cost, speed, and agreement sessions

Hands-on outcome: create a small reviewed evaluation set, rubric, and
disagreement-review record.

### Module 3 — Automated evaluation

10. Deterministic checks
11. Reference-based metrics: METEOR, BLEU, and ROUGE
12. Why reference metrics miss valid variation
13. LLM-as-a-judge: inputs, scores, and rationales
14. Structured outputs and parseable evaluator results
15. Pointwise and pairwise judging
16. Judge bias: position, verbosity, and self-enhancement
17. Judge best practices, calibration, and evaluator layers
18. Independent breakers and negative controls

Hands-on outcome: compare a deterministic check, a judge result, human
calibration evidence, and a deliberately degraded case.

### Module 4 — Factuality, safety, and agents

19. Claim extraction and evidence support
20. Factuality evaluation for Claude responses
21. Weighted factuality and partial error
22. Safety, refusal, and prompt-injection evaluation
23. Tool routing, tool hallucination, and tool descriptions
24. Tool arguments, context, and state changes
25. Evaluating multi-step agent trajectories and recovery

Hands-on outcome: evaluate an agent workflow without allowing a plausible final
answer to hide a failed path, unsafe action, or missing evidence.

### Module 5 — Regression and release decisions

26. Benchmark categories: knowledge, reasoning, coding, safety, and agents
27. Benchmark contamination, Goodhart's law, and Pareto tradeoffs
28. Baselines, variants, uncertainty, high-risk slices, and evaluator layers
29. Revision binding, drift, release decisions, rollback, and monitoring
30. Capstone: produce an evaluation report and release recommendation

Hands-on outcome: run a bounded comparison and write a decision that names
blocking failures, uncertainty, and limitations.

## Production pattern

Every lesson will have:

- a short concept slide sequence;
- a learner objective;
- a runnable lab or guided inspection;
- a starting state;
- an expected result;
- a deliberately degraded or negative-control case;
- a troubleshooting section;
- a speaker script; and
- a statement of what the evidence does not prove.

## Currentness rule

The course separates durable evaluation principles from fast-changing examples.
Provider behavior, model names, benchmark versions, API syntax, and pricing
must be dated or verified before recording. The harness revision, evaluator
contract, and course examples must be recorded together so a later change can
trigger re-evaluation rather than silently reusing stale evidence.

## Source relationship

The Stanford lecture reviewed for this course provides conceptual reference
points such as human agreement, rule-based metrics, LLM-as-a-judge, factuality,
agent evaluation, benchmarks, and Goodhart's law. The lesson scripts will be
original and will not reproduce the lecture transcript.

## Continue learning

- [Julie’s YouTube channel](https://www.youtube.com/@JulieElkins) — optional video walkthroughs.
- [Julie’s public site](https://julie-elkins.github.io) — projects, learning paths, and design principles.
- [Agent Systems Design Guide](https://github.com/julie-elkins/agent-systems-design-guide) — shared design reasoning and report vocabulary.
- [Apple Platform Agent Quality Lab](https://github.com/julie-elkins/apple-platform-agent-quality-lab) — native macOS implementation of the evaluation boundary.
