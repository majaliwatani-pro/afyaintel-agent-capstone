# Day 1 Notes: Introduction to Agents & Vibe Coding

## Course

Kaggle 5-Day AI Agents: Intensive Vibe Coding Course With Google

## Date

June 15, 2026

## Day 1 Topic

Introduction to Agents & Vibe Coding

---

## 1. What I Learned Today

1. I learned how AI development is moving from simple single-turn chatbot interfaces to more autonomous agents that can use tools such as file editing, terminal commands, APIs, and web-based workflows to solve complex goals.

2. I learned the concept of **Vibe Coding**, where natural language becomes the primary programming interface. Instead of manually writing every line of code, the developer describes the goal, constraints, expected behavior, and system structure while the AI agent assists with implementation.

3. I learned that the Software Development Life Cycle is changing from a traditional manual coding process into an iterative **prompt-review-evaluate** workflow. In this new approach, humans guide the agent, review outputs, test functionality, and ensure safety before deployment.

4. I learned that human review is still critical. AI agents can hallucinate, misunderstand requirements, introduce bugs, create security issues, or produce code that appears correct but fails in real use.

5. I learned the basics of evaluating AI agents by testing task success, correctness, safety boundaries, usability, latency, and behavior in low-resource environments.

---

## 2. Important Concepts

### AI Agent

An AI agent is an autonomous software entity that can understand a goal, reason about the next steps, use tools, perform actions, check results, and continue working under human guidance.

Unlike a basic chatbot, an agent can work across multiple steps. It can use external tools such as APIs, command-line programs, databases, file systems, and deployment platforms to complete tasks.

In simple terms:

> A chatbot mainly responds.
> An agent can plan, act, verify, and improve.

---

### Vibe Coding

Vibe Coding is a modern software development approach where the developer uses natural language to describe what should be built, and the AI agent helps generate, edit, test, and debug the code.

The developer does not stop being important. Instead, the developer becomes more like:

* System architect
* Requirements designer
* Prompt engineer
* Code reviewer
* Security reviewer
* Evaluation designer
* Deployment supervisor

The AI agent handles much of the implementation work, while the human remains responsible for correctness, safety, and final approval.

---

### New SDLC With AI Agents

Traditional SDLC usually follows this flow:

1. Requirements
2. Design
3. Coding
4. Testing
5. Deployment
6. Maintenance

The agentic SDLC changes this into a more interactive workflow:

1. Define intent
2. Provide context
3. Set constraints
4. Let the agent generate or modify the solution
5. Review the agent’s output
6. Test and evaluate the result
7. Fix errors through iteration
8. Deploy carefully
9. Monitor and improve continuously

This means software development becomes faster, but it also requires stronger evaluation and review discipline.

---

### Human Review

Human review is necessary because AI agents are powerful but not perfect.

An agent may:

* Misunderstand user instructions
* Generate insecure code
* Introduce hidden bugs
* Use outdated assumptions
* Expose secrets if not guided properly
* Produce outputs that look correct but are logically wrong

Therefore, every serious agent workflow must include human review, testing, logging, and approval before production deployment.

---

### Evaluation

Evaluation means checking whether the agent works correctly, safely, and reliably.

Agent evaluation can include:

* Unit tests
* Integration tests
* Manual review
* Human feedback
* LLM-as-a-judge
* Safety tests
* Prompt injection tests
* Tool-use tests
* Latency and cost checks
* Task success rate

For my AfyaIntel Agent, evaluation must include both English and Swahili outputs, safety behavior, medical-risk routing, and correctness of reports.

---

## 3. Tools Used Today

### Antigravity

Antigravity is Google’s agentic pair-programming environment. It helps developers work with AI agents that can inspect files, modify code, run terminal commands, and assist with project development.

### Antigravity IDE

The Antigravity IDE is the workspace where I open my project folder, review files, inspect agent changes, and manage the development process.

### Google AI Studio

Google AI Studio is used to test Gemini models, prototype prompts, create applications using Build Mode, and experiment with AI-powered application workflows.

### Google Cloud Run

Cloud Run is Google Cloud’s serverless platform for deploying containerized web applications to HTTPS endpoints without managing servers directly.

### Python, pip, and uv

Python is used for local development and agent testing.
pip is used for Python package management.
uv is used for faster Python project and dependency management.

---

