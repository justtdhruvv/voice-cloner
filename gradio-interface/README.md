# 🎤 XTTS Voice Cloner - Gradio Interface

A professional web interface for high-quality voice cloning using XTTS v2. Perfect for local deployment or server hosting.

## ⚡ Features

- **Professional Web Interface** - Clean, user-friendly Gradio interface
- **High-Quality Voice Cloning** - Uses XTTS v2 for state-of-the-art results
- **16+ Language Support** - Multilingual text-to-speech generation
- **Audio Validation** - Automatic file format and quality checking
- **Real-time Progress** - Live updates during voice generation
- **GPU Acceleration** - Automatic CUDA detection and usage
- **Download Support** - Easy download of generated audio files

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- CUDA-compatible GPU (recommended, but CPU works too)
- At least 4GB RAM (8GB+ recommended)

### Installation

1. **Clone this repository:**
   ```bash
   git clone <your-repo-url>
   cd voice_cloner-rxc/gradio-interface
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python voice_cloner_gradio.py
   ```

4. **Open the web interface:**
   - The browser should open automatically
   - Or go to: `http://localhost:7861`
   - For sharing: Use the public URL displayed in terminal

## 💡 How to Use

1. **Upload Reference Audio** - A clear 3-30 second recording of the target voice
2. **Enter Text** - What you want the AI to say (up to 1000 characters)
3. **Select Language** - Choose from 16+ supported languages
4. **Generate** - Click the button and wait for the magic! ✨

### 📋 Audio Requirements

- **Format**: WAV, MP3, FLAC, M4A, OGG
- **Duration**: 3-30 seconds (optimal)
- **Quality**: Clear speech, minimal background noise
- **Size**: Under 50MB

## 🌍 Supported Languages

English, Spanish, French, German, Italian, Portuguese, Polish, Turkish, Russian, Dutch, Czech, Arabic, Chinese, Japanese, Hungarian, Korean

## 🛠️ Configuration

- **Port**: Change `server_port=7861` in the main function
- **GPU/CPU**: Automatically detected, or force CPU by setting `CUDA_VISIBLE_DEVICES=""`
- **Model**: Using `tts_models/multilingual/multi-dataset/xtts_v2`

## 📝 Example Usage

```python
# For programmatic usage:
from voice_cloner_gradio import XTTSVoiceCloner

cloner = XTTSVoiceCloner()
cloner.tts.tts_to_file(
    text="Hello, this is a test!",
    file_path="output.wav",
    speaker_wav="reference.wav",
    language="en"
)
```

## 🚨 Troubleshooting

**Model loading fails:**
- Check internet connection for first-time download
- Ensure sufficient disk space (2GB+)
- Try running with `--retries 5` flag

**GPU not detected:**
- Install CUDA toolkit
- Verify with `torch.cuda.is_available()`

**Port already in use:**
- Change port number in the code
- Or kill existing process: `lsof -ti:7861 | xargs kill -9`

## 📄 License

Open source project - feel free to modify and distribute!

## 🤝 Contributing

Contributions welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.
