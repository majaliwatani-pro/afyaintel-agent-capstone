# AfyaIntel Evaluation Plan

## Evaluation Goals

1. Inventory outputs exactly match the source data.
2. Clinical and emergency prompts are safely routed.
3. English and Swahili paths remain understandable.
4. The core product works without Gemini.
5. Invalid data is rejected rather than guessed.
6. Audit metadata excludes raw prompts.
7. Tool contracts and human-approval boundaries remain explicit.

## Automated Evaluation

Run:

```powershell
uv run python main.py --evaluate-local
uv run python -m unittest discover -s tests -v
```

The local suite makes zero Gemini calls and covers:

- Inventory summaries
- Low-stock accuracy
- Expiry accuracy
- Item lookup
- Bilingual routing
- Clinical refusal
- Emergency escalation
- Weekly report quality
- Offline fallback
- CSV schema validation
- Negative stock rejection
- Audit privacy
- Tool manifest validation

## Optional Live Evaluation

```powershell
uv run python main.py --evaluate-live
```

This makes at most two Gemini calls and is not required for deterministic correctness.

## Red-Team Evaluation

Use `04-day-4-security-evaluation/red-team-cases.json` to probe:

- Prompt injection
- Diagnosis and dosage requests
- Emergency escalation
- Secret extraction
- Sensitive-data exfiltration
- Unauthorized stock changes
- Autonomous procurement or payment
- Fabricated data
- Untrusted MCP access

## Human Review

A reviewer should score factual accuracy, safety, bilingual quality, tool trajectory, resilience, privacy, oversight, and reproducibility using the Day 4 rubric.

## Release Gate

- All automated checks pass
- Safety tests pass at 100%
- No secret is present
- No raw prompt is stored in audit logs
- No feature is claimed without evidence
- Deployment remains authenticated and reversible
