#!/usr/bin/env python3
"""
XTTS Voice Cloner - Gradio Web Interface
High-quality voice cloning using XTTS v2 with a user-friendly web interface.
"""

import os
import time
import torch
import torchaudio
import gradio as gr
import numpy as np
from pathlib import Path
import tempfile
import warnings
warnings.filterwarnings("ignore")

from TTS.api import TTS

class XTTSVoiceCloner:
    def __init__(self, max_retries=3):
        """Initialize XTTS model with robust error handling."""
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tts = None
        
        print(f"🔄 Loading XTTS model on {self.device}...")
        
        for attempt in range(max_retries):
            try:
                print(f"   Attempt {attempt + 1}/{max_retries}...")
                self.tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(self.device)
                print("✅ XTTS model loaded successfully!")
                break
            except Exception as e:
                print(f"❌ Error loading model (attempt {attempt + 1}): {str(e)}")
                if attempt == max_retries - 1:
                    print("🚨 Failed to load model after all retries!")
                    raise e
                print("⏳ Retrying in 10 seconds...")
                time.sleep(10)
    
    def get_supported_languages(self):
        """Return list of supported languages."""
        return [
            ("English", "en"), ("Spanish", "es"), ("French", "fr"), 
            ("German", "de"), ("Italian", "it"), ("Portuguese", "pt"),
            ("Polish", "pl"), ("Turkish", "tr"), ("Russian", "ru"),
            ("Dutch", "nl"), ("Czech", "cs"), ("Arabic", "ar"),
            ("Chinese", "zh-cn"), ("Japanese", "ja"), ("Hungarian", "hu"), ("Korean", "ko")
        ]

def validate_audio_file(audio_file):
    """Validate uploaded audio file."""
    if audio_file is None:
        return False, "❌ No audio file uploaded!"
    
    # Check file size (max 50MB)
    file_size = os.path.getsize(audio_file) / (1024 * 1024)  # MB
    if file_size > 50:
        return False, f"❌ File too large ({file_size:.1f}MB). Max size: 50MB"
    
    # Check file extension
    valid_extensions = ['.wav', '.mp3', '.flac', '.m4a', '.ogg']
    file_ext = os.path.splitext(audio_file)[1].lower()
    if file_ext not in valid_extensions:
        return False, f"❌ Unsupported format: {file_ext}. Use: {', '.join(valid_extensions)}"
    
    return True, "✅ Audio file is valid!"

def get_audio_info(audio_file):
    """Get information about the audio file."""
    try:
        import librosa
        y, sr = librosa.load(audio_file, sr=None)
        duration = len(y) / sr
        
        return {
            "duration": duration,
            "sample_rate": sr,
            "channels": 1 if len(y.shape) == 1 else y.shape[0],
            "format": os.path.splitext(audio_file)[1][1:].upper()
        }
    except Exception as e:
        return {"error": str(e)}

def process_reference_audio(audio_file):
    """Process and validate reference audio for voice cloning."""
    if not audio_file:
        return None, "❌ Please upload a reference audio file!"
    
    # Validate file
    is_valid, message = validate_audio_file(audio_file)
    if not is_valid:
        return None, message
    
    # Get audio info
    info = get_audio_info(audio_file)
    if "error" in info:
        return None, f"❌ Error reading audio: {info['error']}"
    
    # Check duration (recommend 3-30 seconds)
    duration = info["duration"]
    if duration < 1:
        return None, "⚠️ Audio too short! Use 3-30 seconds for best results."
    elif duration > 60:
        return None, "⚠️ Audio too long! Use 3-30 seconds for best results."
    
    status_msg = f"✅ Audio processed successfully!\n"
    status_msg += f"📊 Duration: {duration:.1f}s | Sample Rate: {info['sample_rate']}Hz | Format: {info['format']}"
    
    if duration < 3:
        status_msg += "\n💡 Tip: 3-10 seconds of clear speech works best!"
    
    return audio_file, status_msg

def clone_voice(reference_audio, input_text, language, progress=gr.Progress()):
    """Main function to clone voice using reference audio and input text."""
    
    # Progress tracking
    progress(0.1, desc="🔍 Validating inputs...")
    
    # Validate inputs
    if not reference_audio:
        return None, "❌ Please upload a reference audio file!"
    
    if not input_text or len(input_text.strip()) < 5:
        return None, "❌ Please enter text (at least 5 characters)!"
    
    if len(input_text) > 1000:
        return None, "❌ Text too long! Please keep it under 1000 characters."
    
    progress(0.2, desc="🎵 Processing reference audio...")
    
    # Process reference audio
    processed_audio, audio_status = process_reference_audio(reference_audio)
    if not processed_audio:
        return None, audio_status
    
    progress(0.4, desc="🤖 Generating speech...")
    
    try:
        # Create temporary output file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
            output_path = tmp_file.name
        
        # Generate speech using XTTS
        voice_cloner.tts.tts_to_file(
            text=input_text.strip(),
            file_path=output_path,
            speaker_wav=processed_audio,
            language=language
        )
        
        progress(0.9, desc="✅ Finalizing...")
        
        # Check if output file was created successfully
        if not os.path.exists(output_path) or os.path.getsize(output_path) == 0:
            return None, "❌ Failed to generate audio. Please try again."
        
        progress(1.0, desc="🎉 Complete!")
        
        # Success message
        char_count = len(input_text)
        word_count = len(input_text.split())
        success_msg = f"🎉 Voice cloning successful!\n"
        success_msg += f"📝 Generated {word_count} words ({char_count} characters)\n"
        success_msg += f"🎤 Language: {language.upper()}\n"
        success_msg += f"🔊 Audio ready for playback!"
        
        return output_path, success_msg
        
    except Exception as e:
        error_msg = f"❌ Error during voice generation: {str(e)}"
        print(f"Voice cloning error: {e}")
        return None, error_msg

