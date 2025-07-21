# 🎤 Voice Cloner RXC

**High-quality voice cloning using XTTS v2 with multiple deployment options**

A professional-grade voice cloning system that lets you clone any voice with just a short audio sample. Choose between local Gradio interface or Google Colab for cloud-based usage.

## ⚡ Quick Start

### 🌐 Option 1: Google Colab (Recommended for beginners)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/justtdhruvv/voice-cloner/blob/main//colab-notebook/XTTS_Voice_Cloner_Colab.ipynb)

**Perfect for:** First-time users, no installation required, free GPU access

### 💻 Option 2: Local Gradio Interface (For developers/power users)
```bash
cd voice_cloner-rxc/gradio-interface
pip install -r requirements.txt
python voice_cloner_gradio.py
```

**Perfect for:** Local deployment, server hosting, custom modifications

## 🎯 Features

| Feature | Colab Version | Gradio Interface |
|---------|---------------|------------------|
| Zero Installation | ✅ | ❌ |
| Free GPU Access | ✅ | ⚠️ (Need local GPU) |
| Public Sharing | ✅ | ✅ |
| Custom Modifications | ⚠️ Limited | ✅ |
| Offline Usage | ❌ | ✅ |
| Session Persistence | ❌ (12 hours) | ✅ |

### Core Capabilities
- 🎤 **High-Quality Voice Cloning** - State-of-the-art XTTS v2 model
- 🌍 **16+ Languages** - Multilingual text-to-speech support
- 🎨 **Professional UI** - Beautiful, user-friendly interface
- 📱 **Mobile Friendly** - Works on phones and tablets
- 🔊 **Audio Validation** - Automatic quality checking
- 📥 **Easy Downloads** - One-click audio file downloads
- 🚀 **Real-time Progress** - Live updates during generation

## 📁 Project Structure

```
voice_cloner-rxc/
├── 🌐 colab-notebook/          # Google Colab version
│   ├── XTTS_Voice_Cloner_Colab.ipynb
│   └── README.md
├── 💻 gradio-interface/        # Local Gradio version  
│   ├── voice_cloner_gradio.py
│   ├── requirements.txt
│   └── README.md
├── 📁 examples/                # Sample files
│   ├── sample_script.md
│   └── README.md
└── README.md                   # This file
```

## 🚀 How to Use

### Step 1: Choose Your Version
- **New to voice cloning?** → Use Google Colab version
- **Want local control?** → Use Gradio interface version

### Step 2: Prepare Your Audio
- **Duration**: 10-30 seconds of clear speech
- **Format**: WAV, MP3, FLAC, M4A, or OGG
- **Quality**: Minimal background noise, clear pronunciation

### Step 3: Generate Speech
1. Upload your reference audio
2. Enter the text you want spoken
3. Select language (16+ options)
4. Click generate and wait for magic! ✨

## 🌍 Supported Languages

English • Spanish • French • German • Italian • Portuguese • Polish • Turkish • Russian • Dutch • Czech • Arabic • Chinese • Japanese • Hungarian • Korean

## 💡 Pro Tips

### 🎤 Best Reference Audio:
- Record yourself reading for 10-15 seconds
- Use a quiet room with minimal echo
- Speak naturally (not too fast/slow)
- Avoid background music or noise

### 📝 Optimal Text Input:
- Keep under 1000 characters for best performance
- Use proper punctuation for natural pauses
- Match the language of your reference audio

### ⚡ Performance Tips:
- GPU recommended for faster generation
- Shorter text = faster processing
- High-quality reference audio = better results

## 🛠️ Technical Requirements

### Google Colab Version:
- ✅ **No installation required**
- ✅ **Free GPU access**
- ⚠️ **Internet connection needed**

### Local Gradio Version:
- 🐍 **Python 3.8+**
- 💾 **4GB RAM minimum** (8GB+ recommended)
- 🔥 **CUDA GPU** (optional but faster)
- 💽 **2GB disk space** for models

## 🆘 Troubleshooting

**Model won't download:**
- Check internet connection
- Ensure 2GB+ free disk space
- Try restarting the application

**Poor voice quality:**
- Use higher quality reference audio
- Ensure audio is 3-30 seconds long
- Check for background noise

**Slow generation:**
- Enable GPU if available
- Reduce text length
- Close other applications

## 📄 License & Ethics

This project is open source and free to use. However, please use responsibly:

- ✅ **Personal projects and experimentation**
- ✅ **Educational and research purposes**  
- ✅ **Content creation with proper disclosure**
- ❌ **Impersonation or fraud**
- ❌ **Harassment or harmful content**
- ❌ **Commercial use without consent**

## 🤝 Contributing

Contributions welcome! Please feel free to:
- 🐛 Report bugs and issues
- 💡 Suggest new features
- 🔧 Submit pull requests
- 📚 Improve documentation

## 🌟 Show Your Support

If you find this project useful:
- ⭐ Star this repository
- 🔗 Share with friends
- 🐛 Report issues you find
- 💡 Suggest improvements

---

**Ready to clone some voices?** Choose your preferred version above and start experimenting! 🎤✨

*Powered by XTTS v2 • Built with ❤️ for the AI community*
