# Whitepaper Notes — The New SDLC with Vibe Coding

## Status

Completed

## Main Thesis

Software engineering is shifting from writing syntax to expressing intent. AI can compress implementation time, but specification quality, architecture, verification, and human judgment become more important.

## Key Concepts

### Vibe coding to agentic engineering

Vibe coding is useful for rapid exploration, while production work needs formal context, tests, evaluations, guardrails, and human oversight.

### Agent equals model plus harness

A model becomes useful as an agent only when surrounded by tools, context, memory, orchestration, sandboxes, evaluation, observability, and enforceable constraints.

### Context engineering

Good outputs depend on relevant instructions, knowledge, memory, examples, tools, and guardrails. Static context should contain durable rules; dynamic context should be loaded only when relevant.

### AI-driven SDLC

Implementation can collapse from weeks to hours or minutes, but requirements, architecture, review, and correctness remain human responsibilities.

### Factory model

The developer designs the system that produces and verifies code. The output is not only code; it is the specification, harness, tests, and feedback loop.

### Conductor and orchestrator

A conductor directs real-time work closely. An orchestrator delegates well-defined work and evaluates results at a higher level.

## AfyaIntel Application

The project was redesigned around these principles:

- Deterministic tools for stock facts
- Safety routing before model access
- Local fallback during quota exhaustion
- Explicit human approval
- Repeatable evaluation
- Honest separation of implementation and roadmap

## Reflection

The strongest lesson is that generation is not the main difficulty. Verification, judgment, direction, and accountability are the new engineering craft.
