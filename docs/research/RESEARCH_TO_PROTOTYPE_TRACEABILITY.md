# Research-to-Prototype Traceability Matrix

This document maps the AfyaIntel Hub DSRM research manuscript into the working Kaggle capstone prototype.

## Research foundation

The research manuscript defines AfyaIntel Hub as an offline-first generative health intelligence, clinical NLP, predictive supply-chain, and interoperability framework for low-resource primary healthcare settings in Tanzania. The clinical boundary is explicit: the artifact is decision support only and does not replace licensed professionals, clinical judgment, regulatory authorization, or national EMR systems.

## Traceability

| DSRM research component | Prototype evidence | Status |
|---|---|---|
| Offline-first workflows | CSV-backed local tools; zero-API evaluations; deterministic fallback | Implemented in capstone prototype |
| Local clinical NLP gateway | Rule-based Swahili/Swanglish cue extraction and red-flag vocabulary | Implemented as safe prototype; transformer model is roadmap |
| Predictive supply-chain engine | Transparent stock-out risk baseline using current stock and daily issue averages | Implemented as explainable baseline; XGBoost/Prophet remain pilot roadmap |
| FHIR interoperability | Demo FHIR-compatible inventory Bundle export | Implemented as demonstration; formal validation required before integration |
| Sync queue | De-identified stock-summary queue for later upload | Implemented as local demo queue |
| Governance and safety | Clinical safety gateway, approval matrix, privacy-preserving audit metadata | Implemented |
| Evaluation | Local deterministic tests, unit tests, red-team safety cases, pilot metric plan | Implemented for prototype; field metrics require approved pilot |

## Honesty boundary

The prototype demonstrates the architecture and decision-support logic. It does not claim clinical efficacy, national-system integration, field validation, or autonomous clinical decision-making.
