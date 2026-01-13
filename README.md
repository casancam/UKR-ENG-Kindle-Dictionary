# Ukrainian-English Dictionary for Kindle 🇺🇦🇬🇧

**A comprehensive Ukrainian-to-English dictionary for Kindle e-readers**

This Kindle-native dictionary enables seamless Ukrainian word lookups while reading, making it the perfect companion for English speakers learning Ukrainian or Ukrainian readers engaging with English content.

Compatible with all Kindle models and generations — including *Kindle Paperwhite*, *Oasis*, *Scribe* and others, it integrates directly into the Kindle lookup feature. It also works on any e-reader or app that supports MOBI dictionaries.

## Features

- 🔍 **Optimized for Kindle**. Look up Ukrainian words instantly without leaving your book
- 📚 **Comprehensive Database**. Over 30,000 Ukrainian words with English definitions
- ⚡ **Fast & Lightweight**. No lag, no hassle
- 📖 **Rich Definitions**. Includes part of speech, gender information, and multiple meanings
- 🎯 **Quality Source**. Based on Wiktionary and DBnary data
- 🔠 **Grammatical Info**. Includes verb aspects, noun genders, and usage examples

## Installation

### Download Pre-built Dictionary (Recommended)

1. **[Download uk-en-dictionary.mobi](https://github.com/casancam/UKR-ENG-Kindle-Dictionary/releases/download/1.0/uk-en-dictionary.mobi)** (8.1 MB)
2. Connect your Kindle to your computer via USB
3. Copy the MOBI file to your Kindle's `documents` folder
4. Safely eject your Kindle
5. On your Kindle:
   - Go to **Settings** > **Your Account** > **Language & Dictionaries**
   - Select this dictionary as the default Ukrainian dictionary

### Build from Source

If you prefer to build the dictionary yourself, see the [Development](#development) section below.

## Usage

Once installed, simply tap on any Ukrainian word while reading on your Kindle to see its English definition. The dictionary will automatically appear with:
- English translations
- Part of speech (noun, verb, adjective, etc.)
- Gender and case information (for nouns)
- Multiple definitions and usage contexts

## Development

### Prerequisites

- **Python 3.10+** (tested with Python 3.14)
- **Calibre** (for building MOBI files): [Download](https://calibre-ebook.com)

No additional Python dependencies are required. The scripts use only standard library modules.

### Building the Dictionary

```bash
# 1. Generate dictionary XHTML files
python main.py

# 2. Build MOBI file
python build.py
```

The final `uk-en-dictionary.mobi` file will be created in the project root.

### Project Structure

```
.
├── src/
│   └── ukr-eng-words.json.zip    # Compressed dictionary data (30K+ words)
├── scripts/
│   ├── 0.convert-json.py         # Extract and convert JSON to tab-separated format
│   ├── 1.crosslinks.py           # Process cross-references
│   ├── 2.clean-markup.py         # Clean HTML markup
│   └── 3.convert-to-xhtml.py     # Generate final XHTML dictionary files
├── output/
│   ├── dictionary.opf            # OPF metadata file for Kindle
│   ├── dictionary-1.xhtml        # Dictionary content (part 1)
│   ├── dictionary-2.xhtml        # Dictionary content (part 2)
│   └── dictionary-3.xhtml        # Dictionary content (part 3)
├── main.py                       # Main build script
└── build.py                      # MOBI conversion script
```

### Scripts

| Script | Purpose |
|--------|---------|
| [0.convert-json.py](scripts/0.convert-json.py) | Extracts dictionary data from compressed ZIP and converts to tab-separated format |
| [1.crosslinks.py](scripts/1.crosslinks.py) | Processes cross-references between dictionary entries |
| [2.clean-markup.py](scripts/2.clean-markup.py) | Cleans and standardizes HTML markup |
| [3.convert-to-xhtml.py](scripts/3.convert-to-xhtml.py) | Generates final XHTML files for Kindle |

## Acknowledgments

Thanks to these great resources that made this dictionary possible:

- **[dmklinger/ukrainian](https://github.com/dmklinger/ukrainian)** for providing the comprehensive Ukrainian-English dictionary data sourced from Wiktionary and DBnary. This project's data is distributed under the Creative Commons Attribution-ShareAlike 3.0 Unported License.

- **[pavlo-liapin/kindle-eng-ukr-dictionary](https://github.com/pavlo-liapin/kindle-eng-ukr-dictionary)** for the inspiration and reference base implementation for building Kindle dictionaries, which provided the foundation and approach for this project (used his EN-UK repo as a base).

- **Jake McCrary**'s article [Creating a custom Kindle dictionary](https://jakemccrary.com/blog/2020/11/11/creating-a-custom-kindle-dictionary/) for explaining the basics of the Kindle dictionary format.

## License

### Dictionary Data

The dictionary data is sourced from [dmklinger/ukrainian](https://github.com/dmklinger/ukrainian), which aggregates information from Wiktionary and DBnary. The data is distributed under the **Creative Commons Attribution-ShareAlike 3.0 Unported License**.

### Code

The scripts and build system in this repository are provided as-is for building Kindle dictionaries. Feel free to use and modify them for your own dictionary projects.

## Contributing

Contributions are welcome! If you find issues with definitions or have suggestions for improvements, please:

1. For dictionary content issues: Report them to the upstream [dmklinger/ukrainian](https://github.com/dmklinger/ukrainian) repository
2. For build system or script issues: Open an issue or pull request in this repository

## Support

Have questions or suggestions? Drop a message in the Issues tab or reach out on GitHub!

Happy reading! 📚✨
