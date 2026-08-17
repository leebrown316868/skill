---
name: choose-workflow
description: Choose the next workflow, skill, or tool for software and product work. Use when the user explicitly asks how to approach a task or which workflow to use, or when implementation is materially blocked by unclear requirements, missing prerequisites, or a consequential choice between viable workflows. Do not invoke merely because a task is multi-step, unfamiliar, or complex when the repository's normal workflow can proceed safely.
---

# Choose Workflow

Choose the smallest correct next step using evidence from the current task and environment.

Do not implement, create plans or architecture artifacts, open issues, or start reviews when the user asks only for workflow advice. When the user already asked for implementation, route briefly and continue into the selected step unless a decision, prerequisite, or authorization genuinely blocks progress.

## Process

1. **Identify intent**
   - Classify what the user wants now: advice, diagnosis, implementation, review, release, or reusable workflow design.
   - Determine whether routing is the deliverable or only the first implementation decision.

2. **Inspect relevant evidence**
   - Read only the repository guidance and capability information that could change the route.
   - Check candidate prerequisites before recommending a skill, tool, command, issue tracker, or browser flow.
   - Distinguish confirmed facts from assumptions. Report only uncertainty that affects the decision.

3. **Compare viable routes**
   - Consider only plausible candidates, not an exhaustive catalog.
   - Prefer the route that reduces the most important uncertainty while preserving the user's requested outcome.
   - Reject a named tool when its prerequisites are absent or another route fits materially better.

4. **Select one next step**
   - State one concrete action, its required input, and its expected output.
   - Define a concrete verification or acceptance check.
   - Preview later phases only when that helps the user understand the handoff.

5. **Continue or stop**
   - If the user asked only for routing, stop after the recommendation.
   - If the user asked for execution and the next step is authorized and available, continue with it.
   - Stop and ask one focused question only when the answer would materially change the route and cannot be discovered safely.

## Common Routing Rules

| Situation | Prefer first |
|---|---|
| Requirements or destination are unclear | Focused clarification, discovery, or grilling |
| Effort is too large for one session and the path is still unclear | A decision-mapping workflow such as Wayfinder, after checking its tracker and skill prerequisites |
| A high-fidelity prototype already defines behavior | Inspect the prototype and derive acceptance criteria |
| Bug or regression | Reproduce and diagnose before patching |
| Business logic or data transformation | Concrete examples or tests before implementation |
| Visual-only change | Visual inspection and screenshot comparison |
| API, SDK, platform, or model behavior may have changed | Current official documentation or primary sources |
| Refactor | Establish behavior-preserving checks before editing |
| Review | Confirm the diff base, specification, or acceptance criteria |
| Release | Verify build, tests, packaging, deployment, and rollback expectations |
| Reusable agent capability | Skill creation or update plus validation |

Treat these as defaults, not a fixed pipeline. Do not force TDD onto work without a useful test seam, restart product discovery when an accessible prototype is already the source of truth, or recommend setup that the selected route does not require.

## Evidence to Inspect

Inspect only relevant sources, for example:

- repository instructions such as `AGENTS.md`, `CLAUDE.md`, or editor rules
- installed skills, plugins, MCP servers, and available tools
- package scripts, test runners, linters, typecheckers, and build commands
- existing specs, ADRs, issue templates, prototypes, screenshots, or diffs
- issue tracker, browser, credentials, environment, or deployment prerequisites
- current official documentation when facts may be stale

Use `confirmed`, `not found`, `inaccessible`, or `assumed` internally. Include those labels in the response only when they clarify a consequential limitation.

## Output Scale

Match the response to the decision.

### Quick route

Use by default when the evidence and choice are straightforward:

```markdown
Recommended next step: <one action>

Why: <brief evidence-based reason>
Verify: <concrete success check>
Then: <optional one-line preview or continuation>
```

### Decision report

Use only when the user asks for a comparison, the choice is consequential, or missing prerequisites materially affect it:

```markdown
# Workflow Decision

Task: <type and intended outcome>

Evidence:
- <relevant confirmed fact or consequential uncertainty>

Candidates:
- <selected route> — <why it fits>
- <rejected or deferred route> — <why not now>

Recommended next step: <one action>
Input: <what it needs>
Output: <what it produces>
Verify: <concrete check>
Stop/continue: <what happens after this decision>
Fallback: <only if the selected route may be unavailable>
```

Do not produce an inventory matrix, candidate matrix, full-flow plan, warning list, or starter prompt unless it materially improves the user's decision or they request it.

## Success Criteria

The route is successful when it:

- reflects the user's immediate intent
- relies on relevant, checked capabilities and prerequisites
- chooses exactly one current next step
- defines a concrete verification method
- explains a consequential rejection or uncertainty without dumping the full inventory
- stops for workflow-only requests and continues for authorized execution requests

## Failure Modes

- Triggering on every complex or multi-step task.
- Turning a small decision into a workflow report.
- Recommending a named or familiar tool without checking fit and prerequisites.
- Listing several equally recommended options instead of choosing.
- Treating setup as a universal first step.
- Routing forever when the user already authorized implementation.
- Continuing into implementation when the user asked only for advice.
