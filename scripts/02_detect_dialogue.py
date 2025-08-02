"""Detect dialogue lines within segmented text.

Inputs:
    - Text segments in output_segments/.
Outputs:
    - JSON file in manifests/ named dialogue.json containing
      detected dialogue lines per segment.

This implementation is rudimentary and assumes dialogue is enclosed in quotes.
"""
import json
import re
from pathlib import Path

def detect_dialogue(segments_dir: Path, manifest_path: Path) -> None:
    """Detect quoted dialogue and attribute a generic speaker.

    Args:
        segments_dir: Directory containing text segments.
        manifest_path: Path to the output JSON manifest.
    """
    manifest = {}
    for segment_file in sorted(segments_dir.glob("segment_*.txt")):
        text = segment_file.read_text(encoding="utf-8")
        lines = re.findall(r"\"(.*?)\"", text)
        if not lines:
            continue
        manifest[segment_file.name] = [
            {"speaker": "Unknown", "line": line} for line in lines
        ]
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

def main() -> None:
    root = Path(__file__).resolve().parent.parent
    segments_dir = root / "output_segments"
    manifest_path = root / "manifests" / "dialogue.json"
    detect_dialogue(segments_dir, manifest_path)

if __name__ == "__main__":
    main()
