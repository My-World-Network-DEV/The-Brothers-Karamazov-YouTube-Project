# The Brothers Karamazov YouTube Project

This repository contains a modular pipeline for turning Fyodor Dostoevsky's *The Brothers Karamazov* into an illustrated audiobook or video. Each stage is a small script so humans and AIs can extend or replace components.

## Project Structure
- `brothers_karamazov_full.txt` – placeholder for the full novel.
- `scripts/` – processing scripts numbered in pipeline order.
- `output_segments/` – text segments generated from the novel.
- `output_audio/` – placeholder audio files.
- `output_images/` – image prompts or generated images.
- `manifests/` – JSON files describing pipeline results.

## Quickstart
1. Install dependencies: `pip install -r requirements.txt`
2. Add the novel text to `brothers_karamazov_full.txt`.
3. Run the scripts sequentially:
   ```bash
   python scripts/01_segment_text.py
   python scripts/02_detect_dialogue.py
   python scripts/03_generate_tts.py
   python scripts/04_generate_image_prompts.py
   python scripts/05_create_manifest.py
   ```

Each script creates the directories it needs and writes output for the next stage.

## Pipeline Summary
1. **Segment Text** – Break the novel into manageable pieces.
2. **Detect Dialogue** – Identify spoken lines and speakers.
3. **Generate TTS** – Produce audio for each segment (stubbed).
4. **Generate Image Prompts** – Create prompts or placeholder images.
5. **Create Manifest** – Produce a JSON manifest linking text, audio and images for video assembly.

Contributions are welcome; the project is designed to be easily extended by other humans or AI systems.
