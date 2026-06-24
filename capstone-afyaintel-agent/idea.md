# Capstone Concept — AfyaIntel Agent

## Project Title

**AfyaIntel Agent: Bilingual, Safety-Governed Health-Facility Operations Support for Low-Resource Settings**

## One-Sentence Pitch

AfyaIntel is a local-first English–Swahili operations agent that helps small health facilities monitor medicine stock, identify expiry and shortage risks, prepare management reports, and route clinical requests safely to qualified humans.

## Problem

Health-facility staff often need to make rapid operational decisions from fragmented stock records while working under connectivity, staffing, and language constraints. A generic chatbot is not dependable for this work because it may invent quantities, fail when cloud quota is unavailable, or answer clinical questions beyond its role.

AfyaIntel addresses a narrow and practical problem: turning structured stock data into reliable operational insight while preserving human authority and clinical safety.

## Target Users

- Facility in-charges
- Storekeepers and dispensing staff
- Community health workers handling administrative tasks
- District-level supervisors reviewing facility alerts

## User Needs

1. Understand current stock status quickly.
2. Identify items below minimum thresholds.
3. Detect items approaching expiry.
4. Receive concise English or Swahili summaries.
5. Produce a draft operations report for human review.
6. Avoid unsafe clinical advice from an operational assistant.
7. Continue basic work when internet access or model quota is unavailable.

## Implemented Minimum Viable Agent

The current prototype implements:

- Validated CSV stock-data ingestion
- Deterministic low-stock calculation
- Deterministic 30-day expiry analysis
- Item-specific stock lookup
- English and Swahili response routing
- Weekly operations report generation
- Pre-model clinical safety and emergency routing
- Zero-API local evaluation
- Optional Gemini language/reasoning support
- Clean fallback when the model is unavailable

## What Makes It an Agentic Engineering Project

AfyaIntel is not presented as an unconstrained chatbot. It combines:

- **Model:** optional Gemini reasoning for open-ended operational explanations
- **Tools:** stock reader, shortage detector, expiry checker, report generator
- **Context:** project rules, facility data, date, language, and safety policies
- **Orchestration:** local-first intent routing followed by optional model escalation
- **Guardrails:** deterministic clinical boundary and data validation
- **Evaluation:** repeatable local regression tests and limited live-model checks
- **Human review:** authorized staff approve operational actions

## Value Proposition

### Practical value

The prototype reduces the effort needed to interpret inventory records and create a management summary.

### Safety value

Factual stock calculations do not depend on model memory, and clinical requests are blocked before a model call.

### Inclusion value

The same operational workflow is available in English and Swahili.

### Resilience value

Essential functions continue working during Gemini quota exhaustion or connectivity problems.

### Learning value

The project demonstrates the course themes of vibe coding, agentic engineering, tool use, guardrails, evaluation, local fallback, and interoperability planning.

## Non-Goals

The current prototype does not:

- Diagnose disease or recommend treatment
- Integrate with a live DHIS2 instance
- Use real patient records
- Place medicine orders or process payments
- Claim regulatory or medical-device approval
- Replace a qualified health worker or facility manager

## Responsible Roadmap

### Next milestone

- Convert deterministic functions into explicit reusable tool contracts.
- Add Google Developer Knowledge MCP for official technical documentation only.
- Add a simple web interface using approved structured components.
- Expand the evaluation dataset with reviewed Swahili prompts.

### Future research direction

- Offline synchronization with an authorized facility database
- Human-approved DHIS2 export mapping
- Role-based access and audit logging
- A2A collaboration between stock, reporting, and supervisor-escalation agents
- Field validation with facility staff using synthetic or approved de-identified data

## Success Criteria

- 100% pass rate on deterministic stock and safety tests
- Correct English and Swahili routing in the evaluation set
- No API key or identifiable patient data in the repository
- Clean operation without Gemini for core workflows
- A reproducible demo that clearly separates implemented features from future work
