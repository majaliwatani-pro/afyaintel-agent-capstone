from __future__ import annotations

import re
from datetime import date

from .config import FACILITY_NAME
from .domain import StockItem
from .language import detect_language


def get_low_stock(items: list[StockItem]) -> list[StockItem]:
    return sorted(
        (item for item in items if item.is_low_stock),
        key=lambda item: item.stock_ratio,
    )


def get_expiring_items(
    items: list[StockItem], reference_date: date, days: int = 30
) -> list[tuple[StockItem, int]]:
    result: list[tuple[StockItem, int]] = []
    for item in items:
        remaining = (item.expiry_date - reference_date).days
        if 0 <= remaining <= days:
            result.append((item, remaining))
    return sorted(result, key=lambda pair: pair[1])


def find_item(items: list[StockItem], query: str) -> StockItem | None:
    normalized = query.lower()
    matches = [item for item in items if item.item_name.lower() in normalized]
    if matches:
        return max(matches, key=lambda item: len(item.item_name))
    return None


def format_inventory_summary(items: list[StockItem], language: str) -> str:
    low = get_low_stock(items)
    adequate = len(items) - len(low)
    facility = items[0].facility_name if items else FACILITY_NAME
    if language == "sw":
        lines = [
            f"Muhtasari wa akiba — {facility}",
            f"Jumla ya bidhaa: {len(items)}",
            f"Zenye kiwango cha kutosha: {adequate}",
            f"Zilizo chini ya kiwango cha chini: {len(low)}",
        ]
        if low:
            lines.append("Tahadhari za akiba:")
            lines.extend(
                f"- {item.item_name}: {item.current_stock}/{item.minimum_required} {item.unit}"
                for item in low
            )
        return "\n".join(lines)

    lines = [
        f"Inventory summary — {facility}",
        f"Total items: {len(items)}",
        f"Adequate stock: {adequate}",
        f"Below minimum level: {len(low)}",
    ]
    if low:
        lines.append("Stock alerts:")
        lines.extend(
            f"- {item.item_name}: {item.current_stock}/{item.minimum_required} {item.unit}"
            for item in low
        )
    return "\n".join(lines)


def format_low_stock(items: list[StockItem], language: str) -> str:
    low = get_low_stock(items)
    if not low:
        return (
            "Hakuna bidhaa iliyo chini ya kiwango cha chini."
            if language == "sw"
            else "No item is below its minimum stock level."
        )

    heading = (
        "Bidhaa zilizo chini ya kiwango cha chini:"
        if language == "sw"
        else "Items below minimum stock level:"
    )
    lines = [heading]
    for item in low:
        if language == "sw":
            lines.append(
                f"- {item.item_name}: {item.current_stock}/{item.minimum_required} {item.unit}; pungufu {item.shortage}"
            )
        else:
            lines.append(
                f"- {item.item_name}: {item.current_stock}/{item.minimum_required} {item.unit}; short by {item.shortage}"
            )
    return "\n".join(lines)


def format_expiry_alerts(
    items: list[StockItem], language: str, reference_date: date
) -> str:
    expiring = get_expiring_items(items, reference_date)
    if not expiring:
        return (
            "Hakuna bidhaa inayotarajiwa kuisha muda ndani ya siku 30."
            if language == "sw"
            else "No item expires within the next 30 days."
        )

    heading = (
        "Tahadhari za muda wa matumizi ndani ya siku 30:"
        if language == "sw"
        else "Expiry alerts within 30 days:"
    )
    lines = [heading]
    for item, days_left in expiring:
        if language == "sw":
            lines.append(
                f"- {item.item_name}: {item.expiry_date.isoformat()} ({days_left} siku zimebaki)"
            )
        else:
            lines.append(
                f"- {item.item_name}: {item.expiry_date.isoformat()} ({days_left} days remaining)"
            )
    return "\n".join(lines)


def format_item_status(item: StockItem, language: str) -> str:
    if language == "sw":
        status = "CHINI YA KIWANGO" if item.is_low_stock else "INATOSHA"
        return (
            f"{item.item_name}: {item.current_stock} {item.unit}; kiwango cha chini "
            f"{item.minimum_required}; hali: {status}; muda wa matumizi: "
            f"{item.expiry_date.isoformat()}."
        )
    status = "LOW" if item.is_low_stock else "ADEQUATE"
    return (
        f"{item.item_name}: {item.current_stock} {item.unit}; minimum "
        f"{item.minimum_required}; status: {status}; expiry: {item.expiry_date.isoformat()}."
    )


