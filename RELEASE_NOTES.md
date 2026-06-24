# Release Notes — AfyaIntel 1.0.0

## Added

- Modular Python runtime
- 14-check zero-API evaluation suite
- 10 standard-library unit tests
- Privacy-preserving audit metadata
- Local HTTP API
- Dockerfile
- Agent Skill with scripts and eval cases
- MCP, A2A, and A2UI artifacts
- Threat model and red-team package
- Observability and rollback plans
- Professional responsive portfolio website
- Submission-ready capstone copy and demo script

## Changed

- Repositioned AfyaIntel as an operations-support agent, not a clinical assistant.
- Moved factual and safety-critical behavior to deterministic tools.
- Made Gemini optional.
- Updated evidence from 10/10 to 14/14 local checks.

## Security

- Removed environment-specific lock and virtual-environment files.
- Excluded `.env` and runtime audit/cache files.
- Added secret-handling and incident-response guidance.

## Known limitations

- No authenticated production deployment included.
- No live MCP or A2A connection enabled.
- Antigravity CLI, MCP, and Skill-trigger screenshots still require learner execution.
