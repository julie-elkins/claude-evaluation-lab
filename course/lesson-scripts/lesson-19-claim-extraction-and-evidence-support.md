# Lesson 19: Claim Extraction and Evidence Support

Module: 4 — Factuality, Safety, and Agent Behavior
Suggested runtime: 12–15 minutes
Primary lab: Turn a response into claim-level evidence checks

## Learner objective

By the end of this lesson, you can extract checkable claims from an answer and evaluate whether each claim is supported by the available evidence.

## Slide and recording plan

1. **A response is not one fact** — it contains multiple claims with different risks.
2. **Retrieval is a separate evaluation layer** — measure whether the needed evidence was found before judging the answer.
3. **Claim extraction** — identify atomic, checkable statements.
4. **Evidence support** — supported, unsupported, conflicting, or ambiguous.
5. **Demo: claim-level inspection** — show why one overall score hides a failure.
6. **Practice: build a retrieval and claim/evidence table**.

## Speaker script

Factuality evaluation asks whether the answer’s claims are supported by evidence. Start by separating the response into atomic claims: statements that can be checked independently. A single paragraph may contain a correct date, an unsupported recommendation, and a claim about an action that never occurred.

If the workflow retrieves context, evaluate retrieval before evaluating
grounding. Retrieval recall asks whether the needed evidence was found.
Context relevance asks whether the retrieved material belongs to the task.
Context sufficiency asks whether enough evidence was available to answer safely.
Grounding asks whether the response used that available evidence correctly. A
grounded answer cannot be expected when the required evidence was never
retrieved, so those findings must remain separate.

For each claim, record the evidence source, the support status, and the risk if the claim is wrong. Useful statuses include supported, unsupported, contradicted, and ambiguous. “Ambiguous” means the available evidence does not justify a confident decision; it is not the same as supported.

Keep evidence support separate from source authority. A source can be authoritative but irrelevant to the specific claim. A relevant source can be low quality. The evaluation should record both questions: is this the right evidence, and does the evidence actually support the claim?

Claim extraction can be performed by a human, a structured model step, or a combination. If extraction is automated, validate that claims were not merged in a way that hides a risky statement. A claim-level table makes review slower at first, but it prevents one overall “factuality” score from hiding a high-impact unsupported claim.

In the demo, inspect a synthetic answer with three claims. Mark one supported, one unsupported, and one ambiguous. Then compare the claim table with the answer-level result. The point is not to produce a perfect fact checker from one prompt. The point is to preserve the evidence needed to explain the decision.

The cost of skipping claim extraction is that fluent prose becomes the unit of trust. A response can look mostly correct while containing one unsupported instruction that causes the user to take the wrong action.

## Demo notes

- Use synthetic evidence records with stable IDs.
- Show claim IDs, evidence IDs, support status, and risk.
- Keep unsupported and contradicted distinct.
- Recording boundary: do not use private or unpublished source material.

## Learner practice

Take a six-sentence synthetic answer and create:

`case_id`, `retrieved_evidence_ids`, `required_evidence_ids`,
`retrieval_status`, `claim_id`, `claim_text`, `evidence_ids`,
`support_status`, `risk`, `review_action`.

Write a final decision that explains whether one unsupported claim blocks the answer or triggers review.

## What this lesson does not prove

Claim extraction can miss implicit claims, qualifications, or reasoning steps. A clean table does not guarantee that every meaningful assertion was found.
