# AfyaIntel Demonstration Script

Target length: 3–5 minutes.

## 1. Problem and value

> Small facilities can miss stock shortages and expiry risks because records are fragmented, connectivity is limited, and reporting is manual. AfyaIntel provides bilingual, local-first operational support without replacing clinical judgment.

## 2. Show the project structure

Highlight:

- `AGENTS.md`
- `tool_manifest.json`
- `.agents/skills/afyaintel-stock-operations/`
- `04-day-4-security-evaluation/`
- `05-day-5-production-deployment/`

## 3. Run evaluation

```powershell
uv run python main.py --evaluate-local
```

Explain that the suite uses zero Gemini calls.

## 4. Run the scripted demo

```powershell
uv run python main.py --demo
```

Show:

- Greeting
- Low-stock detection
- Expiry alerts
- Swahili report
- Clinical safety refusal

## 5. Run interactive examples

```powershell
uv run python main.py --interactive
```

Prompts:

1. `Which items are low in stock?`
2. `Ni bidhaa gani zinaisha muda?`
3. `Tengeneza ripoti ya wiki kwa Kiswahili.`
4. `Mgonjwa ana homa. Nimpe dawa gani?`

## 6. Show API readiness

```powershell
uv run python server.py
```

Then show `/health` and one local API response.

## 7. Close with responsible scope

> AfyaIntel drafts operational insights. Human staff approve procurement, redistribution, communication, and every clinical action. The prototype uses synthetic data and is not a medical device.
