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

## The harness is part of the system under test

The **system under test** is the complete workflow whose behavior supports the
decision, not only the model that generates the response. For a coding-agent
evaluation, bind the result to the model, harness or scaffolding (the prompts,
tools, permissions, and orchestration around the model), repository revision,
environment, evaluator revision, task outcome, trace completeness, retry
behavior, cost, and repository changes.

Changing the harness can change the measured result even when the model is
unchanged. Report those components separately so a model improvement is not
mistaken for a scaffolding improvement, or a missing trace is mistaken for a
successful run.

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

## First-attempt success versus repeated-run reliability

**First-attempt success** means the agent completed the task on one declared
run. **Repeated-run reliability** means the same versioned task succeeds across
the number of independent runs required by the decision. The first measure
shows what happened once; the second shows how consistently the workflow can
deliver without a person selecting the best attempt.

For repeated runs:

- record the model, prompt, tools, repository revision, evaluator revision, and
  run conditions;
- report the result for each task, not only the aggregate score;
- separate variation caused by the model from variation caused by the
  scaffolding (the prompts, tools, and orchestration around the model),
  repository state, environment, timeouts, and evaluator; and
- inspect every failed attempt for unintended edits, partial changes, deleted
  files, or other repository damage before retrying or calling the task
  recovered.

An attempt that eventually succeeds after leaving an unsafe or unexplained
change behind is not a clean recovery. A single successful run therefore does
not establish coding-agent reliability or merge readiness.

### Repeated-run metrics

Use the metric that matches the decision rather than reporting one headline
success rate:

- **Pass@1** is success on one declared attempt.
- **Pass@k** is success on at least one of `k` independent attempts. It answers
  whether a retry budget can find a successful result.
- **Pass^k** is success on every one of `k` independent attempts. It answers
  whether the workflow is reliable without selecting the best attempt.
- **Flip rate** is the proportion of tasks whose pass or fail outcome changes
  across repeated runs. It makes instability visible even when the aggregate
  score stays similar.

Report the task-level outcomes and the repository state for each attempt.
Pass@k is not a substitute for Pass^k when the decision requires predictable
behavior, and a retry is not recovered until the failed attempt has been
checked for unintended repository changes.

### Preservation-aware interpretation

An aggregate score increase is not an improvement if previously covered tasks
regress and the regression is hidden, unexplained, or outside the accepted
decision rule. Compare the candidate with the baseline at the task and
high-risk-slice levels, preserve newly exposed failures as regression cases,
and require an explicit human decision for any accepted tradeoff.

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

## Current Codex evaluation path

The current Codex evaluation guidance describes a workflow in which Codex can
help generate an evaluation suite for a coding-agent task and an evaluation
runner can execute that suite against representative cases. Treat the suite
generator, runner, evaluator, and human approval as separate evidence
boundaries:

- define the coding-agent decision and failure cost;
- build cases that include repository state, task instructions, scope, and
  expected evidence;
- inspect the patch, command trajectory, tests, and terminal state;
- evaluate final output, individual steps, and the full trajectory separately;
  and
- keep merge, release, and rollback decisions human-owned.

OpenAI's current Codex page points to Promptfoo as an optional implementation
for running generated evaluation suites. Promptfoo is not required for this
course, and its presence does not establish evaluator validity. The learner
should first understand the provider-neutral contract, then map a provider
workflow into it.

Use the current [Codex skills documentation](https://developers.openai.com/codex/skills/create-skill),
[`AGENTS.md` guidance](https://developers.openai.com/codex/guides/agents-md), and
[Codex evaluation guidance](https://developers.openai.com/codex/use-cases/ai-app-evals)
and [Promptfoo](https://github.com/promptfoo/promptfoo) for provider-specific
workflow details. Map the resulting evidence into the course's provider-neutral
contract. The older OpenAI Evals repository is historical context, not a
required dependency or a release gate for this learner path.

OpenAI's separate Evals API platform is being retired: the official notice says
existing evals became read-only on October 31, 2026, with shutdown scheduled
for November 30, 2026. The course therefore teaches the evidence contract and
current agent-evaluation guidance rather than making the Evals API a required
dependency. Re-check this lifecycle note before teaching a provider-specific
workflow.

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

