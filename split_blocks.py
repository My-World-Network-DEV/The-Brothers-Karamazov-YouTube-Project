"""Split an excerpt into blocks with speaker labels and image prompts."""

from __future__ import annotations

import re
from typing import Dict, List


SPEAKER_REGEX = re.compile(
    r'"[^"\n]+"\s*(?:,\s*)?(?:said|asked|cried)\s+([A-Z][a-z]+)',
    re.IGNORECASE,
)


def _detect_speaker(block: str) -> str:
    """Return a speaker name for a block of text."""
    match = SPEAKER_REGEX.search(block)
    if match:
        return match.group(1)
    return "Narrator"


def _image_prompt(speaker: str, text: str) -> str:
    """Create a lightweight image prompt for *text* spoken by *speaker*."""
    summary = text.strip().replace("\n", " ")
    summary = re.sub(r"\s+", " ", summary)[:120]
    if speaker == "Narrator":
        return f"Scene: {summary}"
    return f"{speaker} speaks: {summary}"


def split_into_blocks(excerpt: str) -> List[Dict[str, str]]:
    """Split *excerpt* by double newlines and annotate blocks.

    Returns a list of dictionaries each containing:
        speaker, text, and image_prompt
    """
    raw_blocks = [b.strip() for b in excerpt.split("\n\n") if b.strip()]
    blocks: List[Dict[str, str]] = []
    for block in raw_blocks:
        speaker = _detect_speaker(block)
        prompt = _image_prompt(speaker, block)
        blocks.append({"speaker": speaker, "text": block, "image_prompt": prompt})
    return blocks
