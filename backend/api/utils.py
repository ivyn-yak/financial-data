import json
from pathlib import Path
import logging
from pydantic import BaseModel
from typing import Dict
from datetime import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def save_to_json(data, filename, output_dir='samples'):
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    filename = Path(output_dir) / filename

    with Path.open(filename, 'w') as f:
        json.dump(data, f, indent=4)

    logger.info(f"Data saved to {filename}")


def build_news_filename(tickers=None, topics=None, time_from=None, time_to=None, sort=None, limit=None):
    parts = ["news"]

    if tickers:
        parts.append("_".join(tickers))  # e.g. ["AAPL","GOOG"] -> "AAPL_GOOG"
    if topics:
        parts.append("_".join(topics))   # e.g. ["AI"] -> "AI"
    if time_from:
        parts.append(time_from)
    if time_to:
        parts.append(time_to)
    if sort:
        parts.append(sort)
    if limit:
        parts.append(str(limit))

    return "_".join(parts) + ".json"


def filter_json_for_model(data: Dict, model: BaseModel) -> Dict:
    """
    Filters JSON keys that exist in the Pydantic model,
    and coerces string values to the right types.
    """
    field_types = model.__annotations__  # dict of {field: type}
    filtered = {}

    for field, field_type in field_types.items():
        if field not in data:
            continue
        val = data[field]

        # Try to coerce types
        if val in (None, "", "None"):
            filtered[field] = None
        elif field_type == int:
            filtered[field] = int(val)
        elif field_type == float:
            filtered[field] = float(val)
        elif field_type == datetime:
            filtered[field] = datetime.strptime(val, "%Y%m%dT%H%M%S")
        else:
            filtered[field] = val  # leave as-is (str, nested, etc.)

    return filtered

