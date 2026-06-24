# AfyaIntel Threat Model

## Assets

- Inventory data
- API credentials
- Operational reports
- Audit records
- Human approval decisions
- Source code and configuration

## Trust Boundaries

1. User input to orchestrator
2. Orchestrator to deterministic tools
3. Orchestrator to optional Gemini API
4. Future MCP or A2A connections
5. Local files to deployment environment

## Primary Threats and Controls

| Threat | Example | Control | Residual risk |
|---|---|---|---|
| Secret exposure | API key committed to ZIP | `.gitignore`, `.env.example`, secret scan, key rotation | Human error remains possible |
| Prompt injection | User asks agent to ignore safety | Deterministic safety gateway before model call | New phrasing may require updated tests |
| Data exfiltration | Untrusted MCP requests files | MCP allowlist, least privilege, no patient data | Future integrations require review |
| Hallucinated stock | Model invents quantities | Inventory values come only from deterministic tools | Source CSV can still be wrong |
| Unauthorized action | Agent orders medicine | No write/payment tools; human approval required | Future action tools need authorization |
| Audit privacy leak | Raw prompt stored in logs | Store only query hash and execution metadata | Hashes are not anonymous against tiny known inputs |
| Denial of service | Huge request body | Server body-size limit and platform controls | Local CLI can still receive long input |
| Dependency compromise | Malicious package | Minimal dependencies, pinned review, clean lock generation | Supply-chain risk is not eliminated |

## Safety Invariants

- No diagnosis or prescription.
- Emergency prompts are escalated immediately.
- No identifiable patient data.
- No autonomous procurement, payments, or stock modification.
- No raw provider errors shown to users.
- Core functions remain usable without Gemini.
