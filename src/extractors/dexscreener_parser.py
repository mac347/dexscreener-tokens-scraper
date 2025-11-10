thonimport logging
from typing import Any, Dict, List, Optional

import requests

from models.token_model import Token

logger = logging.getLogger("dexscreener.extractors.dexscreener_parser")

class DexScreenerError(RuntimeError):
    """Generic error raised when interacting with the DexScreener API."""

class DexScreenerClient:
    """
    Lightweight client for the DexScreener public API.

    This client focuses on the `/latest/dex/search` endpoint, which allows
    queries in the form of `chain/dex` (e.g. `solana/moonshot`) or general
    token / pair queries.
    """

    def __init__(
        self,
        base_url: str = "https://api.dexscreener.com/latest/dex",
        timeout: int = 10,
        session: Optional[requests.Session] = None,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = session or requests.Session()

    def _request(self, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}/{path.lstrip('/')}"
        logger.debug("Requesting %s with params=%s", url, params)

        try:
            response = self.session.get(url, params=params, timeout=self.timeout)
        except requests.RequestException as exc:
            logger.error("HTTP error while contacting DexScreener: %s", exc)
            raise DexScreenerError("Network error while contacting DexScreener") from exc

        if not response.ok:
            logger.error(
                "DexScreener returned non-OK status: %s %s",
                response.status_code,
                response.text,
            )
            raise DexScreenerError(
                f"DexScreener error: HTTP {response.status_code} - {response.text}"
            )

        try:
            data = response.json()
        except ValueError as exc:
            logger.error("Failed to parse JSON from DexScreener: %s", exc)
            raise DexScreenerError("Invalid JSON from DexScreener") from exc

        return data

    def search_pairs(self, query: str) -> List[Dict[str, Any]]:
        """
        Search for pairs using DexScreener's search endpoint.

        DexScreener returns a structure like:
        {
            "schemaVersion": "1.0",
            "pairs": [...]
        }
        """
        data = self._request("search", params={"q": query})
        pairs = data.get("pairs") or []
        logger.debug("DexScreener search returned %d pairs for query '%s'.", len(pairs), query)
        return pairs

    def fetch_tokens_for_query(
        self,
        query: str,
        max_pages: int = 1,
        page_size: int = 50,
    ) -> List[Token]:
        """
        Fetch Token models for a given query.

        DexScreener search is not strictly paginated in the usual sense, but this
        function exposes `max_pages` and `page_size` to fit the project's
        abstraction. For now it simply truncates to `max_pages * page_size`.
        """
        if max_pages < 1:
            max_pages = 1

        pairs = self.search_pairs(query)
        max_items = max_pages * page_size
        if max_items and len(pairs) > max_items:
            logger.debug(
                "Truncating pairs from %d to %d (max_pages=%d, page_size=%d).",
                len(pairs),
                max_items,
                max_pages,
                page_size,
            )
            pairs = pairs[:max_items]

        tokens: List[Token] = []
        for pair in pairs:
            try:
                token = Token.from_pair_payload(pair)
                tokens.append(token)
            except Exception as exc:
                logger.debug("Failed to parse pair into Token, skipping. Error: %s", exc, exc_info=True)

        logger.info(
            "Converted %d pairs into Token models for query '%s'.", len(tokens), query
        )
        return tokens