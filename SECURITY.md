# Security and Data-Protection Policy

## Secrets

- Never commit `.env`, API keys, service accounts, tokens, or credentials.
- Use `.env.example` only as a template.
- Restrict keys to the minimum required service.
- Revoke any key that appears in a message, archive, screenshot, or Git history.

## Health Data

- Use synthetic or de-identified operational data only.
- Do not enter patient names, phone numbers, addresses, record numbers, or other identifiers.
- Do not send sensitive data to untrusted models, MCP servers, A2A agents, or logs.

## Least Privilege

- Inventory tools are read-only.
- Model access is optional and disabled in the HTTP service by default.
- Procurement, payment, redistribution, record changes, and external communication require authorized human approval.

## Logging

The audit log stores:

- Timestamp
- Query hash
- Language
- Execution path
- Safety flags

It does not store the raw prompt.

## Release Security Gate

- Local evaluations pass.
- Unit tests pass.
- Secret scan returns no private key or credential.
- Threat model and red-team cases are reviewed.
- Deployment uses authenticated access and approved secret storage.
