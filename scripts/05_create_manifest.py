"""Create a final manifest linking text segments, audio, and image prompts.

Inputs:
    - output_segments/segment_XXXX.txt
    - output_audio/segment_XXXX.mp3
    - output_images/segment_XXXX.txt
Outputs:
    - JSON file in manifests/final_manifest.json

The manifest can be used by a video assembler to combine assets.
"""
import json
from pathlib import Path

def build_manifest(segments_dir: Path, audio_dir: Path, prompt_dir: Path, manifest_path: Path) -> None:
    manifest = []
    for segment_file in sorted(segments_dir.glob("segment_*.txt")):
        entry = {
            "segment": str(segment_file),
            "audio": str(audio_dir / (segment_file.stem + ".mp3")),
            "image_prompt": str(prompt_dir / (segment_file.stem + ".txt")),
        }
        manifest.append(entry)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

def main() -> None:
    root = Path(__file__).resolve().parent.parent
    segments_dir = root / "output_segments"
    audio_dir = root / "output_audio"
    prompt_dir = root / "output_images"
    manifest_path = root / "manifests" / "final_manifest.json"
    build_manifest(segments_dir, audio_dir, prompt_dir, manifest_path)

if __name__ == "__main__":
    main()
