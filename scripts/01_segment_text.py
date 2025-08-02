"""Segment the full novel text into smaller pieces.

Inputs:
    - brothers_karamazov_full.txt: placeholder for the complete novel text.
Outputs:
    - Individual text files in output_segments/ named segment_XXXX.txt.

Each segment is a simple chunk of characters; this is a naive splitter meant
for later refinement.
"""
from pathlib import Path

def segment_text(input_file: Path, output_dir: Path, segment_size: int = 1000) -> None:
    """Split the input text into segments and save them.

    Args:
        input_file: Path to the novel text.
        output_dir: Directory to write segment files.
        segment_size: Approximate number of characters per segment.
    """
    text = input_file.read_text(encoding="utf-8")
    output_dir.mkdir(parents=True, exist_ok=True)

    for i in range(0, len(text), segment_size):
        segment = text[i:i + segment_size].strip()
        if not segment:
            continue
        segment_path = output_dir / f"segment_{i // segment_size:04d}.txt"
        segment_path.write_text(segment, encoding="utf-8")

def main() -> None:
    root = Path(__file__).resolve().parent.parent
    input_file = root / "brothers_karamazov_full.txt"
    output_dir = root / "output_segments"
    segment_text(input_file, output_dir)

if __name__ == "__main__":
    main()
