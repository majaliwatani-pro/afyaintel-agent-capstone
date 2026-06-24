# AGENTS.md — AfyaIntel Engineering Contract

## Mission

Build and maintain a bilingual, local-first health-facility operations assistant for stock monitoring, expiry review, reporting, and safe human escalation.

## Hard Boundaries

AfyaIntel must not:

- Diagnose a condition.
- Prescribe or recommend a medicine, treatment, or dosage.
- Process identifiable patient data.
- Invent missing inventory values.
- Change stock records without explicit authorized workflow.
- Order, pay, redistribute, or communicate externally without human approval.
- Reveal secrets or inspect `.env` unless the user explicitly asks for a safe local check.

## Engineering Principles

1. Deterministic before generative.
2. Ground every inventory fact in validated data.
3. Route safety before any model call.
4. Keep core workflows available offline.
5. Apply least privilege to every tool.
6. Store only privacy-preserving audit metadata.
7. Separate implemented features from roadmap items.
8. Require repeatable evaluation before release.

## Development Commands

```powershell
uv sync
uv run python main.py --evaluate-local
uv run python -m unittest discover -s tests -v
uv run python main.py --demo
uv run python server.py
```

## Project Skill Catalog

### `afyaintel-stock-operations`

Use for inventory validation, low-stock and expiry analysis, bilingual operations reports, tool-contract review, and zero-API evaluation. Do not use for clinical advice, payments, or unrelated software tasks.

Path:

```text
.agents/skills/afyaintel-stock-operations/
```

## Documentation Rule

Never mark a codelab, deployment, protocol connection, or official submission as complete without direct evidence.
