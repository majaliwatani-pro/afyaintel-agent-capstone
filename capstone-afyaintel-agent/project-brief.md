# AfyaIntel Agent — Project Brief

## Title

**AfyaIntel Agent: Bilingual, Local-First Health-Facility Operations Support for Low-Resource Settings**

## Builder

Majaliwa Tani Mabirika

## Problem

Small health facilities often manage essential medicines and supplies through paper records, disconnected spreadsheets, and manual reporting. Limited connectivity and language barriers can delay shortage detection, expiry review, and management action.

## Solution

AfyaIntel is a local-first operations agent that reads validated inventory data, identifies low-stock and expiry risks, generates English or Swahili management reports, and routes clinical requests to qualified human professionals.

## Differentiator

The project does not treat a language model as the source of truth. Deterministic Python tools handle factual stock calculations and safety routing. Gemini is optional and used only for non-clinical language support. The core workflow continues when the model quota or network is unavailable.

## Intended Users

- Facility managers
- Storekeepers
- District supply supervisors
- Authorized health-program staff

## Non-Users / Non-Goals

- Patients seeking diagnosis or treatment
- Autonomous procurement or payment systems
- Real patient-record processing
- Replacement for clinical judgment

## Implemented Capabilities

- Validated CSV inventory ingestion
- Low-stock calculation
- 30-day expiry-risk calculation
- Item-level status lookup
- English and Swahili summaries
- Weekly management report
- Clinical-safety and emergency routing
- Local zero-API evaluation
- Privacy-preserving audit metadata
- HTTP API and Docker deployment path
- Agent Skill, tool manifest, agent card, and A2UI schema

## Evidence

- Automated local evaluation
- Python unit tests
- Tool contracts
- Threat model and red-team cases
- Demo script
- Portfolio website

## Responsible AI Position

AfyaIntel is a learning prototype for operational decision support. It does not diagnose disease, prescribe medicines, recommend doses, or execute procurement, redistribution, payments, or external communication without authorized human approval.
