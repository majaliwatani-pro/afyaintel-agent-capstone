# AfyaIntel Mini-Agent

A bilingual, local-first health-facility operations agent that demonstrates deterministic tools, optional Gemini support, clinical safety routing, privacy-preserving audit metadata, evaluation, and deployment readiness.

## Scope

AfyaIntel may:

- Read validated synthetic inventory data
- Detect low-stock and expiry risk
- Generate English and Swahili operational summaries
- Draft weekly management reports
- Route clinical and emergency requests to humans

AfyaIntel must not:

- Diagnose disease
- Prescribe or recommend treatment or dosage
- Process identifiable patient data
- Change inventory records
- Place orders, pay suppliers, or send messages autonomously

## Requirements

- Python 3.12+
- `uv`
- Optional Gemini API key for live non-clinical explanations

## Setup

```powershell
Set-Location -Path "C:\Users\cohema\agy2-projects\kaggle-5day-ai-agents-2026\01-day-1-introduction-vibe-coding\afyaintel-mini-agent"
uv sync
```

## Run

Local evaluation:

```powershell
uv run python main.py --evaluate-local
```

Unit tests:

```powershell
uv run python -m unittest discover -s tests -v
```

Scripted demo:

```powershell
uv run python main.py --demo
```

Interactive CLI:

```powershell
uv run python main.py --interactive
```

Local HTTP API:

```powershell
uv run python server.py
```

Optional live model checks:

```powershell
uv run python main.py --evaluate-live
```

## Architecture

```text
User → Orchestrator → Safety Gateway → Validated Data → Deterministic Tools
                                └────→ Human Referral
No local tool match → Optional Gemini → Cache / Quota-safe Local Fallback
Every path → Privacy-preserving audit metadata
```

## Key Files

- `afyaintel/` — modular runtime
- `tests/` — standard-library unit tests
- `sample_stock.csv` — synthetic demo inventory
- `tool_manifest.json` — tool contracts
- `agent-card.json` — future A2A discovery contract
- `a2ui-dashboard.schema.json` — safe UI intent schema
- `server.py` — local HTTP service
- `Dockerfile` — deployment artifact
- `eval_report.md` / `eval_report.json` — generated evidence

## Environment

Copy the workspace root `.env.example` to `.env` and keep it private.

```env
GEMINI_API_KEY=your_private_key
GEMINI_MODEL=gemini-2.5-flash-lite
AFYAINTEL_REFERENCE_DATE=2026-06-15
AFYAINTEL_ALLOW_MODEL=false
```

The core product does not need a model key.

## Data and Safety

This is a learning prototype using synthetic data. It is not a medical device and must not be used to make clinical decisions.
