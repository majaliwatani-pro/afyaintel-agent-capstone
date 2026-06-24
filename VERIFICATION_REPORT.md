# Verification Report — AfyaIntel Research-Integrated Capstone

Generated: 2026-06-19

## Verification summary

| Check | Result |
|---|---|
| Local deterministic evaluation | PASS — 18/18 checks |
| Python unit tests | PASS — 14/14 tests |
| HTTP health endpoint | PASS |
| HTTP summary endpoint | PASS |
| HTTP forecast endpoint | PASS |
| HTTP FHIR bundle endpoint | PASS |
| HTTP A2UI dashboard endpoint | PASS |
| Secret scan | PASS — no `.env` file or real API key included |
| Gemini dependency | Optional only; core demo uses zero Gemini API calls |

## Commands run

```bash
python3 main.py --evaluate-local
python3 -m unittest discover -s tests -v
PORT=8181 python3 server.py
```

## Local evaluation result

```text
Result: 18/18 tests passed
```

Validated areas:

- English inventory summary
- Swahili inventory summary
- Low-stock accuracy
- Expiry accuracy
- Specific-item lookup
- Clinical advice refusal
- Emergency escalation
- Weekly report generation
- Offline fallback
- Greeting without model
- Stock-out forecast baseline
- FHIR-compatible inventory bundle export
- A2UI dashboard payload generation
- Human approval matrix
- CSV validation
- Negative stock rejection
- Privacy-preserving audit log
- Tool manifest validation

## Unit tests

```text
Ran 14 tests
OK
```

## API checks

- `GET /health` returned service status.
- `GET /api/summary?lang=en` returned inventory summary.
- `GET /api/forecast?lang=en` returned stock-out risk forecast.
- `GET /api/fhir/inventory` returned a FHIR-compatible Bundle payload.
- `GET /api/dashboard` returned A2UI dashboard JSON.

## Safety boundary

The prototype remains decision support only. It does not diagnose, prescribe, treat, replace clinicians, exchange real patient data, or integrate with national systems without authorization.
