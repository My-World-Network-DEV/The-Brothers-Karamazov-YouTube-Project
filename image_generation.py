"""Generate an illustration per block using the OpenAI API."""

from __future__ import annotations

import base64
import os
from typing import Dict, List

from openai import OpenAI

import config
from utils import ensure_dir, slugify


def generate_images(blocks: List[Dict[str, str]], output_dir: str) -> None:
    """Add an ``image_path`` to each block, saving images to *output_dir*."""
    ensure_dir(output_dir)
    client = OpenAI(api_key=config.OPENAI_API_KEY)
    for idx, block in enumerate(blocks, 1):
        try:
            result = client.images.generate(prompt=block["image_prompt"], model="gpt-image-1")
            image_b64 = result.data[0].b64_json
            image_bytes = base64.b64decode(image_b64)
        except Exception:
            block["image_path"] = None
            continue

        filename = f"{idx:03d}_{slugify(block['speaker'])}.png"
        path = os.path.join(output_dir, filename)
        with open(path, "wb") as f:
            f.write(image_bytes)
        block["image_path"] = path
