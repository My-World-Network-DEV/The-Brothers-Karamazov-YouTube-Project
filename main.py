"""Entry point for generating audiobook snippets with illustrations."""

from __future__ import annotations

import argparse
import os

from split_blocks import split_into_blocks
from voice_generation import synthesize_speech
from image_generation import generate_images
from utils import ensure_dir, load_text, save_json

OUTPUT_DIR = "outputs"


def main() -> None:
    parser = argparse.ArgumentParser(description="Brothers Karamazov audiobook POC")
    parser.add_argument("excerpt", help="Path to text excerpt file")
    args = parser.parse_args()

    ensure_dir(OUTPUT_DIR)

    text = load_text(args.excerpt)
    blocks = split_into_blocks(text)
    save_json(blocks, os.path.join(OUTPUT_DIR, "blocks.json"))

    synthesize_speech(blocks, OUTPUT_DIR)
    generate_images(blocks, OUTPUT_DIR)

    save_json(blocks, os.path.join(OUTPUT_DIR, "blocks_final.json"))


if __name__ == "__main__":
    main()
