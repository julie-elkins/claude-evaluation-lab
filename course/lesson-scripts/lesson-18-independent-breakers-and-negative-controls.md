# Lesson 18: Independent Breakers and Negative Controls

Module: 3 — Automated Evaluators
Suggested runtime: 10–12 minutes
Primary lab: Prove that a gate can catch a planted failure

## Learner objective

By the end of this lesson, you can use a negative control, meaning a deliberately bad case that should fail, to test whether an evaluator is actually connected to the release decision.

## Slide and recording plan

1. **The breaker role** — look for false passes, not only successful examples.
2. **Negative controls** — planted failures with expected findings.
3. **Independence** — the evaluator and breaker should not share one blind spot.
4. **Demo: mutate a passing case** — verify the gate catches it.
5. **Practice: write a breaker contract**.

## Speaker script

An independent breaker is a control designed to challenge the evaluation. A negative control is a deliberately bad case that should produce a known failure. These controls answer a practical question: if the system becomes wrong in a way we understand, does the evaluator notice and block or escalate it?

A positive example shows that one good case passes. A negative control tests whether the gate has a working failure path. Use both. If the negative control passes, the result is a finding about the evaluation system, even if all normal cases look healthy.

Independence matters. If the same judge, prompt, reference, and evidence preparation are used by both the evaluator and the breaker, they may share the same blind spot. Add controls that vary the failure mechanism: remove required evidence, alter the authorization state, inject a false tool name, or change the terminal outcome while leaving the response fluent.

The harness uses mutation controls to check whether the evaluation catches deliberate changes. This is more informative than adding more unmodified happy paths because it tests the sensitivity of the gate to the failure it claims to detect.

In the demo, begin with a passing synthetic case. Mutate one property, such as removing the required evidence or changing the semantic outcome to an unauthorized action. Run the evaluator and confirm that the finding appears in the structured result. Then restore the case and confirm the original path still passes.

The cost of skipping negative controls is silent evaluator drift. A refactor can disconnect a check from the decision, and the ordinary examples continue to pass. The dashboard remains green because nothing is actively trying to fail.

## Demo notes

- Use the harness mutation controls or a small local synthetic mutation.
- Show the expected failure before running the mutated case.
- Record whether the failure blocks, escalates, or only reports.
- Recording boundary: do not mutate real customer data; use the public synthetic examples.

## Learner practice

Write a breaker contract with:

1. the property being protected,
2. the deliberate mutation,
3. the expected finding,
4. the required release consequence,
5. the evidence that the breaker ran.

Add one breaker for missing evidence and one for unauthorized action.

## What this lesson does not prove

A passing negative control proves only that the tested failure was detected. It does not prove that other failure modes will be detected or that the control is independent in every meaningful sense.
