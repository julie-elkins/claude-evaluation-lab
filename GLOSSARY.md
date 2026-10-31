# Glossary

The course uses these terms consistently. Each definition describes why the
term matters to an evaluation decision.

## Agent

A system that can observe context, choose actions, call tools, and continue
until it reaches a stopping condition.

## Baseline

The reference system or process used for comparison. Without a baseline, an
improvement claim has no controlled point of reference.

## Calibration

A session where reviewers or evaluators score shared examples, compare
disagreements, and clarify the rubric before wider measurement.

## Case

One test situation, including input, context, expected behavior, observed
result, and decision consequence.

## Deterministic check

A repeatable rule that should return the same result for the same evidence, such
as checking a required field or an authorization boundary.

## Evidence

Recorded information that supports, limits, or contradicts an evaluation
decision.

## Evidence contract

The explicit list of evidence that must exist before a result can support its
declared decision.

## Evaluator

A rule, program, model, or human process that turns observed behavior into a
finding or score.

## Held-out case

A case kept away from evaluator tuning and used later to estimate performance on
cases the method did not help shape.

## Inter-rater agreement

How consistently multiple reviewers score the same cases. Agreement describes
repeatability, not automatic correctness.

## Judge

In this course, a language model used to evaluate another output against
explicit criteria. A judge is a measurement component, not an oracle.

## Negative control

A deliberately bad case that should fail. It tests whether the evaluator can
detect the failure it claims to measure.

## Pointwise judging

Scoring one response against an absolute rubric.

## Pairwise judging

Choosing between two responses under a stated criterion. The result is
relative, so it does not prove that the preferred answer passes an absolute
requirement.

## Semantic outcome

Whether the requested task actually reached its declared goal. It is different
from transport status, which only describes whether a request returned.

## Slice

A meaningful subset of cases, such as high-risk, boundary, or missing-context
cases, inspected separately from the aggregate result.

## Terminal state

The declared end state of an evaluation path, such as completed, failed,
refused, skipped, or not evaluated.

## Transport status

Whether the request boundary returned successfully. A successful transport
status does not prove that the task succeeded.

## Trajectory

The ordered sequence of observations, decisions, tool calls, results, and
recovery steps that produced an agent outcome.

## Uncertainty

The part of a result that could change because of sampling, repeated runs,
evaluator variation, or missing evidence.

## Variant

A changed model, prompt, tool policy, evaluator, or workflow compared with a
baseline.
