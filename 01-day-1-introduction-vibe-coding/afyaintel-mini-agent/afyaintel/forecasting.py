from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta

from .domain import StockItem


@dataclass(frozen=True)
class ForecastRisk:
    item_name: str
    current_stock: int
    daily_issue_average: float
    days_remaining: float
    estimated_stockout_date: str
    risk_level: str
    rationale: str


def risk_level_for(item: StockItem) -> str:
    days = item.estimated_days_remaining
    if item.is_low_stock or days <= 14:
        return "HIGH"
    if days <= 30 or item.stock_ratio < 1.25:
        return "MEDIUM"
    return "LOW"


def build_forecast(items: list[StockItem], reference_date: date) -> list[ForecastRisk]:
    risks: list[ForecastRisk] = []
    for item in items:
        days = item.estimated_days_remaining
        if days == float("inf"):
            stockout_date = "unknown"
        else:
            stockout_date = (reference_date + timedelta(days=int(days))).isoformat()
        level = risk_level_for(item)
        if level == "HIGH":
            rationale = "below minimum level or projected to deplete within 14 days"
        elif level == "MEDIUM":
            rationale = "requires monitoring; stock buffer is limited"
        else:
            rationale = "currently stable under demo assumptions"
        risks.append(
            ForecastRisk(
                item_name=item.item_name,
                current_stock=item.current_stock,
                daily_issue_average=item.daily_issue_average,
                days_remaining=days,
                estimated_stockout_date=stockout_date,
                risk_level=level,
                rationale=rationale,
            )
        )
    return sorted(risks, key=lambda risk: {"HIGH": 0, "MEDIUM": 1, "LOW": 2}[risk.risk_level])


def format_forecast(items: list[StockItem], reference_date: date, language: str) -> str:
    risks = build_forecast(items, reference_date)
    if language == "sw":
        lines = [
            "# Utabiri wa Hatari ya Kuisha kwa Akiba",
            "Njia: hesabu ya wazi ya demo kwa kutumia wastani wa matumizi ya kila siku; si Prophet/XGBoost halisi.",
        ]
        for risk in risks[:6]:
            days_text = "haijulikani" if risk.days_remaining == float("inf") else f"takriban {risk.days_remaining:.1f} siku"
            lines.append(
                f"- {risk.item_name}: {risk.risk_level}; imebaki {days_text}; makadirio ya kuisha {risk.estimated_stockout_date}."
            )
        lines.append("Maamuzi ya ununuzi au ugawaji yanahitaji uthibitisho wa binadamu mwenye mamlaka.")
        return "\n".join(lines)
    lines = [
        "# Stock-Out Risk Forecast",
        "Method: transparent demo calculation using daily issue averages; not a validated Prophet/XGBoost model.",
    ]
    for risk in risks[:6]:
        days_text = "unknown" if risk.days_remaining == float("inf") else f"about {risk.days_remaining:.1f} days"
        lines.append(
            f"- {risk.item_name}: {risk.risk_level}; remaining {days_text}; estimated stock-out {risk.estimated_stockout_date}."
        )
    lines.append("Procurement or redistribution decisions require authorized human approval.")
    return "\n".join(lines)
