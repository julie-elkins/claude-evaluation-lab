# Lesson 4: Evidence contracts and terminal states

**Module:** Evaluation foundations  
**Estimated runtime:** 10 minutes  
**Lab:** Guided checklist exercise

## Learner objective

By the end of this lesson, you can distinguish completed, failed, refused,
skipped, and not-evaluated results, and explain why missing evidence cannot be
silently treated as a pass.

## Slide and recording plan

1. Every evaluation needs an evidence contract.
2. Terminal states make missing work visible.
3. “Not evaluated” is not “passed.”
4. The evidence layers in the harness.
5. Module checkpoint.

## Speaker script

An evidence contract is the explicit description of what must be observed before
an evaluation result can support its decision. The contract is not a score
formula. It is the boundary around the claim.

For example, a contract might require a task identifier, the system revision,
the expected state transition, the observed state transition, the evaluator
version, and a record of whether the workflow stayed within its cost ceiling.
The exact fields depend on the decision. What matters is that the required
evidence is named before the result is interpreted.

##### Terminal states 🚦

The harness uses separate terminal states so an absent result cannot disappear
inside a green report.

| Harness terminal state | Meaning | Boundary |
|---|---|---|
| `completed` | The declared evaluation path reached its intended terminal state. | It does not mean that every task passed. |
| `failed` | The evidence was present, but the declared rule was not met. | The failure must remain visible. |
| `refused` | The evaluation declined to proceed because required input, authority, or safety conditions were missing. | It is not equivalent to a model failure. |
| `skipped` | A check was intentionally not run. | The reason must remain visible. |
| `not_evaluated` | The evidence was unavailable or invalid. | It is not a weaker form of pass. |

> [!NOTE]
> These are harness execution states. They explain what happened during the
> evaluation path; they are not a replacement for the separate report and
> release statuses used elsewhere in this course.

This distinction matters when a report contains a favorable average. Suppose
the evaluator ran on nine normal cases and could not run the tenth high-risk
case because its source was unavailable. The average over nine cases may still
be useful as an observation, but it cannot support a claim that the full
declared set passed.

The same logic applies to LLM-as-a-judge results. A judge score without a
calibration result, a stable rubric, or a human comparison may be exploratory.
It can help locate behavior worth inspecting. It should not silently become
release evidence.

> **Learner checkpoint — review the evidence contract**
>
> Use the checklist as a review surface. For each row, ask four questions:
>
> 1. Who owns the check?
> 2. What evidence artifact identifies the result?
> 3. What threshold or decision rule applies?
> 4. What happens if the evidence is missing?

That last question is the one that prevents absence from becoming a pass.
Sometimes the answer is “block.” Sometimes it is “request human review.”
Sometimes it is “run the case again with a bounded limit.” The answer must be
declared before the result is read.

You have now completed the foundation module. You can define the decision, name
the failure that matters, separate transport status from semantic outcome, and
keep unavailable evidence visible. The next module will build the evaluation
cases and human rubric that give those checks something trustworthy to measure.

## Demo notes

Open the evaluation checklist and show the status vocabulary. Use one example
where the evidence is missing and ask whether the result should be `passed`,
`not_evaluated`, or `blocked`. Emphasize that the status is part of the
decision contract, not decorative report text.

## Learner practice

Create a five-row table for one workflow:

- normal case;
- boundary case;
- missing-evidence case;
- conflicting-evidence case; and
- deliberately degraded case.

Assign the expected terminal state for each.

## What this lesson does not prove

The vocabulary makes evaluation gaps visible. It does not decide the correct
threshold for every product or risk level; that decision belongs to the
accountable owner of the workflow.
