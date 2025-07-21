# 🔧 Batch Cloner Usage Guide

The `batch_cloner.py` script allows you to generate voice clones from the command line without a web interface.

## 🚀 Quick Start

### Basic Usage (Auto-detect files)
```bash
python batch_cloner.py
```
This will automatically:
- Look for audio files in `../examples/` directory
- Use `../examples/sample_script.md` as the script
- Save output to `output/cloned_voice.wav`

### Custom Usage
```bash
python batch_cloner.py --reference my_voice.wav --script my_text.txt --output my_output.wav
```

## 📋 Command Line Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--reference` | `-r` | Path to reference audio file | Auto-detect |
| `--script` | `-s` | Path to script text file | `../examples/sample_script.md` |
| `--output` | `-o` | Output audio file path | `output/cloned_voice.wav` |
| `--language` | `-l` | Language code | `en` |

## 💡 Examples

### Example 1: Use specific files
```bash
python batch_cloner.py -r voice_sample.wav -s my_script.txt -o result.wav
```

### Example 2: Different language
```bash
python batch_cloner.py -r spanish_voice.wav -s spanish_text.txt -l es
```

### Example 3: Auto-detect audio
```bash
python batch_cloner.py -s my_custom_script.md
```

## 📁 File Organization

### Expected Structure:
```
gradio-interface/
├── batch_cloner.py          # This script
├── output/                  # Generated audio files
└── ../examples/             # Reference audio and scripts
    ├── test_reference.wav   # Sample audio
    └── sample_script.md     # Sample text
```

## 🎤 Audio Requirements

- **Formats**: WAV, MP3, FLAC, M4A, OGG
- **Duration**: 3-30 seconds recommended
- **Quality**: Clear speech, minimal background noise

## 📝 Script Requirements

- **Formats**: .txt, .md files
- **Encoding**: UTF-8
- **Length**: Up to 1000 characters recommended

## 🌍 Supported Languages

Use these codes with the `-l` option:

| Language | Code | Language | Code |
|----------|------|----------|------|
| English | `en` | Spanish | `es` |
| French | `fr` | German | `de` |
| Italian | `it` | Portuguese | `pt` |
| Polish | `pl` | Turkish | `tr` |
| Russian | `ru` | Dutch | `nl` |
| Czech | `cs` | Arabic | `ar` |
| Chinese | `zh-cn` | Japanese | `ja` |
| Hungarian | `hu` | Korean | `ko` |

## 🚨 Troubleshooting

**No reference audio found:**
```bash
❌ No reference audio file found!
Please:
1. Place an audio file in the 'examples' directory, OR
2. Use --reference to specify the audio file path
```
**Solution:** Add an audio file to the examples directory or specify the path.

**Script file not found:**
```bash
❌ Script file not found: ../examples/sample_script.md
```
**Solution:** Create the script file or specify a different path with `-s`.

**Model loading fails:**
```bash
❌ Error loading TTS model: [error message]
```
**Solution:** Check internet connection for first-time model download.

## ⚡ Performance Tips

- **GPU**: Automatically detected and used if available
- **CPU**: Works but slower (2-3x longer generation time)
- **Memory**: Ensure 4GB+ RAM for large texts

## 🔄 Workflow Examples

### Content Creation Workflow:
1. Record your voice (10-15 seconds): `my_voice.wav`
2. Write your script: `script.txt`
3. Generate: `python batch_cloner.py -r my_voice.wav -s script.txt`

### Batch Processing Multiple Files:
```bash
# Process multiple scripts with same voice
python batch_cloner.py -r voice.wav -s script1.txt -o output1.wav
python batch_cloner.py -r voice.wav -s script2.txt -o output2.wav
python batch_cloner.py -r voice.wav -s script3.txt -o output3.wav
```

## 🎯 Integration with Other Tools

The batch cloner can be integrated into larger workflows:

```bash
# Example: Generate multiple audio files
for script in scripts/*.txt; do
    output="output/$(basename "$script" .txt).wav"
    python batch_cloner.py -r reference.wav -s "$script" -o "$output"
done
```

Perfect for:
- **Automated content generation**
- **Batch processing scripts**
- **CI/CD pipelines**
- **Content creation workflows**
