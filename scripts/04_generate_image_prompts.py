"""
04_generate_image_prompts.py
----------------------------

Generate illustrative prompts for each text segment. The prompts can be
used with an image generation model or as placeholders.

Inputs
    output_segments/*.txt : Text segments.

Outputs
    output_images/segment_XXX.txt : Text files containing image prompts.
"""

from pathlib import Path

SEGMENT_DIR = Path("output_segments")
OUTPUT_DIR = Path("output_images")

def create_prompt(text: str, max_words: int = 30) -> str:
    """Return a simple prompt based on the beginning of the segment."""
    words = text.strip().split()
    excerpt = " ".join(words[:max_words])
    return f"Illustrate the following scene: {excerpt}..."

def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for seg_file in sorted(SEGMENT_DIR.glob("*.txt")):
        text = seg_file.read_text(encoding="utf-8")
        prompt = create_prompt(text)
        out_path = OUTPUT_DIR / f"{seg_file.stem}.txt"
        out_path.write_text(prompt, encoding="utf-8")
        print(f"Wrote {out_path}")

if __name__ == "__main__":
    main()
