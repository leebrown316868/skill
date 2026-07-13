---
name: choose-workflow
description: Route complex software/product tasks to the right AI coding workflow, skill, tool, prerequisite check, and verification path before implementation. Use when the user asks which workflow to use, how to approach a coding task, whether to use Matt Pocock Skills, Superpowers, Codex/Claude/Cursor workflows, TDD, review, debugging, docs/search, MCP/tools, or when a task is ambiguous, multi-step, high-risk, unfamiliar, or likely to suffer from premature implementation.
---

# Choose Workflow

Route the current task. Do not implement code, create architecture docs, split issues, run setup, or start reviews while using this skill unless the user explicitly asks for that next phase after the routing decision.

This skill chooses the current smallest correct next step. It does not choose workflows from memory.

## Core Rule

First discover:

1. the user's task type
2. available repo instructions
3. available skills and tools
4. missing prerequisites for candidate workflows
5. viable verification methods

Then recommend exactly one next step and give a short preview of the rest.

## Routing Ladder

Follow this ladder in order. Do not skip to a favorite tool.

1. Intent
   - Classify the task.
   - If the user only wants a workflow, stop after routing.
   - If the user wants implementation but the task is complex, route first and identify the next phase.

2. Inventory
   - Inspect local guidance and available capabilities before recommending them.
   - Mark every relevant item as `confirmed`, `not found`, `inaccessible`, or `assumed`.
   - Do not claim a skill, MCP server, command, test runner, issue tracker, or browser flow exists without evidence.

3. Prerequisites
   - For each candidate workflow/tool/skill, check its prerequisites.
   - If a promising candidate is missing setup/configuration, recommend that setup as the next step only when it is required for the selected route.
   - Do not hard-code vendor-specific setup as a universal first step.

4. Route
   - Choose one current next step, not a whole execution chain.
   - Prefer the step that reduces uncertainty fastest while preserving user intent.
   - Include why alternatives were not selected.

5. Verify
   - Define how success of the next step will be checked.
   - Verification must be concrete: commands, files, artifact checks, screenshots, review criteria, examples, or manual acceptance points.

6. Stop
   - Stop after the routing decision.
   - Do not continue into architecture generation, issue creation, implementation, review, release, or file edits unless explicitly asked.

7. Capture
   - If the same route will be useful across tasks, suggest where to capture it: a skill, `AGENTS.md`, `CLAUDE.md`, Cursor rules, docs, or issue template.
   - Keep one-off task notes out of reusable skills.

## Task Types

Use one or more:

- `idea`: rough product or feature idea
- `existing prototype`: HTML/CSS/JS, Figma, screenshots, demo, or mockup already expresses requirements
- `existing codebase feature`: add behavior to a repo
- `bug/regression`: failure or unexpected behavior
- `refactor`: improve structure without changing behavior
- `ui migration`: visual/layout conversion
- `business logic`: calculations, validation, scoring, state transitions, data transforms
- `integration`: APIs, auth, databases, SDKs, AI models, deployment platforms
- `review`: inspect diff, architecture, spec compliance, quality, or risks
- `release`: verify, package, document, deploy, submit
- `workflow design`: user asks how to work, not for implementation
- `skill creation/update`: create or improve reusable agent skills

## Inventory Checklist

Inspect only what is relevant to the task. Prefer local evidence before assumptions.

Local guidance:

- `AGENTS.md`
- `CLAUDE.md`
- `.cursor/rules`
- `.cursorrules`
- `.windsurfrules`
- `.github/copilot-instructions.md`
- `.claude/`
- `.agents/`
- `.codex/`
- `skills/`
- `docs/`
- ADRs, `CONTEXT.md`, issue templates, README

Execution capabilities:

- package scripts
- test runner
- linter, formatter, typechecker
- build/dev commands
- browser or screenshot tools
- issue tracker or PR tooling
- MCP/docs/search tools
- installed skills/plugins

External knowledge:

- Use current official docs or primary sources when the task depends on current APIs, platform behavior, model/tool capabilities, laws, pricing, or emerging best practices.
- Use community sources to discover patterns, not as the sole authority.

## Prerequisite Checks

Use these examples as checks, not fixed workflow steps.

| Candidate | Check before recommending |
|---|---|
| Matt Pocock Skills | Are the skills installed? Is required setup/docs/issue structure present? |
| Superpowers | Are the relevant Superpowers skills available? Does the task match brainstorming, planning, TDD, debugging, review, or subagent work? |
| Codex repo workflow | Is `AGENTS.md` or project guidance present? Are verification commands known? |
| Claude Code workflow | Is `CLAUDE.md`, subagent config, MCP, or relevant skill support present? |
| Cursor workflow | Are project rules or plan-mode conventions present? |
| TDD | Is there test infrastructure and a testable logic seam? |
| Debugging | Can the failure be reproduced? Is there a minimal repro path? |
| Review | Is there a diff base, spec, issue, or acceptance criteria? |
| UI migration | Is there a source of truth and a visual verification method? |
| Prototype analysis | Is the prototype accessible? Are routes/pages/interactions inspectable? |
| API/integration | Is there an API spec, credentials/env strategy, mock, or sandbox? |
| Release | Are build, test, packaging, deploy, and rollback checks known? |
| Skill creation/update | Is the skill folder known? Is validation available? Are examples clear enough? |

If prerequisites are missing, the next step may be "set up the prerequisite" rather than "use the workflow."

## Route Selection Heuristics

- If requirements are unclear, choose clarification or discovery before planning.
- If a high-fidelity prototype exists, treat it as the source of truth; do not restart from generic PRD discovery.
- If a bug is reported, choose reproduction and diagnosis before patching.
- If business logic is central, choose examples/tests before implementation.
- If the task is visual-only, choose visual inspection or screenshot comparison over forced TDD.
- If the task is mostly workflow design, stop with a routing decision.
- If the task asks for a reusable capability, choose skill creation/update and validation.
- If current information may be stale or niche, choose docs/search before workflow commitment.
- If no candidate is sufficiently grounded, ask one focused clarifying question.

## Output Format

Produce this concise routing decision:

````markdown
# Workflow Routing Decision

## Task Type
- ...

## Inventory Matrix
| Item | Status | Evidence | Impact |
|---|---|---|---|
| ... | confirmed/not found/inaccessible/assumed | ... | ... |

## Candidate Workflows Considered
| Workflow / Skill / Tool | Fit | Prerequisites | Decision |
|---|---|---|---|
| ... | ... | ... | selected/rejected/defer |

## Recommended Next Step
[Recommend exactly one next step.]

Why:
...

Input:
...

Output:
...

Prerequisites:
...

Verification:
...

Stop Point:
...

Fallback:
...

## Full Flow Preview
1. ...
2. ...
3. ...

## Do Not Do
- ...

## First Prompt / Command
```text
...
```
````

## Success Criteria

This skill succeeds when the response:

- classifies the task
- shows evidence for available guidance/tools
- checks prerequisites before recommending tools
- recommends exactly one next step
- defines input, output, verification, stop point, and fallback
- explains what not to do
- previews later phases without executing them
- avoids hard-coded vendor or project-specific workflows

## Anti-Patterns

- Recommending a tool because the user named it, without checking fit or prerequisites.
- Turning workflow routing into architecture generation, issue creation, implementation, or review.
- Treating setup as a universal first step.
- Rewriting product requirements when a working prototype already exists.
- Producing a long menu of equally recommended options.
- Assuming unavailable skills, commands, MCP servers, or issue trackers.
- Hiding uncertainty instead of marking it as missing, inaccessible, or assumed.
