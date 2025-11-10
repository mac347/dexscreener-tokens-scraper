thonimport csv
import logging
from pathlib import Path
from typing import Iterable, List

from models.token_model import Token

logger = logging.getLogger("dexscreener.outputs.csv_exporter")

def export_tokens_to_csv(tokens: Iterable[Token], output_path: Path) -> None:
    """
    Serialize a collection of Token models to a CSV file.

    Column names match the JSON field names defined in Token.to_dict().
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    tokens_list: List[Token] = list(tokens)

    if not tokens_list:
        logger.warning("No tokens provided for CSV export. Skipping file creation.")
        return

    fieldnames = list(tokens_list[0].to_dict().keys())

    with output_path.open("w", encoding="utf-8", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for token in tokens_list:
            writer.writerow(token.to_dict())

    logger.debug("Wrote CSV file with %d tokens to %s", len(tokens_list), output_path)