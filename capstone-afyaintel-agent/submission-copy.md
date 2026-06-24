# AfyaIntel Capstone Submission Copy

## Title

AfyaIntel Agent: Offline-First Bilingual Health-Facility Intelligence for Low-Resource Settings

## Short description

AfyaIntel is a local-first AI agent prototype that helps health-facility staff monitor medicine stock, detect shortages and expiry risks, generate English/Swahili operational reports, and route clinical questions to qualified human review. It is designed for low-resource Tanzanian primary-care workflows where connectivity, staffing, and stock reporting are constrained.

## What makes it valuable

AfyaIntel is not a general chatbot. It uses deterministic tools for factual inventory and safety-critical behavior, while Gemini remains optional for non-clinical language support. The system continues working when model quota or internet access is unavailable. It demonstrates agentic engineering through structured context, tool contracts, evaluation, human approval controls, privacy-preserving audit metadata, FHIR-compatible export, A2A/A2UI interoperability artifacts, and a responsible pilot roadmap.

## Research foundation

The project is grounded in an AfyaIntel Hub Design Science Research manuscript focused on offline-first clinical workflow support, Swahili/Swanglish clinical NLP, predictive pharmaceutical supply chains, HL7 FHIR interoperability, and human-in-the-loop governance.

## Current prototype capabilities

- Bilingual English/Swahili operations support
- Inventory summary and item lookup
- Low-stock and expiry detection
- Transparent stock-out risk forecast baseline
- Clinical safety gateway and emergency escalation
- Human approval matrix
- FHIR-compatible inventory bundle export
- De-identified sync queue simulation
- A2UI dashboard payload generation
- Local HTTP API and Docker deployment path
- Repeatable local evaluation without Gemini API calls

## Responsible AI boundary

AfyaIntel does not diagnose disease, prescribe medicine, provide dosage instructions, replace licensed health workers, or exchange real patient data. It is a decision-support and operational-intelligence prototype for synthetic or authorized de-identified data only.

## Why this matters

Low-resource facilities need tools that work offline, support local language, reduce reporting friction, and make medicine-stock pressure visible earlier. AfyaIntel shows how agentic AI can become practical, safe, and locally relevant when grounded in deterministic tools, clinical governance, and interoperability standards.
