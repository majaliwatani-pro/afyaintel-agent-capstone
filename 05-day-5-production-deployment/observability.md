# Observability Plan

## Metrics

- Request count by execution path
- Safety-routed request count
- Emergency escalation count
- Data-validation failures
- Model success, cache-hit, and quota-fallback counts
- Response latency
- HTTP error rate

## Traces

A trace should show:

1. Language route
2. Safety decision
3. Data validation
4. Tool selected
5. Model call only when required
6. Human-review boundary

Do not include patient identifiers, API keys, or raw clinical prompts.

## Logs

The prototype records:

- Timestamp
- Query hash
- Language
- Execution path
- Safety flags

The raw query is intentionally excluded.

## Alerts

- Repeated data validation failures
- Unexpected increase in model errors
- Any attempted write or payment action
- Any secret detection
- Safety test regression
