"""
05_create_manifest.py
---------------------

Combine the outputs of previous stages into a final manifest suitable for
video assembly.

Inputs
    output_segments/*.txt
    output_audio/*.mp3
    output_images/*.txt

Outputs
    manifests/final_manifest.json : List mapping text, audio and image prompt
    for each segment.
"""

from pathlib import Path
import json

SEGMENT_DIR = Path("output_segments")
AUDIO_DIR = Path("output_audio")
IMAGE_DIR = Path("output_images")
OUTPUT_DIR = Path("manifests")

def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest = []
    for seg_file in sorted(SEGMENT_DIR.glob("*.txt")):
        stem = seg_file.stem
        entry = {
            "text": str(seg_file),
            "audio": str(AUDIO_DIR / f"{stem}.mp3"),
            "image_prompt": str(IMAGE_DIR / f"{stem}.txt"),
        }
        manifest.append(entry)
    out_path = OUTPUT_DIR / "final_manifest.json"
    out_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Wrote {out_path}")

if __name__ == "__main__":
    main()
