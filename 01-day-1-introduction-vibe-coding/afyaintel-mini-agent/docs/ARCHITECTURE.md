# Runtime Architecture

```mermaid
flowchart TD
    U[CLI / HTTP Client] --> O[Orchestrator]
    O --> S[Deterministic Safety Gateway]
    S -->|Blocked| H[Human Review / Emergency Referral]
    S -->|Operational| D[Validated Inventory Data]
    D --> T[Deterministic Tools]
    T --> R[English / Swahili Result]
    O -->|Only when local tools do not match| G[Optional Gemini Layer]
    G -->|Quota or network failure| F[Local Fallback]
    O --> A[Privacy-Preserving Audit Metadata]
```

## Design choices

- Safety routing occurs before model access.
- Factual inventory calculations never depend on the LLM.
- Raw prompts are not stored in audit logs.
- The HTTP server disables model calls unless `AFYAINTEL_ALLOW_MODEL=true`.
- Procurement and clinical actions remain outside the agent's permissions.
