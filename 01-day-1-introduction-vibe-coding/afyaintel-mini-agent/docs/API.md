# AfyaIntel Local HTTP API

The HTTP service uses Python's standard library and keeps model access disabled by default.

## Start

```powershell
$env:PORT = "8080"
uv run python server.py
```

## Endpoints

- `GET /health` — service health and operating mode.
- `GET /api/summary?lang=en|sw` — deterministic inventory summary.
- `GET /api/report?lang=en|sw` — deterministic weekly operations report.
- `POST /api/query` — orchestrated query with safety routing.

Example body:

```json
{"query": "Dawa zipi zimepungua?"}
```

## Production boundary

Before public deployment, add authentication, HTTPS-only access, request-size controls at the platform edge, centralized audit storage, and an approved secret manager. Do not use real patient data.
