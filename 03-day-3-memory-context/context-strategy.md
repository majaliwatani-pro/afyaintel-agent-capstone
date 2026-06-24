# AfyaIntel Context Strategy

## Static context

Always available:

- `AGENTS.md`
- Security boundaries
- Product scope
- Coding conventions
- Human-approval rules

## Dynamic context

Loaded only when needed:

- Inventory CSV
- AfyaIntel stock-operations Skill
- Official technical documentation through approved MCP
- Optional Gemini explanation context

## Context minimization rules

- Do not place the full CSV in the system prompt.
- Do not preload every tool schema.
- Retrieve only the tool or skill relevant to the current task.
- Do not include patient-identifiable information.
- Prefer deterministic outputs for inventory values.

## Memory boundary

The prototype does not maintain patient memory or personal profiles. Its only persistent metadata is privacy-preserving execution audit data and optional cached non-clinical model responses.
