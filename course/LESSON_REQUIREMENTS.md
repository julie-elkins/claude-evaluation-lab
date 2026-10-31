# Lesson requirements and recording gate

This file is the build contract for the remaining scripts and slides. A lesson
is not ready for recording until its objective, visual anchor, hands-on
treatment, and limitation statement are present.

| # | Lesson | Learner outcome | Hands-on treatment | Currentness or evidence note |
| --- | --- | --- | --- | --- |
| 1 | What an evaluation is | Define an evaluation as evidence against a decision. | Inspect the checklist and write one decision target. | Durable principle. |
| 2 | Declare the decision | Name the task, decision, failure cost, and required evidence. | Write a four-line evaluation contract. | Durable principle. |
| 3 | Transport versus semantic outcome | Separate successful requests from successful tasks. | Run Lab 1 and compare naive and guarded paths. | Harness-backed. |
| 4 | Evidence contracts and terminal states | Distinguish completed, failed, refused, skipped, and not evaluated. | Classify synthetic terminal states. | Harness-backed. |
| 5 | Representative evaluation cases | Build normal, boundary, missing, conflicting, unauthorized, and failure cases. | Create a versioned case manifest. | Durable; use synthetic data. |
| 6 | Golden, calibration, and held-out data | Keep reference, calibration, and measurement cases separate. | Split a small dataset and explain the separation. | Harness checklist. |
| 7 | Rubrics and reviewer calibration | Turn a vague quality dimension into observable criteria. | Write a human rubric with examples. | Durable; examples must be synthetic. |
| 8 | Inter-rater agreement | Interpret raw agreement and chance-adjusted agreement. | Compare reviewer scores and inspect disagreements. | Metrics are illustrative, not universal thresholds. |
| 9 | Human-rating cost and agreement sessions | Recognize the time, cost, and alignment work behind human labels. | Run a calibration session on disputed cases. | Durable; avoid implying one required staffing model. |
| 10 | Deterministic checks | Use fixed rules for schemas, fields, tools, authorization, and state. | Add a failing deterministic assertion. | Harness-backed. |
| 11 | METEOR, BLEU, and ROUGE | Explain overlap, ordering, brevity, and reference dependence. | Score small synthetic text pairs. | Historical metrics; verify library/API details before recording. |
| 12 | Why reference metrics miss variation | Explain why valid paraphrases can score poorly. | Compare equivalent responses with different wording. | Durable limitation. |
| 13 | LLM-as-a-judge | Define judge inputs, criteria, score, and rationale. | Build a judge contract against a human rubric. | Provider behavior changes; date examples. |
| 14 | Structured evaluator outputs | Parse a judge result without confusing parseability with validity. | Validate a JSON schema and inject a semantically wrong result. | Claude/API syntax must be rechecked before recording. |
| 15 | Pointwise and pairwise judging | Distinguish single-response scoring from preference comparison. | Run both forms on synthetic responses. | Durable pattern; provider implementations change. |
| 16 | Judge bias | Detect position, verbosity, self-enhancement, and alignment bias. | Swap order, normalize length, and compare results. | Bias controls require human or reference calibration. |
| 17 | Judge best practices and evaluator layers | Use crisp criteria, binary scales where appropriate, rationale, calibration, low temperature, and layered evaluators. | Compare deterministic, semantic, and agent-based results. | Current harness checklist includes evaluator-layer control. |
| 18 | Independent breakers and negative controls | Keep the evaluator separate from the system being evaluated. | Run a deliberate false-pass case. | Harness skill boundary. |
| 19 | Claim extraction and evidence support | Turn a response into checkable claims. | Produce synthetic claim identifiers and evidence links. | Source content stays synthetic or approved. |
| 20 | Factuality evaluation | Check each claim against approved evidence. | Run supported and unsupported claim cases. | Harness content-assurance packs. |
| 21 | Weighted factuality and partial error | Aggregate fact-level results without hiding important errors. | Compare equal and risk-weighted aggregation. | Weighting is a declared decision, not a universal formula. |
| 22 | Safety, refusal, and prompt injection | Evaluate refusal and boundary behavior separately from helpfulness. | Run synthetic unsafe and injected-instruction cases. | Do not include harmful payloads beyond safe synthetic identifiers. |
| 23 | Tool routing and hallucinated tools | Detect missed tools, wrong tools, and invented tool names. | Inspect a synthetic tool-routing trajectory. | Harness scenarios and tool contracts. |
| 24 | Tool arguments, context, and state | Evaluate arguments, required context, authorization, and state change. | Compare valid and invalid synthetic tool calls. | Harness checklist and scenario packs. |
| 25 | Agent trajectories and recovery | Evaluate observe/plan/act loops, retries, recovery, and final state. | Run the agent workflow teaching lab and a degraded trajectory. | Harness-backed; final text cannot erase path failure. |
| 26 | Benchmark categories | Explain knowledge, reasoning, coding, safety, and agent benchmarks. | Map a benchmark to the decision it can and cannot support. | Benchmark names, versions, and access must be rechecked. |
| 27 | Benchmark limits and tradeoffs | Explain contamination, Goodhart's law, Pareto tradeoffs, and model profiles. | Write a benchmark limitation statement and cost/safety comparison. | Fast-changing benchmark landscape. |
| 28 | Baselines, variants, uncertainty, and slices | Compare systems with separate correctness, safety, tool-call, latency, cost, and user-outcome dimensions. | Run a controlled comparison with a high-risk slice. | Latest harness checklist addition. |
| 29 | Revision, release, rollback, and monitoring | Bind evidence to revisions and define rerun, release, rollback, feedback, and drift paths. | Inspect change-impact, rollback, monitorability, and feedback examples. | Current harness operational contract. |
| 30 | Capstone evaluation report | Produce a bounded evaluation decision with limitations and human ownership. | Submit a report and release recommendation. | Must state what the evidence does not prove. |

## Slide gate

Every lesson needs at least:

- one decision or concept anchor;
- one evidence or workflow visual;
- one learner action;
- one failure or limitation callout; and
- speaker notes that name the demo starting state, expected result, and
  recording boundary.

## Script gate

Every script needs to answer:

1. What decision is this lesson helping the learner make?
2. What evidence is required?
3. What failure would otherwise look like a pass?
4. What should the learner run, inspect, or write?
5. What does the result not prove?
