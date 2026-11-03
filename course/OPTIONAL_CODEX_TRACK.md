# Optional Codex coding-agent extension 🔬

The required course path remains offline, synthetic, and provider-neutral. This
optional extension adds a second agent boundary: evaluating a coding agent that
can inspect a repository, choose commands, edit files, run tests, and report
completion.

Codex is not treated as merely another model provider. A coding-agent result
includes a repository diff, test evidence, command and tool trajectory, scope
boundaries, and safety evidence. The same evaluation contract still applies:
declare the decision, required evidence, failure cost, stopping condition, and
human owner before inspecting the result.

## When to use it

Use this extension after Labs 4–8, when you understand trajectories,
observability, security controls, and release decisions.

Run the [optional Codex coding-agent evaluation lab](labs/optional-codex-agent-adapter/README.md)
to evaluate a synthetic healthy run and a deliberately degraded run.

## Coding-agent evaluation dimensions

- [ ] The agent interpreted the declared task.
- [ ] The agent inspected only the relevant repository scope.
- [ ] Commands were permitted and bounded.
- [ ] No destructive command or secret-access attempt occurred.
- [ ] The changed-file set stayed within scope.
- [ ] Required tests ran and their results were preserved.
- [ ] The diff is reviewable and tied to the task.
- [ ] The agent stopped at the declared terminal state.
- [ ] The completion claim is supported by evidence.
- [ ] Human review and rollback remain explicit.

## Skills and instruction evidence

Codex may use reusable **skills**, meaning instruction and workflow bundles that
can be selected explicitly or loaded when their description matches the task. It
may also read `AGENTS.md`, a repository instruction file whose scope and
precedence can change what the agent is allowed to do.

Evaluate these separately from the final patch:

- [ ] The intended skill or instruction file was selected.
- [ ] An inappropriate skill or instruction file did not trigger.
- [ ] The active instruction sources and their scope are recorded.
- [ ] Local instructions did not silently conflict with broader instructions.
- [ ] The agent followed the instructions in its commands, edits, tests, and
      stopping behavior.
- [ ] The skill or instruction change was compared with a baseline.
- [ ] The result was checked in a fresh run rather than only in a reused
      context.

The skill-selection result and the task-result quality are different measures.
A skill can trigger correctly and still produce a poor patch. Conversely, a
good patch from one run does not prove that the skill generalizes across
repositories or task types.

Use the current [Codex skills documentation](https://developers.openai.com/codex/skills/create-skill),
[`AGENTS.md` guidance](https://developers.openai.com/codex/guides/agents-md), and
[Codex evaluation guidance](https://developers.openai.com/codex/use-cases/ai-app-evals)
for provider-specific syntax. Map the resulting evidence into the course's
provider-neutral contract.

## Provider-neutral mapping

| Course concept | Coding-agent evidence |
| --- | --- |
| Semantic outcome | The requested repository change actually works. |
| Trajectory | File inspection, commands, edits, tests, retries, and stopping. |
| Evidence contract | Diff, changed-file list, test result, terminal state, and policy evidence. |
| Security boundary | No secret access, destructive command, or unauthorized side effect. |
| Release decision | Merge, hold, revise, or rollback based on the patch evidence. |

## Optional live path

After the synthetic lab is understood, attach one approved Codex run to the same
contract. Keep the live path optional because credentials, changing product
behaviour, repository access, cost, and privacy obligations reduce
reproducibility.

Use the current [Codex documentation](https://developers.openai.com/codex/)
and [Codex SDK documentation](https://developers.openai.com/codex/sdk/) for
current syntax. Preserve provider-specific evidence at the adapter boundary,
then map it into the course's provider-neutral report vocabulary.

One live coding-agent run does not prove general code quality, security,
reliability, or merge readiness.

