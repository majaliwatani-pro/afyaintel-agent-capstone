# Day 3 Whitepaper Notes — Agent Skills

## Status

Completed from the supplied Agent Skills whitepaper.

## Definition

An Agent Skill is a portable folder anchored by `SKILL.md`, with optional `scripts/`, `references/`, and `assets/`. It gives a general-purpose agent specialist competence on demand.

## Problems Skills Address

1. **Context rot:** too many always-on instructions can reduce model performance.
2. **Procedural memory:** skills preserve how to complete a workflow, not just facts about it.
3. **Multi-agent overload:** one agent can flex into multiple specialist roles without a separate deployed agent for every task.
4. **Portability:** a lightweight folder can move across compatible tools and vendors.

## Progressive Disclosure

The router initially sees only lightweight metadata. Detailed instructions and scripts are loaded only when the user's request matches the skill. This reduces token use and irrelevant context.

## Skills, MCP, and AGENTS.md

- `AGENTS.md` is always-loaded project context and global rules.
- A Skill is on-demand procedural know-how.
- MCP provides reach to external systems and data.
- A Skill may instruct an agent how and when to use an MCP tool.

## Evaluation-Driven Development

A reliable skill should be designed from test cases first. Each case should define:

- Input
- Expected skill
- Expected tool trajectory
- Expected output format
- Rubric

The skill must be tested for:

- Trigger failure
- Execution failure
- Token-budget failure
- Regression against other skills

## AfyaIntel Application

The AfyaIntel stock-operations skill has:

- Three positive trigger cases
- Three negative trigger cases
- Deterministic validation scripts
- Explicit prohibition of diagnosis and prescriptions
- Local evaluation with zero Gemini calls

## Reflection

> A skill without a test is documentation, not a dependable capability.
