# Claude Evaluation Lab instructions

This is a public learner-facing course repository built on the public
Agent Assurance Harness.

## Boundaries

- Use public synthetic data only.
- Never commit credentials, API keys, private URLs, unpublished exam content,
  raw provider payloads, private prompts, or private logs.
- Keep the first learner path offline and deterministic.
- Treat the Agent Assurance Harness as a pinned dependency, not as copied source.
- A live Claude example must be opt-in and must declare request, time, token,
  and spend limits before execution.
- Every lab must state what it proves and what it does not prove.
- Every evaluation lesson must include at least one deliberately degraded case
  that should be caught by the evaluator.
- Do not turn a passing synthetic result into a claim about live model quality,
  production safety, or learner adoption.

## Learner contract

Each lab must provide:

1. a fast first result;
2. a workflow map;
3. copy-paste commands;
4. expected output;
5. troubleshooting;
6. an evidence template;
7. a limitation statement; and
8. an optional extension for learners who want more depth.

## Writing

Explain evaluation terms inline. For example, semantic outcome means whether the
requested task actually reached its declared goal; it is separate from transport
status, which only says whether a request returned successfully.
