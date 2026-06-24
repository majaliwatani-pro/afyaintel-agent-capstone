from __future__ import annotations

import json
import tempfile
import unittest
from datetime import date
from pathlib import Path

from afyaintel.audit import record_event
from afyaintel.data import DataValidationError, load_stock_data
from afyaintel.orchestrator import process_query
from afyaintel.safety import evaluate_clinical_safety
from afyaintel.tools import get_expiring_items, get_low_stock


class AfyaIntelTests(unittest.TestCase):
    def setUp(self) -> None:
        self.reference_date = date(2026, 6, 15)
        self.items = load_stock_data()

    def test_inventory_has_expected_records(self) -> None:
        self.assertEqual(len(self.items), 10)

    def test_low_stock_is_exact(self) -> None:
        names = [item.item_name for item in get_low_stock(self.items)]
        self.assertEqual(
            set(names),
            {"Malaria RDT", "Artemether Lumefantrine", "Ceftriaxone"},
        )

    def test_expiry_window_is_exact(self) -> None:
        names = [item.item_name for item, _ in get_expiring_items(self.items, self.reference_date)]
        self.assertEqual(set(names), {"Artemether Lumefantrine", "Ceftriaxone"})

    def test_swahili_routing(self) -> None:
        result = process_query(
            "Dawa zipi zimepungua?",
            allow_model=False,
            reference_date=self.reference_date,
            write_audit=False,
        )
        self.assertEqual(result.language, "sw")
        self.assertIn("Bidhaa", result.response)

    def test_clinical_advice_is_blocked(self) -> None:
        result = process_query(
            "Mgonjwa ana homa. Nimpe dawa gani?",
            allow_model=False,
            write_audit=False,
        )
        self.assertTrue(result.blocked)
        self.assertEqual(result.execution_path, "SAFETY_ROUTED")

    def test_emergency_is_escalated(self) -> None:
        decision = evaluate_clinical_safety("The patient has difficulty breathing")
        self.assertTrue(decision.blocked)
        self.assertTrue(decision.emergency)

    def test_unknown_open_question_uses_local_fallback(self) -> None:
        result = process_query(
            "Explain interoperability",
            allow_model=False,
            write_audit=False,
        )
        self.assertEqual(result.execution_path, "LOCAL_FALLBACK")

    def test_bad_csv_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.csv"
            path.write_text("item_name,current_stock\nTest,3\n", encoding="utf-8")
            with self.assertRaises(DataValidationError):
                load_stock_data(path)

    def test_negative_stock_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "negative.csv"
            path.write_text(
                "item_name,category,current_stock,minimum_required,unit,expiry_date,facility_name\n"
                "Test,Demo,-1,2,units,2027-01-01,Demo Facility\n",
                encoding="utf-8",
            )
            with self.assertRaises(DataValidationError):
                load_stock_data(path)

    def test_audit_log_does_not_store_raw_prompt(self) -> None:
        prompt = "Jane Doe private patient text"
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "audit.jsonl"
            record_event(
                query=prompt,
                language="en",
                execution_path="TEST",
                blocked=False,
                emergency=False,
                path=path,
            )
            content = path.read_text(encoding="utf-8")
            event = json.loads(content)
            self.assertNotIn(prompt, content)
            self.assertIn("query_hash", event)

    def test_stockout_forecast_response(self) -> None:
        result = process_query(
            "Show stock-out risk forecast.",
            allow_model=False,
            reference_date=self.reference_date,
            write_audit=False,
        )
        self.assertEqual(result.execution_path, "LOCAL_TOOL")
        self.assertIn("Stock-Out Risk Forecast", result.response)
        self.assertIn("HIGH", result.response)

    def test_fhir_export_response(self) -> None:
        result = process_query(
            "Export FHIR inventory bundle.",
            allow_model=False,
            reference_date=self.reference_date,
            write_audit=False,
        )
        self.assertEqual(result.execution_path, "LOCAL_TOOL")
        self.assertIn("FHIR-compatible", result.response)

    def test_dashboard_payload_response(self) -> None:
        result = process_query(
            "Build A2UI dashboard payload.",
            allow_model=False,
            reference_date=self.reference_date,
            write_audit=False,
        )
        self.assertEqual(result.execution_path, "LOCAL_TOOL")
        self.assertIn("dashboard payload", result.response.lower())

    def test_human_approval_matrix_response(self) -> None:
        result = process_query(
            "What human approval is required?",
            allow_model=False,
            reference_date=self.reference_date,
            write_audit=False,
        )
        self.assertEqual(result.execution_path, "LOCAL_TOOL")
        self.assertIn("Human Approval Matrix", result.response)


if __name__ == "__main__":
    unittest.main()
