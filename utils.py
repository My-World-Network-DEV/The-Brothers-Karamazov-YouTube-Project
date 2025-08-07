"""Utility functions for file I/O and helpers."""

from __future__ import annotations

import json
import os
import re
from typing import Any


def ensure_dir(path: str) -> None:
    """Ensure that a directory exists."""
    os.makedirs(path, exist_ok=True)


def load_text(path: str) -> str:
    """Read and return text from *path*."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def save_json(data: Any, path: str) -> None:
    """Serialize *data* as JSON to *path* with UTF-8 encoding."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def slugify(value: str) -> str:
    """Create a filesystem-friendly slug from *value*."""
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")
