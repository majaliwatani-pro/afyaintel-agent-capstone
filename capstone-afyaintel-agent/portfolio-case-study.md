# Portfolio Case Study — AfyaIntel

## Role

Product designer, agent engineer, evaluator, and documentation author.

## Challenge

Design an AI agent that is useful in a low-connectivity health-facility context while avoiding clinical overreach and free-tier model dependency.

## Approach

I separated the system into a deterministic operational core and an optional generative layer. The deterministic core reads structured stock data, computes shortage and expiry risk, generates bilingual reports, and enforces clinical safety. The generative layer is used only for non-clinical explanations and can fail without stopping the product.

## Key Decisions

- Local-first instead of cloud-only
- Deterministic facts instead of model-generated numbers
- Safety routing before model access
- Human approval instead of autonomous action
- Query hashes instead of raw prompt logs
- On-demand Agent Skill instead of loading every instruction globally

## Technical Highlights

- Python 3.12
- `uv` dependency workflow
- Gemini API as an optional layer
- Standard-library HTTP API
- Docker deployment artifact
- JSON tool manifest, agent card, and A2UI schema
- Automated and human evaluation framework

## Outcome

The result is a reproducible prototype that demonstrates course concepts across the full agent lifecycle and can be shown through a professional portfolio site, a short demo, and verifiable test evidence.
