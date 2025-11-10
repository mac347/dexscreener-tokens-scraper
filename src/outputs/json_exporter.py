thonimport json
import logging
from pathlib import Path
from typing import Iterable, List

from models.token_model import Token

logger = logging.getLogger("dexscreener.outputs.json_exporter")

def export_tokens_to_json(tokens: Iterable[Token], output_path: Path) -> None:
    """
    Serialize a collection of Token models to a JSON file using the field names
    described in the project README.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    serializable: List[dict] = [t.to_dict() for t in tokens]

    with output_path.open("w", encoding="utf-8") as f:
        json.dump(serializable, f, indent=2, ensure_ascii=False)

    logger.debug("Wrote JSON file with %d tokens to %s", len(serializable), output_path)