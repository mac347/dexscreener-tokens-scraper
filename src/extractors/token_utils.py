thonfrom __future__ import annotations

import logging
from datetime import datetime, timezone
from typing import Any, Dict, Optional
from urllib.parse import urlparse

logger = logging.getLogger("dexscreener.extractors.token_utils")

def derive_lower_pool_address(pair_detail_url: Optional[str]) -> Optional[str]:
    """
    Extract the pool address from a DexScreener pair URL and normalize to lowercase.

    Example:
        https://dexscreener.com/solana/29jupdw7... -> "29jupdw7..."
    """
    if not pair_detail_url:
        return None

    try:
        parsed = urlparse(pair_detail_url)
        segments = [seg for seg in parsed.path.split("/") if seg]
        if not segments:
            return None
        return segments[-1].lower()
    except Exception as exc:
        logger.debug("Failed to derive lower pool address from URL '%s': %s", pair_detail_url, exc)
        return None

def compute_age_hours_from_timestamp(created_ms: Optional[int]) -> Optional[float]:
    """
    Convert a millisecond timestamp (UTC) into age in hours as a float.

    DexScreener provides `pairCreatedAt` timestamps in milliseconds.
    """
    if not created_ms:
        return None
    try:
        created_dt = datetime.fromtimestamp(created_ms / 1000.0, tz=timezone.utc)
        now = datetime.now(tz=timezone.utc)
        delta = now - created_dt
        return round(delta.total_seconds() / 3600.0, 2)
    except Exception as exc:
        logger.debug(
            "Failed to compute age hours from timestamp '%s': %s", created_ms, exc
        )
        return None

def safe_get_nested(data: Dict[str, Any], *keys: str, default: Any = None) -> Any:
    """
    Safely traverse nested dictionaries.

    Example:
        safe_get_nested(d, "txns", "h24", "buys", default=0)
    """
    current: Any = data
    for key in keys:
        if not isinstance(current, dict):
            return default
        if key not in current:
            return default
        current = current[key]
    return current

def get_token_image_url(pair_payload: Dict[str, Any]) -> Optional[str]:
    """
    DexScreener may embed token or pair image URLs in different locations.
    Try common locations here and fall back gracefully.
    """
    # Common place for logos
    image_url = safe_get_nested(pair_payload, "info", "imageUrl")
    if image_url:
        return image_url

    # Fallback on baseToken if present
    image_url = safe_get_nested(pair_payload, "baseToken", "imageUrl")
    if image_url:
        return image_url

    return None