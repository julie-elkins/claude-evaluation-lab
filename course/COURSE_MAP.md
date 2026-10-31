# Course map

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

Hands-on outcome: create a small reviewed evaluation set and rubric.

### Module 3 — Automated evaluation

9. Deterministic checks
10. Reference-based metrics and their limits
11. LLM-as-a-judge with structured outputs
12. Judge bias, calibration, and reproducibility
13. Independent breakers and negative controls

Hands-on outcome: compare a deterministic check, a judge result, and a
deliberately degraded case.

### Module 4 — Factuality, safety, and agents

14. Claim extraction and evidence support
15. Factuality evaluation for Claude responses
16. Safety and refusal evaluation
17. Tool selection, arguments, and state changes
18. Evaluating multi-step agent trajectories

Hands-on outcome: evaluate an agent workflow without allowing a plausible final
answer to hide a failed path.

### Module 5 — Regression and release decisions

19. Baselines, variants, and regression tests
20. Cost, latency, uncertainty, and metric tradeoffs
21. Benchmarks versus use-case evidence
22. Capstone: produce an evaluation report and release recommendation

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

## Source relationship

The Stanford lecture reviewed for this course provides conceptual reference
points such as human agreement, rule-based metrics, LLM-as-a-judge, factuality,
agent evaluation, benchmarks, and Goodhart's law. The lesson scripts will be
original and will not reproduce the lecture transcript.
