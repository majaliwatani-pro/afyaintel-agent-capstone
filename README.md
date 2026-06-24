# AfyaIntel Agent — Professional Kaggle AI Agents Capstone

**Project:** AfyaIntel Agent: Bilingual, Local-First Health-Facility Operations Support for Low-Resource Settings  
**Course:** Kaggle 5-Day AI Agents: Intensive Vibe Coding Course With Google  
**Builder:** Majaliwa Tani Mabirika  
**Version:** 1.1.0 Research-Integrated Edition  
**Status:** Working local prototype; professional capstone package; external codelab evidence still to be captured

## Executive Summary

AfyaIntel helps authorized health-facility staff understand medicine and supply stock, identify expiry risk, and draft English or Swahili operations reports. It is designed around a simple principle: factual and safety-critical behavior should remain deterministic, testable, and available even when a model, network, or free-tier quota is unavailable.

The project demonstrates agentic engineering through explicit context, structured tools, clinical guardrails, privacy-preserving audit metadata, human approval, Agent Skills, interoperability artifacts, automated evaluation, and deployment readiness.

## Why It Matters

Small facilities may use paper registers or disconnected spreadsheets, while staff manually prepare shortage and expiry reports. A useful agent for this context must be:

- **Local-first:** essential workflows continue without model access.
- **Bilingual:** English and Swahili operational support.
- **Grounded:** stock values come from validated structured data.
- **Safety-governed:** no diagnosis, prescription, dosage, or treatment.
- **Human-supervised:** no autonomous procurement, payment, redistribution, or communication.
- **Evaluated:** claims are backed by repeatable local and unit tests.

## Working Capabilities

- Validates a single-facility inventory CSV.
- Detects stock below minimum thresholds.
- Detects items expiring within 30 days.
- Looks up specific inventory items.
- Generates English and Swahili summaries.
- Generates a management-ready weekly report.
- Routes clinical and emergency requests to human professionals.
- Handles Gemini quota failures without breaking core workflows.
- Records privacy-safe execution metadata without raw prompts.
- Exposes a local HTTP API and Docker deployment path.

## Course Concept Map

| Day | Concept | AfyaIntel evidence |
|---|---|---|
| 1 | Vibe coding → agentic engineering | Working harness, deterministic tools, guardrails, local evaluation |
| 2 | Tools and interoperability | Tool contracts, MCP policy, A2A agent card, A2UI schema |
| 3 | Agent Skills and context | Portable stock-operations Skill, scripts, references, eval cases |
| 4 | Security and evaluation | Threat model, red-team cases, privacy audit, human approval matrix |
| 5 | Production lifecycle | HTTP API, Dockerfile, observability and rollback plans |

## Quick Start

```powershell
Set-Location -Path "C:\Users\cohema\agy2-projects\kaggle-5day-ai-agents-2026\01-day-1-introduction-vibe-coding\afyaintel-mini-agent"
uv sync
uv run python main.py --evaluate-local
uv run python -m unittest discover -s tests -v
uv run python main.py --demo
```

Interactive mode:

```powershell
uv run python main.py --interactive
```

Portfolio website:

```powershell
Set-Location -Path "C:\Users\cohema\agy2-projects\kaggle-5day-ai-agents-2026\portfolio"
python -m http.server 8000
```

Open `http://localhost:8000`.

## Repository Map

```text
00-admin/                              Course setup and links
01-day-1-introduction-vibe-coding/     Learning evidence and working application
02-day-2-tools-interoperability/       Protocol notes and interoperability artifacts
03-day-3-memory-context/               Context strategy and Agent Skill evidence
04-day-4-security-evaluation/          Threat model, red team, rubric, incident response
05-day-5-production-deployment/        HTTP, Docker, observability, rollback, deployment guide
.agents/skills/                        Portable AfyaIntel Agent Skill
capstone-afyaintel-agent/              Submission-oriented capstone documents
portfolio/                             Professional responsive portfolio website
screenshots/                            Evidence assets
errors-and-fixes/                      Reproducible troubleshooting notes
```

## Capstone Assets

- [`capstone-afyaintel-agent/final-writeup.md`](capstone-afyaintel-agent/final-writeup.md)
- [`capstone-afyaintel-agent/project-brief.md`](capstone-afyaintel-agent/project-brief.md)
- [`capstone-afyaintel-agent/portfolio-case-study.md`](capstone-afyaintel-agent/portfolio-case-study.md)
- [`capstone-afyaintel-agent/submission-copy.md`](capstone-afyaintel-agent/submission-copy.md)
- [`capstone-afyaintel-agent/demo-script.md`](capstone-afyaintel-agent/demo-script.md)
- [`CERTIFICATION_READINESS.md`](CERTIFICATION_READINESS.md)

## Completion Honesty

The code and capstone package are complete as a local professional prototype. The repository does not falsely claim that Antigravity CLI, Google Developer Knowledge MCP, Skill-trigger screenshots, cloud deployment, or the official Kaggle capstone submission have already been completed. Those actions must be performed and evidenced by the learner.

## Responsible Scope

AfyaIntel is a learning prototype, not a medical device. Use synthetic or de-identified operational data only. Qualified professionals remain responsible for all clinical and operational decisions.


## Research-Integrated Edition

This version integrates the AfyaIntel Hub DSRM research manuscript into the working capstone prototype. The prototype now includes deterministic demonstrations of clinical NLP cue extraction, transparent stock-out forecasting, FHIR-compatible inventory export, de-identified synchronization queueing, an A2UI dashboard payload, and a human approval matrix.

Additional research-aligned documents:

- `docs/research/RESEARCH_TO_PROTOTYPE_TRACEABILITY.md`
- `docs/implementation/PILOT_DOSSIER.md`
- `docs/implementation/GRANT_AND_PARTNERSHIP_BRIEF.md`
- `docs/implementation/DATA_PROTECTION_IMPACT_CHECKLIST.md`
- `VISION_2030.md`

Run the expanded evaluation:

```powershell
uv run python main.py --evaluate-local
uv run python -m unittest discover -s tests -v
uv run python main.py --demo
```