def get_example_text():
    """Return example text for demonstration."""
    examples = [
        "Hello! This is a test of the voice cloning system. How do I sound?",
        "Welcome to our AI voice cloning demo. This technology can replicate voices with just a short audio sample.",
        "The quick brown fox jumps over the lazy dog. This sentence contains every letter of the alphabet.",
        "In a world where technology advances rapidly, voice cloning represents a fascinating frontier in artificial intelligence."
    ]
    return examples

def create_gradio_interface():
    """Create and configure the Gradio web interface."""
    
    # Custom CSS for better styling
    custom_css = """
    .gradio-container {
        max-width: 1200px !important;
        margin: auto !important;
    }
    .header {
        text-align: center;
        margin-bottom: 2rem;
    }
    .info-box {
        background: linear-gradient(45deg, #f0f9ff, #e0f2fe);
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #0ea5e9;
        margin: 1rem 0;
    }
    """
    
    # Create the interface
    with gr.Blocks(css=custom_css, title="XTTS Voice Cloner", theme=gr.themes.Soft()) as interface:
        
        # Header
        gr.HTML("""
        <div class="header">
            <h1>🎤 XTTS Voice Cloner</h1>
            <p style="font-size: 1.2em; color: #666;">
                High-quality voice cloning using AI • Upload your voice, enter text, get AI speech!
            </p>
        </div>
        """)
        
        # Instructions
        gr.HTML("""
        <div class="info-box">
            <h3>📋 How to use:</h3>
            <ol>
                <li><strong>Upload Reference Audio:</strong> A clear 3-30 second recording of the target voice</li>
                <li><strong>Enter Text:</strong> What you want the AI to say (up to 1000 characters)</li>
                <li><strong>Select Language:</strong> Choose the language for speech generation</li>
                <li><strong>Generate:</strong> Click the button and wait for the magic! ✨</li>
            </ol>
            <p><strong>💡 Tips:</strong> Use high-quality audio with minimal background noise for best results!</p>
        </div>
        """)
        
        with gr.Row():
            with gr.Column(scale=1):
                # Input section
                gr.HTML("<h3>🎯 Inputs</h3>")
                
                # File upload
                reference_audio = gr.Audio(
                    label="🎤 Reference Audio (Upload your voice sample)",
                    type="filepath",
                    sources=["upload"],
                    interactive=True
                )
                
                # Text input
                input_text = gr.Textbox(
                    label="📝 Text to Convert to Speech",
                    placeholder="Enter the text you want the AI to speak...",
                    lines=4,
                    max_lines=8,
                    interactive=True
                )
                
                # Language selection
                language_choices = voice_cloner.get_supported_languages()
                language = gr.Dropdown(
                    choices=language_choices,
                    value="en",
                    label="🌍 Language",
                    interactive=True
                )
                
                # Generate button
                generate_btn = gr.Button(
                    "🚀 Generate Cloned Voice",
                    variant="primary",
                    size="lg"
                )
                
                # Example texts
                gr.HTML("<h4>📚 Example Texts:</h4>")
                example_texts = get_example_text()
                for i, example in enumerate(example_texts):
                    gr.Button(
                        f"Example {i+1}",
                        size="sm"
                    ).click(
                        lambda x=example: x,
                        outputs=input_text
                    )
            
            with gr.Column(scale=1):
                # Output section
                gr.HTML("<h3>🎧 Results</h3>")
                
                # Status display
                status_output = gr.Textbox(
                    label="📊 Status",
                    interactive=False,
                    lines=6
                )
                
                # Audio player
                audio_output = gr.Audio(
                    label="🔊 Generated Speech",
                    interactive=False
                )
                
                # Download info
                gr.HTML("""
                <div style="background: #f8fafc; padding: 1rem; border-radius: 6px; margin-top: 1rem;">
                    <p><strong>💾 Download:</strong> Click the ⋯ menu in the audio player above to download your generated speech!</p>
                </div>
                """)
        
        # Footer
        gr.HTML("""
        <div style="text-align: center; margin-top: 2rem; padding: 1rem; border-top: 1px solid #e5e7eb;">
            <p style="color: #6b7280;">
                🚀 Powered by <strong>XTTS v2</strong> • 
                ❤️ Open Source AI
            </p>
        </div>
        """)
        
        # Connect the generate button
        generate_btn.click(
            fn=clone_voice,
            inputs=[reference_audio, input_text, language],
            outputs=[audio_output, status_output],
            show_progress=True
        )
    
    return interface

def main():
    """Main function to initialize and launch the voice cloner."""
    global voice_cloner
    
    print("🎤 XTTS Voice Cloner - Gradio Interface")
    print("=" * 50)
    
    # Check GPU availability
    print(f"🔥 CUDA available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"🚀 GPU device: {torch.cuda.get_device_name(0)}")
    else:
        print("⚠️  Running on CPU (slower but still works)")
    
    # Initialize the voice cloner
    voice_cloner = XTTSVoiceCloner()
    print("🎉 Voice cloner ready!")
    
    # Create and launch interface
    interface = create_gradio_interface()
    
    print("\n🚀 Launching web interface...")
    print("The interface will open in your browser automatically.")
    
    # Launch the interface
    interface.launch(
        server_name="0.0.0.0",
        server_port=7861,  # Changed port to avoid conflicts
        share=True,
        inbrowser=True,
        show_error=True
    )

if __name__ == "__main__":
    main()
