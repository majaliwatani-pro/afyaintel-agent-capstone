# Unit 2 Podcast Notes — Agent Tools and Interoperability

## Status

Completed from the provided transcript.

## Core Lesson

Open protocols allow developers to replace fragile one-off integrations with reusable, governed connections. This changes the developer's role from maintaining custom adapters to orchestrating an interoperable agent ecosystem.

## MCP

Model Context Protocol standardizes how models discover and call tools. It reduces the model-to-tool integration problem from many custom pairings toward a shared model-plus-tool structure.

Key practices:

- Prefer trusted or official servers.
- Keep credentials out of prompts.
- Use environment variables and restricted keys.
- Load only relevant tools to avoid context overload.
- Inspect transport messages and schemas when debugging.

## A2A

Agent2Agent supports stateful collaboration with specialist agents. Unlike bounded tools, agents may negotiate, pause, request clarification, and maintain multi-turn state. Agent cards describe capabilities and data-handling expectations.

## A2UI

Agent-to-User Interface uses declarative structure rather than arbitrary executable code. A trusted client maps the structure to approved UI components.

## UCP and AP2

UCP standardizes discovery and ordering, while AP2 applies user-defined mandates and cryptographic verification to payment actions. AfyaIntel will not implement autonomous purchasing in the current prototype.

## AfyaIntel Reflection

AfyaIntel should expose narrow, permissioned tools for inventory reading, shortage calculation, expiry checking, report creation, and safety routing. Clinical and sensitive data must never be sent to an untrusted MCP server.
