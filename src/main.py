thonimport argparse
import json
import logging
import sys
from pathlib import Path
from typing import List, Dict, Any

# Ensure project root and src are on sys.path so we can import models and extractors
CURRENT_FILE = Path(__file__).resolve()
SRC_DIR = CURRENT_FILE.parent
ROOT_DIR = SRC_DIR.parent

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from extractors.dexscreener_parser import DexScreenerClient  # noqa: E402
from models.token_model import Token  # noqa: E402
from outputs.json_exporter import export_tokens_to_json  # noqa: E402
from outputs.csv_exporter import export_tokens_to_csv  # noqa: E402

logger = logging.getLogger("dexscreener.main")

def load_settings(settings_path: Path) -> Dict[str, Any]:
    if not settings_path.exists():
        logger.warning("Settings file %s not found, using hardcoded defaults.", settings_path)
        return {
            "dexscreener": {
                "baseUrl": "https://api.dexscreener.com/latest/dex",
                "timeoutSeconds": 10,
            },
            "pagination": {
                "maxPages": 1,
                "pageSize": 50,
            },
            "output": {
                "directory": "data",
                "jsonFilename": "tokens.json",
                "csvFilename": "tokens.csv",
            },
        }

    with settings_path.open("r", encoding="utf-8") as f:
        return json.load(f)

def load_input_targets(input_path: Path) -> List[Dict[str, Any]]:
    if not input_path.exists():
        logger.error("Input targets file %s does not exist.", input_path)
        raise FileNotFoundError(f"Input targets file not found: {input_path}")

    with input_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, dict):
        # Allow a single object
        return [data]
    if not isinstance(data, list):
        raise ValueError("Input file must contain a list of targets or a single target object.")
    return data

def resolve_output_paths(root_dir: Path, settings: Dict[str, Any], override_output_dir: str | None):
    output_cfg = settings.get("output", {})
    directory = override_output_dir or output_cfg.get("directory", "data")
    json_filename = output_cfg.get("jsonFilename", "tokens.json")
    csv_filename = output_cfg.get("csvFilename", "tokens.csv")

    out_dir = (root_dir / directory).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    return out_dir / json_filename, out_dir / csv_filename

def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="DexScreener Tokens Scraper - collect live token data from DexScreener."
    )
    parser.add_argument(
        "--input",
        type=str,
        default=str(ROOT_DIR / "data" / "inputs.sample.json"),
        help="Path to JSON file describing scrape targets.",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default=None,
        help="Directory where JSON/CSV results will be written. Overrides settings file.",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=None,
        help="Optional override for maximum pages to fetch per target.",
    )
    parser.add_argument(
        "--log-level",
        type=str,
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Log verbosity.",
    )
    return parser

def configure_logging(level: str) -> None:
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    )

def run_scraper(args: argparse.Namespace) -> int:
    configure_logging(args.log_level)
    logger.info("Starting DexScreener Tokens Scraper.")

    settings_path = SRC_DIR / "config" / "settings.example.json"
    settings = load_settings(settings_path)

    base_url = settings.get("dexscreener", {}).get(
        "baseUrl", "https://api.dexscreener.com/latest/dex"
    )
    timeout = settings.get("dexscreener", {}).get("timeoutSeconds", 10)
    default_max_pages = settings.get("pagination", {}).get("maxPages", 1)
    page_size = settings.get("pagination", {}).get("pageSize", 50)

    input_path = Path(args.input).resolve()
    try:
        targets = load_input_targets(input_path)
    except Exception as exc:
        logger.exception("Failed to load input targets: %s", exc)
        return 1

    json_path, csv_path = resolve_output_paths(ROOT_DIR, settings, args.output_dir)

    client = DexScreenerClient(base_url=base_url, timeout=timeout)

    all_tokens: List[Token] = []

    for idx, target in enumerate(targets, start=1):
        query = target.get("query")
        if not query:
            logger.warning("Target #%d has no 'query' field, skipping: %s", idx, target)
            continue

        max_pages = args.max_pages or target.get("maxPages", default_max_pages)
        logger.info("Fetching tokens for query '%s' (max_pages=%s)...", query, max_pages)

        try:
            tokens_for_query = client.fetch_tokens_for_query(
                query=query,
                max_pages=max_pages,
                page_size=page_size,
            )
        except Exception as exc:
            logger.exception("Failed to fetch tokens for query '%s': %s", query, exc)
            continue

        logger.info("Retrieved %d tokens for query '%s'.", len(tokens_for_query), query)
        all_tokens.extend(tokens_for_query)

    if not all_tokens:
        logger.warning("No tokens were collected; nothing to export.")
        return 0

    try:
        export_tokens_to_json(all_tokens, json_path)
        logger.info("Exported %d tokens to JSON: %s", len(all_tokens), json_path)
    except Exception as exc:
        logger.exception("Failed to export JSON: %s", exc)
        return 1

    try:
        export_tokens_to_csv(all_tokens, csv_path)
        logger.info("Exported %d tokens to CSV: %s", len(all_tokens), csv_path)
    except Exception as exc:
        logger.exception("Failed to export CSV: %s", exc)
        return 1

    logger.info("Scraper completed successfully.")
    return 0

def main() -> None:
    parser = build_arg_parser()
    args = parser.parse_args()
    exit_code = run_scraper(args)
    sys.exit(exit_code)

if __name__ == "__main__":
    main()