## 4. What I Built Today
1. Verified local Python, pip, and uv installations by executing a verification script `python-check/main.py`.
2. Built the **AfyaIntel Mini-Agent Prototype** (in `afyaintel-mini-agent/`), a tool-augmented operational assistant that reads `sample_stock.csv`, intercepts clinical queries, supports Swahili/English responses, and executes an automated local evaluation suite covering 14 deterministic and engineering checks.

I completed the following:

* Created the main course workspace:
  `C:\Users\cohema\agy2-projects\kaggle-5day-ai-agents-2026`

* Installed and verified Python 3.12.10.

* Verified pip installation.

* Installed and verified uv.

* Created a Python verification folder:
  `01-day-1-introduction-vibe-coding/python-check`

* Created and executed a simple `main.py` script to confirm that the local Python environment is working.

* Configured Google Cloud CLI.

* Created a dedicated Google Cloud project:
  `kaggle-ai-agents-2026`

* Configured Application Default Credentials safely.

* Opened and prepared the workspace for Antigravity and AI Studio work.

---

## 5. Evidence Available in This Archive

- `screenshots/04-gemini-api-test-output.png` — local Gemini API test
- `screenshots/05-day1-livestream-course-overview.png` through `23-day1-quiz-q5-answer.png` — livestream and quiz evidence
- `afyaintel-mini-agent/eval_report.md` and `eval_report.json` — deterministic evaluation evidence
- `whitepaper-notes.md` — whitepaper reflection
- `day-1-livestream-notes.md` — livestream reflection

The Antigravity, AI Studio, Cloud Run, and AfyaIntel terminal screenshots should be recaptured and added before final submission because they are not present in this archive.

---

## 6. Errors Encountered and Fixed

### Error 1: Python Was Not Found

Problem:
PowerShell returned:

`Python was not found`

Cause:
Python was not installed or was not available in PATH.

Fix:
Installed Python 3.12.10 using winget and confirmed that Python and pip were working.

Status:
Fixed.

---

### Error 2: pip Was Not Recognized

Problem:
PowerShell returned:

`pip is not recognized as the name of a cmdlet`

Cause:
pip was not available because Python was not properly installed or detected.

Fix:
After installing Python 3.12.10, pip became available and was upgraded successfully.

Status:
Fixed.

---

### Error 3: uv Was Not Found

Problem:
PowerShell returned:

`uv is not recognized`

Cause:
uv was not installed yet.

Fix:
Installed uv using pip:

`py -3.12 -m pip install uv`

Status:
Fixed.

---

### Error 4: Wrong Script Path

Problem:
The command failed with:

`The system cannot find the path specified`

Cause:
I was already inside the `python-check` folder but still tried to run the script using a longer relative path.

Fix:
Ran the correct command:

`uv run main.py`

Status:
Fixed.

---

### Error 5: Google Cloud API Billing Issue

Problem:
Some Google Cloud APIs could not be enabled because billing was not linked to the new project.

Cause:
The project `kaggle-ai-agents-2026` was created successfully, but no billing account was linked at first.

Fix:
For now, continue local development and AI Studio work. Billing can be linked later if advanced Cloud Run deployment is required.

Status:
Pending billing decision.

---

## 7. Questions I Still Have

1. What are the best practices for structuring tools so an agent does not get confused when selecting which tool to run?

2. How can I build a robust evaluation pipeline for a bilingual English/Swahili agent?

3. How can I optimize prompts to reduce token usage and latency for low-resource network environments?

4. How should I design guardrails for health-related AI agents so that risky clinical questions are routed to human professionals?

5. What is the best way to document tool calls, reasoning traces, and evaluation results in a capstone project?

---

## 8. Capstone Connection

Day 1 helped me understand how to structure my capstone idea as a real AI agent instead of a simple chatbot.

My planned capstone direction is:

**AfyaIntel Agent: Swahili Health Facility Support Agent**

The agent will support low-resource health facilities by helping with:

* Stock summary
* Report generation
* Swahili and English explanations
* Operational decision support
* Human-review routing
* Safety-aware responses

The agent will not act as a doctor. It will support reporting, supply chain decisions, and operational workflows while routing risky medical questions to qualified human professionals.

---

## 9. Day 1 Reflection

Day 1 showed me that building serious AI agents requires more than writing prompts. It requires clear goals, strong context, safe tool use, evaluation, human review, and careful deployment.

My main takeaway is:

> A strong AI agent is not judged only by whether it can respond, but by whether it can complete useful tasks safely, correctly, and reliably.
