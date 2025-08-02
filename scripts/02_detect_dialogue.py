"""
02_detect_dialogue.py
---------------------

Detect dialogue lines in each text segment and produce a manifest
that attributes the lines to speakers when possible.

Inputs
    output_segments/*.txt : Text segments created in the previous step.

Outputs
    manifests/dialogue_manifest.json : JSON mapping of segments to dialogue lines.
"""

from pathlib import Path
import json

SEGMENT_DIR = Path("output_segments")
OUTPUT_DIR = Path("manifests")

def detect_dialogue(text: str) -> list:
    """Very naive dialogue detection based on lines starting with quotes."""
    dialogues = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith(('"', '“')):
            dialogues.append({"speaker": None, "line": stripped})
    return dialogues

def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest = {}
    for seg_file in sorted(SEGMENT_DIR.glob("*.txt")):
        text = seg_file.read_text(encoding="utf-8")
        manifest[seg_file.name] = detect_dialogue(text)
    out_path = OUTPUT_DIR / "dialogue_manifest.json"
    out_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Wrote dialogue manifest for {len(manifest)} segments to {out_path}")

if __name__ == "__main__":
    main()
