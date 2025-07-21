import os
from TTS.api import TTS
import torch

REFERENCE_AUDIO = "examples/01_REFERENCE_ElevenLabs.wav"
SCRIPT_PATH = "examples/script.md"
OUTPUT_DIR = "doutput"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "Reel1.wav")
LANGUAGE = "en"

def main():
    # Check reference audio
    if not os.path.exists(REFERENCE_AUDIO):
        print(f"Reference audio not found: {REFERENCE_AUDIO}")
        return
    # Read script text
    if not os.path.exists(SCRIPT_PATH):
        print(f"Script file not found: {SCRIPT_PATH}")
        return
    with open(SCRIPT_PATH, "r", encoding="utf-8") as f:
        text = f.read().strip()
    if not text:
        print("Script file is empty.")
        return
    print(f"Loaded script from {SCRIPT_PATH} (length: {len(text)} chars)")
    print(f"Using reference audio: {REFERENCE_AUDIO}")
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Load model
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")
    try:
        tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
    except Exception as e:
        print(f"Error loading TTS model: {e}")
        return
    print("Model loaded. Generating speech...")
    try:
        tts.tts_to_file(
            text=text,
            file_path=OUTPUT_PATH,
            speaker_wav=REFERENCE_AUDIO,
            language=LANGUAGE
        )
        print(f"Done! Output saved to: {OUTPUT_PATH}")
    except Exception as e:
        print(f"Error during synthesis: {e}")

if __name__ == "__main__":
    main()
