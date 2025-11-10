thonfrom __future__ import annotations

from dataclasses import dataclass, asdict, field
from typing import Any, Dict, Optional

from extractors.token_utils import (
    derive_lower_pool_address,
    compute_age_hours_from_timestamp,
    safe_get_nested,
    get_token_image_url,
)

@dataclass
class Token:
    tokenName: Optional[str] = None
    tokenSymbol: Optional[str] = None
    priceUsd: Optional[float] = None
    age: Optional[float] = None
    transactionCount: Optional[int] = None
    volumeUsd: Optional[float] = None
    makerCount: Optional[int] = None
    priceChange5m: Optional[float] = None
    priceChange1h: Optional[float] = None
    priceChange6h: Optional[float] = None
    priceChange24h: Optional[float] = None
    liquidityUsd: Optional[float] = None
    marketCapUsd: Optional[float] = None
    boost: Optional[float] = None
    pairDetailUrl: Optional[str] = None
    address: Optional[str] = None
    lowerPoolAddress: Optional[str] = None
    tokenImageUrl: Optional[str] = None

    raw: Dict[str, Any] = field(default_factory=dict, repr=False)

    @classmethod
    def from_pair_payload(cls, pair: Dict[str, Any]) -> "Token":
        """
        Build a Token instance from a single DexScreener pair payload.

        The mapping is intentionally defensive and tolerant of missing keys.
        """
        base_token = pair.get("baseToken") or {}
        chain_id = pair.get("chainId")
        pair_address = pair.get("pairAddress")

        # Price, volume, txns, and price change snapshots
        price_usd = _to_float(pair.get("priceUsd"))
        liquidity_usd = _to_float(safe_get_nested(pair, "liquidity", "usd"))
        market_cap_usd = _to_float(pair.get("fdv"))
        volume_24h = _to_float(safe_get_nested(pair, "volume", "h24"))

        # Transactions count over the last 24h
        tx_buys_24h = _to_int(safe_get_nested(pair, "txns", "h24", "buys", default=0))
        tx_sells_24h = _to_int(safe_get_nested(pair, "txns", "h24", "sells", default=0))
        transaction_count = (tx_buys_24h or 0) + (tx_sells_24h or 0)

        # Price changes
        price_change_5m = _to_float(safe_get_nested(pair, "priceChange", "m5"))
        price_change_1h = _to_float(safe_get_nested(pair, "priceChange", "h1"))
        price_change_6h = _to_float(safe_get_nested(pair, "priceChange", "h6"))
        price_change_24h = _to_float(safe_get_nested(pair, "priceChange", "h24"))

        # Boost metrics (DexScreener exposes e.g. boostScore)
        boost_score = _to_float(pair.get("boostScore") or pair.get("boost"))

        # Age in hours from pairCreatedAt
        created_ms = pair.get("pairCreatedAt")
        age_hours = compute_age_hours_from_timestamp(created_ms) if created_ms else None

        # Pair details URL
        explicit_url = pair.get("url")
        if not explicit_url and chain_id and pair_address:
            explicit_url = f"https://dexscreener.com/{chain_id}/{pair_address}"

        lower_pool_address = derive_lower_pool_address(explicit_url)

        token_image_url = get_token_image_url(pair)

        return cls(
            tokenName=base_token.get("name"),
            tokenSymbol=base_token.get("symbol"),
            priceUsd=price_usd,
            age=age_hours,
            transactionCount=transaction_count or None,
            volumeUsd=volume_24h,
            makerCount=_to_int(safe_get_nested(pair, "makers", "h24") or pair.get("makerCount")),
            priceChange5m=price_change_5m,
            priceChange1h=price_change_1h,
            priceChange6h=price_change_6h,
            priceChange24h=price_change_24h,
            liquidityUsd=liquidity_usd,
            marketCapUsd=market_cap_usd,
            boost=boost_score,
            pairDetailUrl=explicit_url,
            address=base_token.get("address"),
            lowerPoolAddress=lower_pool_address,
            tokenImageUrl=token_image_url,
            raw=pair,
        )

    def to_dict(self) -> Dict[str, Any]:
        """
        Represent the token as a JSON-serializable dict with the fields defined
        in the README. The internal `raw` payload is intentionally omitted.
        """
        data = asdict(self)
        # Remove raw payload
        data.pop("raw", None)
        return data

def _to_float(value: Any) -> Optional[float]:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None

def _to_int(value: Any) -> Optional[int]:
    if value is None:
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None