# Lesson 2: Declare the decision before choosing the metric

**Module:** Evaluation foundations  
**Estimated runtime:** 9 minutes  
**Lab:** Guided design exercise

## Learner objective

By the end of this lesson, you can write a decision target, name the failure
that matters most, and choose evidence that can actually support that decision.

## Slide and recording plan

1. Start with the decision, not the score.
2. The same output can require different evaluations.
3. Name the most expensive plausible failure.
4. Map the decision to evidence.
5. Learner exercise: write the evaluation contract.

## Speaker script

An evaluation becomes easier to design when the decision is explicit. Without
that sentence, teams often begin by asking which metric is popular or which
benchmark is easy to run. That reverses the dependency.

Consider a Claude assistant that summarizes an internal document. If the
decision is “does the summary sound clear?”, a human rubric for relevance and
readability may be useful. If the decision is “can this summary be sent to a
customer?”, we also need factuality, source support, sensitive-data checks, and
an approval boundary.

The output did not change. The decision changed. That means the evidence must
change.

I use four questions to define the evaluation contract.

First: what user task or system behavior are we evaluating?

Second: what decision will the result support?

Third: what is the most expensive plausible failure? This is not a request to
invent a dramatic scenario. It is a way to prevent an average score from hiding
the one failure that makes release unacceptable.

Fourth: what evidence would allow another person to inspect the result? The
answer may include the final text, but it may also need the tool choice, the
arguments, the authorization state, the source identifiers, the number of
retries, or the state before and after the action.

This is where evaluation layers become useful. A deterministic check is a fixed
rule, such as whether a required field exists or whether an argument matches a
schema. A semantic check evaluates meaning, such as whether the response
addresses the task. A trajectory check evaluates the sequence of actions,
including retries and tool calls. A release check decides whether the evidence
supports the declared change.

No single layer replaces the others. A response can be semantically helpful
while using an unauthorized tool. A tool call can be syntactically valid while
changing the wrong record. A low cost can coexist with an unsafe refusal.

For the exercise, choose one Claude workflow and write four lines:

The task is…

The decision is…

The most expensive plausible failure is…

The evidence I need is…

If you cannot name the evidence, the evaluation is not ready to run. That is
not a failure of the model. It is a missing contract.

The next lesson turns this into a runnable example by separating transport
status from semantic outcome.

## Demo notes

Use a simple two-column slide: “decision” and “evidence.” Walk through a
document assistant example, then show the same output evaluated under two
different decisions. Keep the example synthetic and do not use private
documents.

## Learner practice

Complete the four-line evaluation contract for one workflow. Add one negative
case that would look successful if you checked only the request status.

## What this lesson does not prove

A well-written contract does not prove that the chosen evidence is sufficient.
It makes the intended decision and the missing evidence visible enough to review.
