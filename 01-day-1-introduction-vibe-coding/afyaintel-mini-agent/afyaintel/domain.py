from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class StockItem:
    item_name: str
    category: str
    current_stock: int
    minimum_required: int
    unit: str
    expiry_date: date
    facility_name: str
    item_code: str = ""
    batch_id: str = ""
    daily_issue_average: float = 0.0
    readiness_level: str = "Level 2: Hybrid"
    sync_status: str = "queued"

    @property
    def is_low_stock(self) -> bool:
        return self.current_stock < self.minimum_required

    @property
    def shortage(self) -> int:
        return max(0, self.minimum_required - self.current_stock)

    @property
    def stock_ratio(self) -> float:
        if self.minimum_required == 0:
            return 1.0
        return self.current_stock / self.minimum_required

    @property
    def estimated_days_remaining(self) -> float:
        if self.daily_issue_average <= 0:
            return float("inf")
        return self.current_stock / self.daily_issue_average


@dataclass(frozen=True)
class SafetyDecision:
    blocked: bool
    emergency: bool
    reason: str


@dataclass(frozen=True)
class QueryResult:
    response: str
    execution_path: str
    language: str
    blocked: bool = False
    emergency: bool = False
