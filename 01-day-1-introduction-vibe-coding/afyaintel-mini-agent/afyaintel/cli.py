from __future__ import annotations

import argparse
import sys

from . import __version__
from .evaluation import run_live_evaluations, run_local_evaluations
from .orchestrator import process_query


def run_demo() -> None:
    prompts = [
        "Hello",
        "Which items are currently low in stock?",
        "Show stock-out risk forecast.",
        "Export a FHIR inventory bundle.",
        "Build an A2UI dashboard payload.",
        "Tengeneza ripoti ya wiki kwa Kiswahili.",
        "Mgonjwa ana homa kali. Nimpe dawa gani?",
    ]
    print("AFYAINTEL DEMO — LOCAL-FIRST, SAFETY-GOVERNED")
    for prompt in prompts:
        result = process_query(prompt, allow_model=False)
        print(
            f"\nUSER: {prompt}\nPATH: {result.execution_path}\n{result.response}"
        )


def interactive_mode() -> None:
    print("=" * 72)
    print("AfyaIntel: Bilingual Health-Facility Operations Agent")
    print("Local-first stock, expiry, reporting, and safety routing")
    print("Type 'exit' or 'quit' to end the session.")
    print("=" * 72)
    while True:
        try:
            query = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nSession ended.")
            return
        if query.lower() in {"exit", "quit"}:
            print("Session ended. Kwa heri!")
            return
        if not query:
            continue
        result = process_query(query, allow_model=True)
        print(f"\nAfyaIntel [{result.execution_path}]:\n{result.response}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="AfyaIntel local-first bilingual health-facility operations agent"
    )
    parser.add_argument("--interactive", action="store_true", help="Start the interactive CLI")
    parser.add_argument("--evaluate", action="store_true", help="Alias for --evaluate-local")
    parser.add_argument("--evaluate-local", action="store_true", help="Run zero-API local evaluations")
    parser.add_argument("--evaluate-live", action="store_true", help="Run at most two Gemini-backed checks")
    parser.add_argument("--demo", action="store_true", help="Run a scripted local demonstration")
    parser.add_argument("--version", action="store_true", help="Print the project version")
    args = parser.parse_args()

    if args.version:
        print(f"AfyaIntel {__version__}")
        return 0
    if args.interactive:
        interactive_mode()
        return 0
    if args.evaluate_live:
        return run_live_evaluations()
    if args.demo:
        run_demo()
        return 0
    return run_local_evaluations()


if __name__ == "__main__":
    sys.exit(main())
