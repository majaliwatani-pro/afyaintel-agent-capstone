# AfyaIntel Agent

## Bilingual, Local-First Health-Facility Operations Support

### Executive Summary

AfyaIntel is a safety-governed AI agent prototype designed to help low-resource health facilities monitor medicine and supply stock, identify expiry risks, and prepare English or Swahili operational reports. It addresses a practical constraint: essential workflows should remain available when internet connectivity or model quota is unavailable.

The system follows an agentic engineering approach. Deterministic Python tools calculate factual inventory results, a pre-model safety gateway blocks diagnosis and prescription requests, privacy-preserving audit metadata supports accountability, and human approval remains mandatory for procurement, redistribution, communication, and clinical decisions. Gemini is optional and never serves as the source of truth for inventory values.

### The Problem

Small facilities may rely on paper registers, disconnected spreadsheets, and manual reporting. Staff can spend valuable time identifying shortages, reviewing expiry dates, and preparing updates for supervisors. Cloud-only assistants are also vulnerable to connectivity, cost, and quota limitations.

### The Solution

AfyaIntel provides:

- Validated inventory ingestion
- Low-stock and expiry analysis
- Bilingual management summaries
- Item-level lookup
- Weekly report generation
- Clinical-safety and emergency routing
- Local fallback when Gemini is unavailable
- A deployment-ready HTTP service

### Agentic Engineering

The project demonstrates:

- **Intent and scope:** operational support with explicit non-goals
- **Context engineering:** global rules, structured data, references, and on-demand Skills
- **Tools:** deterministic inventory, reporting, safety, and auditing functions
- **Interoperability:** MCP policy, A2A agent-card draft, and A2UI schema
- **Memory discipline:** no patient memory; only privacy-safe metadata and optional non-clinical cache
- **Evaluation:** repeatable zero-API tests, unit tests, red-team cases, and human rubric
- **Production thinking:** health endpoint, Dockerfile, observability, rollback, and access-control requirements

### Course Alignment

| Course area | AfyaIntel evidence |
|---|---|
| Day 1 — Vibe coding to agentic engineering | Working prototype, `AGENTS.md`, deterministic harness, evaluation |
| Day 2 — Tools and interoperability | Tool contracts, MCP policy, agent card, A2UI schema |
| Day 3 — Agent Skills and context | Portable Skill with scripts, references, and eval cases |
| Day 4 — Security and evaluation | Threat model, red-team suite, audit privacy, approval matrix |
| Day 5 — Production deployment | HTTP API, Dockerfile, observability and rollback plans |

### Results

The local evaluation validates stock accuracy, bilingual responses, safety routing, invalid-data rejection, audit privacy, and tool-manifest integrity without consuming Gemini quota. Unit tests independently verify core behavior.

### Limitations

- Synthetic single-facility CSV data
- Rule-based language and safety detection
- No authenticated production deployment in this archive
- No real MCP or A2A connection enabled
- No real patient data, clinical guidance, payment, or procurement execution

### Roadmap

1. Complete local Antigravity CLI, MCP, and Skill-trigger evidence.
2. Add authenticated role-based access.
3. Replace CSV with an approved facility inventory API.
4. Add reviewed terminology and multilingual quality evaluation.
5. Pilot only after security, legal, clinical, and data-governance approval.

### Conclusion

AfyaIntel shows that a valuable health-operations agent does not need to depend on unrestricted model autonomy. By combining deterministic tools, bilingual support, safety gates, human approval, evaluation, and local resilience, the project presents a credible path from course prototype to responsible operational pilot.


## Research Integration

AfyaIntel is grounded in a Design Science Research manuscript that frames the broader artifact as an offline-first generative health intelligence, clinical NLP, predictive supply-chain, and interoperability framework for low-resource Tanzanian primary healthcare settings. The capstone prototype implements a safe and testable slice of that vision: inventory intelligence, bilingual reporting, clinical safety routing, synthetic NLP cue extraction, stock-out risk forecasting, FHIR-compatible export, and human governance controls.

The prototype intentionally remains within a decision-support boundary. It does not claim diagnostic accuracy, prescription authority, national-platform integration, or real-patient validation. Those require ethical clearance, institutional authorization, clinical review, and controlled pilot evaluation.

## Prototype-to-Pilot Path

1. Validate synthetic workflows and local evaluation.
2. Conduct clinician review of safety responses and Swahili/Swanglish terminology.
3. Test de-identified historical stock data where authorized.
4. Validate FHIR mappings against approved national or partner requirements.
5. Run a controlled facility pilot only after governance approval.