def build_weekly_report(
    items: list[StockItem], language: str, reference_date: date
) -> str:
    low = get_low_stock(items)
    expiring = get_expiring_items(items, reference_date)
    facility = items[0].facility_name if items else FACILITY_NAME
    generated = reference_date.isoformat()

    if language == "sw":
        lines = [
            f"# Ripoti Fupi ya Uendeshaji — {facility}",
            f"Tarehe ya marejeo: {generated}",
            "",
            "## Muhtasari",
            f"- Jumla ya bidhaa: {len(items)}",
            f"- Chini ya kiwango cha chini: {len(low)}",
            f"- Zinazoisha muda ndani ya siku 30: {len(expiring)}",
            "",
            "## Hatua Zinazopendekezwa",
        ]
        if low:
            lines.extend(
                f"- Msimamizi athibitishe ombi la kuongeza {item.item_name} (pungufu {item.shortage} {item.unit})."
                for item in low
            )
        if expiring:
            lines.extend(
                f"- Mhifadhi akague FEFO kwa {item.item_name}; muda unaisha {item.expiry_date.isoformat()}."
                for item, _ in expiring
            )
        lines.append("- Maamuzi ya ununuzi na ugawaji yahakikiwe na mhusika mwenye mamlaka.")
        return "\n".join(lines)

    lines = [
        f"# Weekly Operations Snapshot — {facility}",
        f"Reference date: {generated}",
        "",
        "## Summary",
        f"- Total inventory items: {len(items)}",
        f"- Below minimum level: {len(low)}",
        f"- Expiring within 30 days: {len(expiring)}",
        "",
        "## Recommended Actions",
    ]
    if low:
        lines.extend(
            f"- Facility manager should verify a replenishment request for {item.item_name} (short by {item.shortage} {item.unit})."
            for item in low
        )
    if expiring:
        lines.extend(
            f"- Storekeeper should apply FEFO review to {item.item_name}; expiry {item.expiry_date.isoformat()}."
            for item, _ in expiring
        )
    lines.append("- Procurement and redistribution decisions require authorized human approval.")
    return "\n".join(lines)


def help_response(language: str) -> str:
    if language == "sw":
        return (
            "AfyaIntel husaidia kufuatilia akiba ya dawa na vifaa, kuona bidhaa zilizo chini ya kiwango, "
            "kutambua muda wa matumizi unaokaribia, na kuandaa ripoti fupi. Haitoi utambuzi wala maagizo ya matibabu.\n"
            "Mifano: 'Dawa zipi ziko chini ya kiwango?', 'Ni bidhaa gani zinaisha muda?', 'Tengeneza ripoti ya wiki'."
        )
    return (
        "AfyaIntel supports inventory monitoring, low-stock detection, expiry alerts, and concise operations reports. "
        "It does not diagnose conditions or prescribe treatment.\n"
        "Examples: 'Which items are low in stock?', 'What expires soon?', 'Generate a weekly report'."
    )


def local_operational_response(
    query: str, items: list[StockItem], reference_date: date
) -> str | None:
    normalized = query.lower().strip()
    language = detect_language(query)

    if not normalized:
        return None
    if re.search(r"\b(hello|hi|hey|habari|hujambo|mambo)\b", normalized):
        return (
            "Habari. Mimi ni AfyaIntel, msaidizi wa shughuli za kituo cha afya. Andika 'msaada' kuona kazi ninazoweza kufanya."
            if language == "sw"
            else "Hello. I am AfyaIntel, a health-facility operations assistant. Type 'help' to see supported tasks."
        )
    if any(term in normalized for term in ["help", "msaada", "main function", "purpose", "unafanya nini", "kazi yako"]):
        return help_response(language)
    if any(term in normalized for term in ["weekly report", "operational report", "stock report", "ripoti", "report"]):
        return build_weekly_report(items, language, reference_date)
    if any(term in normalized for term in ["low stock", "low in stock", "below minimum", "karibia kuisha", "chini ya kiwango", "upungufu", "zimepungua"]):
        return format_low_stock(items, language)
    if any(term in normalized for term in ["expiry", "expire", "expiring", "muda wa matumizi", "inaisha muda", "zinaisha muda"]):
        return format_expiry_alerts(items, language, reference_date)

    item = find_item(items, query)
    if item:
        return format_item_status(item, language)

    if any(term in normalized for term in ["inventory", "stock", "akiba", "dawa zilizobaki", "essential meds"]):
        return format_inventory_summary(items, language)
    return None
