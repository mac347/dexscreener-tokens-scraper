thonfrom __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, Optional

@dataclass
class Launchpad:
    """
    Represents launchpad-specific metrics for early-stage tokens.

    This model is designed to accept generic launchpad payloads, even if they
    come from different platforms (e.g., Moonit, Pump.Fun, etc.).
    """

    platform: Optional[str] = None
    status: Optional[str] = None
    softCapUsd: Optional[float] = None
    hardCapUsd: Optional[float] = None
    raisedUsd: Optional[float] = None
    progressPercent: Optional[float] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    raw: Dict[str, Any] | None = None

    @classmethod
    def from_payload(cls, payload: Dict[str, Any], platform: Optional[str] = None) -> "Launchpad":
        def to_float(value: Any) -> Optional[float]:
            if value is None:
                return None
            try:
                return float(value)
            except (TypeError, ValueError):
                return None

        def parse_ts(ts: Any) -> Optional[datetime]:
            if ts is None:
                return None
            # Accept seconds or milliseconds
            try:
                ts = float(ts)
            except (TypeError, ValueError):
                return None
            if ts > 10_000_000_000:  # heuristically treat as ms