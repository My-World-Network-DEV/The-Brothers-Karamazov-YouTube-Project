"""
01_segment_text.py
------------------

Split the full novel text into smaller segments that later stages of the
pipeline can process individually.

Inputs
    brothers_karamazov_full.txt : The full text of the novel.

Outputs
    output_segments/segment_XXX.txt : One text file per segment.
"""

from pathlib import Path

def segment_text(input_file: Path, output_dir: Path) -> None:
    """Split the input text file into segments separated by blank lines."""
    output_dir.mkdir(parents=True, exist_ok=True)
    if not input_file.exists():
        raise FileNotFoundError(f"Input file {input_file} not found")

    text = input_file.read_text(encoding="utf-8")
    raw_segments = [s.strip() for s in text.split("\n\n") if s.strip()]

    for idx, segment in enumerate(raw_segments, start=1):
        out_path = output_dir / f"segment_{idx:03d}.txt"
        out_path.write_text(segment, encoding="utf-8")

    print(f"Wrote {len(raw_segments)} segments to {output_dir}")

if __name__ == "__main__":
    segment_text(Path("brothers_karamazov_full.txt"), Path("output_segments"))
