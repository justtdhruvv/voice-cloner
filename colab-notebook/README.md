# 🎤 XTTS Voice Cloner - Google Colab

Run this powerful voice cloning system directly in Google Colab - no local installation required!

## 🚀 Quick Start

### Option 1: Direct Colab Link
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/your-username/your-repo/blob/main/voice_cloner-rxc/colab-notebook/XTTS_Voice_Cloner_Colab.ipynb)

### Option 2: Manual Setup
1. Go to [Google Colab](https://colab.research.google.com/)
2. Upload the `XTTS_Voice_Cloner_Colab.ipynb` file
3. Run all cells (Runtime → Run all)
4. Use the web interface that opens!

## ⚡ Features

- **Zero Installation** - Runs entirely in Google Colab
- **Free GPU Access** - T4/V100 GPUs available for faster processing
- **Public Sharing** - Get shareable URLs for others to use
- **Professional Interface** - Beautiful Gradio web UI
- **16+ Languages** - Multilingual voice cloning support
- **Real-time Progress** - Live updates during generation

## 📋 How to Use

1. **Enable GPU** (Important!)
   - Runtime → Change runtime type → Hardware accelerator → GPU

2. **Run the Notebook**
   - Runtime → Run all (or Ctrl+F9)
   - Wait for model download (first time only)

3. **Use the Interface**
   - Upload your reference audio (3-30 seconds)
   - Enter text to convert to speech
   - Select language
   - Click "Generate Cloned Voice"

4. **Share with Others**
   - Copy the public URL from the output
   - Share with friends/colleagues
   - They can use it without running the notebook

## 🎯 Perfect For

- **Content Creators** - Generate voiceovers quickly
- **Educators** - Create engaging educational content
- **Accessibility** - Text-to-speech for various needs
- **Prototyping** - Test voice concepts rapidly
- **Demonstrations** - Show voice cloning capabilities

## 💡 Tips for Best Results

### Audio Quality
- **Duration**: 3-10 seconds of clear speech
- **Format**: WAV, MP3, FLAC preferred
- **Content**: Natural speaking, no background noise
- **Volume**: Clear and audible

### Text Input
- **Length**: Keep under 1000 characters for best performance
- **Language**: Match the reference speaker's language
- **Punctuation**: Use proper punctuation for natural pauses

## 🚨 Important Notes

- **Session Limits**: Colab sessions expire after 12 hours of inactivity
- **GPU Quota**: Limited free GPU hours per day
- **Temporary Files**: Download results before session ends
- **Public URLs**: Expire when Colab session ends

## 🌟 What You Get

✅ **High-quality voice cloning** with XTTS v2  
✅ **Professional web interface** with Gradio  
✅ **Real-time progress tracking**  
✅ **Audio validation and processing**  
✅ **Download generated speech**  
✅ **Mobile-friendly interface**  
✅ **Public sharing capability**  
✅ **16+ language support**  

## 🔧 Advanced Usage

### Custom Examples
The notebook includes example texts, but you can add your own:
1. Scroll to the "Example Texts" section
2. Modify the `get_example_text()` function
3. Add your custom examples

### Language Support
Current supported languages:
- English, Spanish, French, German, Italian, Portuguese
- Polish, Turkish, Russian, Dutch, Czech, Arabic
- Chinese, Japanese, Hungarian, Korean

### GPU vs CPU
- **GPU**: ~30 seconds for short text
- **CPU**: ~2-3 minutes for short text
- Always enable GPU in Colab for best experience

## 🤝 Sharing Your Results

1. **Download Audio**: Click ⋯ menu in audio player → Download
2. **Share Interface**: Copy the `https://xxxxxxx.gradio.live` URL
3. **Social Media**: Share your voice cloning experiments!

## 🆘 Troubleshooting

**Model won't load:**
- Check internet connection
- Restart runtime and try again
- Make sure GPU is enabled

**Interface won't open:**
- Look for the public URL in the output
- Try refreshing the page
- Check browser pop-up blockers

**Audio generation fails:**
- Verify audio file is valid format
- Check text length (under 1000 chars)
- Try shorter reference audio

## 📱 Mobile Support

The interface works great on mobile devices:
- Upload audio from phone gallery
- Type or paste text easily
- Listen to results directly
- Download generated audio

---

**Ready to clone some voices?** Open the notebook and start experimenting! 🎤✨
