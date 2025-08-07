"""Generate speech audio for each block using the ElevenLabs API."""

from __future__ import annotations

import os
from typing import Dict, List

import requests

import config
from utils import ensure_dir, slugify

ELEVEN_URL = "https://api.elevenlabs.io/v1/text-to-speech/"


def synthesize_speech(blocks: List[Dict[str, str]], output_dir: str) -> None:
    """Add an ``audio_path`` entry to each block in *blocks*.

    Parameters
    ----------
    blocks:
        List of block dictionaries produced by :func:`split_blocks`.
    output_dir:
        Directory where generated audio files will be written.
    """
    ensure_dir(output_dir)
    for idx, block in enumerate(blocks, 1):
        voice_id = config.ELEVENLABS_VOICE_IDS.get(
            block["speaker"], config.ELEVENLABS_VOICE_IDS.get("Narrator", "")
        )
        if not voice_id:
            block["audio_path"] = None
            continue

        payload = {"text": block["text"]}
        headers = {
            "xi-api-key": config.ELEVENLABS_API_KEY,
            "Content-Type": "application/json",
        }

        try:
            resp = requests.post(f"{ELEVEN_URL}{voice_id}", json=payload, headers=headers, timeout=30)
            resp.raise_for_status()
        except Exception:
            block["audio_path"] = None
            continue

        filename = f"{idx:03d}_{slugify(block['speaker'])}.mp3"
        path = os.path.join(output_dir, filename)
        with open(path, "wb") as f:
            f.write(resp.content)
        block["audio_path"] = path
