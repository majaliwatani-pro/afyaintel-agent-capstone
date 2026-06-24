# Day 3 — Agent Skills, Context, and Procedural Memory

## Learning Objective

Turn repeated, reliable workflows into on-demand Agent Skills so the agent receives specialized instructions only when relevant.

## AfyaIntel Day 3 Extension

The project includes a portable skill at:

```text
.agents/skills/afyaintel-stock-operations/
```

The skill packages:

- Trigger metadata
- Stock-validation workflow
- Local evaluation command
- Safety boundaries
- Tool-contract references
- Positive and negative routing cases

## Why a Skill Instead of More Global Prompt Text?

`AGENTS.md` contains always-on project rules. The AfyaIntel skill contains narrow procedural knowledge for inventory validation, stock alerts, expiry checks, reporting, and local evaluations. Loading this only when needed reduces context bloat.

## Completion Boundary

The skill files and local scripts are complete. A final Antigravity screenshot is still required to prove that the installed skill triggered from a natural-language prompt.
