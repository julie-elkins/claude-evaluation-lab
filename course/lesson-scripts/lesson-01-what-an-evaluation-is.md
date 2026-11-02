# Lesson 1: What an evaluation is—and what it is not

**Module:** Evaluation foundations  
**Estimated runtime:** 8 minutes  
**Lab:** None; orientation and inspection

## Learner objective

By the end of this lesson, you can describe an evaluation as evidence collected
against a declared decision, rather than as a single score attached to a model.

## Slide and recording plan

1. Title: What are we trying to decide?
2. Evaluation is a decision-support workflow.
3. A score is not the same thing as evidence.
4. The evaluation layers: task, path, usage, and decision.
5. The agent development lifecycle: define, build, test, release, deploy,
   monitor, and learn.
6. From manual discovery to a durable evaluation.
7. Preview: the false-pass lab.

## Speaker script

When people say “we need to evaluate the model,” they may mean several
different things. They may mean: is the answer useful? Is it factually
supported? Did the agent select the right tool? Did it stay within its cost
limit? Did the request finish quickly enough? Or did the change improve the
workflow without making a high-risk case worse?

Those are different questions. If we collapse them into one number, we lose the
reason we were measuring in the first place.

In this course, I will use a narrower definition. An evaluation is a workflow
that collects evidence against a declared decision. The decision might be
whether to release a prompt change, whether to keep a model in production, or
whether a particular agent task is ready for human approval.

That definition has two consequences.

First, the decision comes before the metric. If the decision is whether an agent
is allowed to update a customer record, a useful evaluation needs evidence about
authorization and state change. A high language-quality score does not answer
that question.

Second, the evidence must be bounded. We need to know which workflow, model,
prompt, tools, data, policy, and evaluator produced the result. Otherwise a
passing result may belong to a different system than the one we are about to
change.

The [Agent Assurance Harness](https://github.com/julie-elkins/agent-assurance-harness)
gives us a small, inspectable example. It records transport status, semantic
outcome, retry count, estimated cost, evaluator status, and missing evidence.
It does not pretend that those fields prove live model quality. It tells us
what was observed for one declared synthetic scenario.

That distinction is important because evaluation results are often reused beyond
their original scope. A result from a small test set may be repeated in a slide
as if it were a production guarantee. A benchmark score may be quoted as if it
answered a customer-specific question. A successful request may be reported as
task completion even though the response is empty.

Manual inspection is a good way to discover a failure. It becomes a durable
evaluation only when we preserve the case, declare the evaluator, version the
inputs and workflow, and define the experiment and action that should follow.
That is the move from “I saw something go wrong” to “we can detect this failure
again and make a bounded decision about it.”

Keep the lifecycle visible: define the decision, build the workflow and
controls, test representative cases, release with approval and rollback,
deploy within a bounded environment, monitor the evidence, and turn safe
findings back into new regression or held-out cases. The same evaluation
vocabulary works across those phases, but the evidence and decision are not
identical.

We will keep asking one question throughout this course: what decision does this
evidence support, and what does it not support?

In the next lesson, we will write that decision down before choosing a metric.
Then we will run the first lab, where two workflows both receive a successful
transport response but only one has enough evidence to continue.

## Demo notes

Open the course README and the Agent Evaluation Checklist. Point to the fields
that separate task outcome, trace evidence, usage, uncertainty, and release
decision. Do not present the checklist as an automatic production approval; it
is a decision aid for the declared workflow.

## Learner practice

Choose one Claude workflow you care about. Write one sentence beginning:

> “I need evidence to decide whether…”

Then list one thing that sentence does not decide, and identify which lifecycle
phase you are in: define, build, test, release, deploy, monitor, or learn.

## What this lesson does not prove

It does not establish that any model, benchmark, or evaluation harness is
universally reliable. It establishes the course's evaluation vocabulary and
decision-first framing.
