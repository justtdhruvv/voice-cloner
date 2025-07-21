import os
import sys
import argparse
from TTS.api import TTS
import torch

# Default paths (can be overridden via command line arguments)
DEFAULT_REFERENCE_AUDIO = "../examples/test_reference.wav"
DEFAULT_SCRIPT_PATH = "../examples/sample_script.md"
DEFAULT_OUTPUT_DIR = "output"
DEFAULT_LANGUAGE = "en"

def find_reference_audio():
    """Find available reference audio files in examples directory."""
    examples_dir = "../examples"
    if not os.path.exists(examples_dir):
        examples_dir = "examples"
    
    if not os.path.exists(examples_dir):
        return None
    
    # Look for common audio file extensions
    audio_extensions = ['.wav', '.mp3', '.flac', '.m4a', '.ogg']
    audio_files = []
    
    for file in os.listdir(examples_dir):
        if any(file.lower().endswith(ext) for ext in audio_extensions):
            audio_files.append(os.path.join(examples_dir, file))
    
    return audio_files[0] if audio_files else None

def main():
    parser = argparse.ArgumentParser(description="XTTS Voice Cloner - Batch Processing")
    parser.add_argument("--reference", "-r", 
                       help="Path to reference audio file")
    parser.add_argument("--script", "-s", 
                       help="Path to script text file")
    parser.add_argument("--output", "-o", 
                       help="Output audio file path")
    parser.add_argument("--language", "-l", default=DEFAULT_LANGUAGE,
                       help="Language code (default: en)")
    
    args = parser.parse_args()
    
    # Determine reference audio file
    reference_audio = args.reference
    if not reference_audio:
        reference_audio = find_reference_audio()
        if not reference_audio:
            print("❌ No reference audio file found!")
            print("Please:")
            print("1. Place an audio file in the 'examples' directory, OR")
            print("2. Use --reference to specify the audio file path")
            print("\nExample usage:")
            print("  python batch_cloner.py --reference my_voice.wav --script my_text.txt")
            return
    
    # Determine script file
    script_path = args.script or DEFAULT_SCRIPT_PATH
    
    # Determine output path
    if args.output:
        output_path = args.output
        output_dir = os.path.dirname(output_path) or "."
    else:
        output_dir = DEFAULT_OUTPUT_DIR
        output_path = os.path.join(output_dir, "cloned_voice.wav")
    
    # Check reference audio
    if not os.path.exists(reference_audio):
        print(f"❌ Reference audio not found: {reference_audio}")
        return
        
    # Check script text
    if not os.path.exists(script_path):
        print(f"❌ Script file not found: {script_path}")
        print("Available script files:")
        examples_dir = os.path.dirname(script_path)
        if os.path.exists(examples_dir):
            for file in os.listdir(examples_dir):
                if file.endswith(('.txt', '.md')):
                    print(f"  - {os.path.join(examples_dir, file)}")
        return
        
    with open(script_path, "r", encoding="utf-8") as f:
        text = f.read().strip()
    if not text:
        print("❌ Script file is empty.")
        return
        
    print(f"✅ Loaded script from {script_path} (length: {len(text)} chars)")
    print(f"🎤 Using reference audio: {reference_audio}")
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Load model
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"🔥 Using device: {device}")
    
    try:
        print("📚 Loading XTTS model...")
        tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
        print("✅ Model loaded successfully!")
    except Exception as e:
        print(f"❌ Error loading TTS model: {e}")
        return
        
    print("🎵 Generating speech...")
    try:
        tts.tts_to_file(
            text=text,
            file_path=output_path,
            speaker_wav=reference_audio,
            language=args.language
        )
        print(f"🎉 Done! Output saved to: {output_path}")
        print(f"📊 Generated {len(text.split())} words in {args.language.upper()}")
    except Exception as e:
        print(f"❌ Error during synthesis: {e}")

if __name__ == "__main__":
    print("🎤 XTTS Voice Cloner - Batch Processing")
    print("=" * 50)
    main()
