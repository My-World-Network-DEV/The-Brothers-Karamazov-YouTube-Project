# The Brothers Karamazov YouTube Project

An experiment in building a modular, AI-assisted pipeline for creating an illustrated audiobook/video of Fyodor Dostoevsky's *The Brothers Karamazov*.

## Overview
This repository demonstrates an end-to-end workflow:
1. **Segment the novel** into manageable pieces.
2. **Detect dialogue** and associate speakers.
3. **Generate text-to-speech (TTS)** audio for each segment.
4. **Generate image prompts** corresponding to the scenes or dialogue.
5. **Create a manifest** linking text, audio, and imagery for video assembly.

## Quickstart
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Add the full novel text to `brothers_karamazov_full.txt`.
3. Run the scripts sequentially:
   ```bash
   python scripts/01_segment_text.py
   python scripts/02_detect_dialogue.py
   python scripts/03_generate_tts.py
   python scripts/04_generate_image_prompts.py
   python scripts/05_create_manifest.py
   ```
4. Use the generated manifest and assets to assemble your video.

## Notes
- All scripts are stubs intended for extension by humans or AIs.
- Output directories are populated with placeholder files; real outputs will appear after running the pipeline.
- Contributions and improvements are welcome.
