"""Generate image prompts for each segment.

Inputs:
    - Text segments in output_segments/.
Outputs:
    - Prompt text files in output_images/.
    - JSON manifest in manifests/image_prompts.json.

Replace the prompt generation logic with calls to an image model if desired.
"""
import json
from pathlib import Path

def create_prompt(text: str) -> str:
    """Return a simple illustration prompt for the given text."""
    snippet = text.strip().splitlines()[0][:80]
    return f"Illustrate the scene: {snippet}"

def generate_prompts(segments_dir: Path, prompt_dir: Path, manifest_path: Path) -> None:
    prompt_dir.mkdir(parents=True, exist_ok=True)
    manifest = {}
    for segment_file in sorted(segments_dir.glob("segment_*.txt")):
        text = segment_file.read_text(encoding="utf-8")
        prompt = create_prompt(text)
        prompt_file = prompt_dir / (segment_file.stem + ".txt")
        prompt_file.write_text(prompt, encoding="utf-8")
        manifest[segment_file.name] = {"prompt": prompt, "file": str(prompt_file)}
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

def main() -> None:
    root = Path(__file__).resolve().parent.parent
    segments_dir = root / "output_segments"
    prompt_dir = root / "output_images"
    manifest_path = root / "manifests" / "image_prompts.json"
    generate_prompts(segments_dir, prompt_dir, manifest_path)

if __name__ == "__main__":
    main()
