#!/usr/bin/env python3
"""
Build script to generate MOBI dictionary file from XHTML output.

This script uses Calibre's ebook-convert tool to create a MOBI file
from the generated XHTML dictionary files.

Prerequisites:
    - Calibre must be installed (https://calibre-ebook.com)
    - Dictionary XHTML files must exist in the output/ directory

Usage:
    python build.py
"""

import os
import subprocess
import sys
from pathlib import Path


def check_calibre_installed():
    """Check if Calibre's ebook-convert is available."""
    try:
        # Try to run ebook-convert to check if it's installed
        result = subprocess.run(
            ['ebook-convert', '--version'],
            capture_output=True,
            text=True
        )
        return True
    except FileNotFoundError:
        return False


def find_ebook_convert():
    """Find the ebook-convert executable."""
    # Common Calibre installation paths
    common_paths = [
        r'C:\Program Files\Calibre2\ebook-convert.exe',
        r'C:\Program Files (x86)\Calibre2\ebook-convert.exe',
        '/usr/bin/ebook-convert',
        '/usr/local/bin/ebook-convert',
        '/Applications/calibre.app/Contents/MacOS/ebook-convert',
    ]

    # Check if ebook-convert is in PATH
    try:
        result = subprocess.run(['ebook-convert', '--version'],
                              capture_output=True, text=True)
        return 'ebook-convert'
    except FileNotFoundError:
        pass

    # Check common installation paths
    for path in common_paths:
        if os.path.exists(path):
            return path

    return None


def build_mobi():
    """Build the MOBI file from XHTML sources."""
    print("\033[1;36m" + "=" * 60 + "\033[0m")
    print("\033[1;36mBuilding Ukrainian-English Dictionary MOBI file\033[0m")
    print("\033[1;36m" + "=" * 60 + "\033[0m\n")

    # Check if output directory exists
    if not os.path.exists('output'):
        print("\033[1;31mError: output/ directory not found.\033[0m")
        print("Please run 'python main.py' first to generate the dictionary files.")
        return False

    # Check if dictionary files exist
    opf_file = 'output/dictionary.opf'
    if not os.path.exists(opf_file):
        print(f"\033[1;31mError: {opf_file} not found.\033[0m")
        print("Please run 'python main.py' first to generate the dictionary files.")
        return False

    # Find ebook-convert
    ebook_convert = find_ebook_convert()

    if not ebook_convert:
        print("\033[1;31mError: Calibre's ebook-convert not found.\033[0m")
        print("\nPlease install Calibre from: https://calibre-ebook.com")
        print("\nAfter installation:")
        print("  - On Windows: Add Calibre to your PATH")
        print("  - On macOS/Linux: ebook-convert should be available automatically")
        return False

    print(f"\033[1;32mOK - Found ebook-convert: {ebook_convert}\033[0m\n")

    # Output MOBI file
    output_mobi = 'uk-en-dictionary.mobi'

    print(f"\033[1;34mConverting to MOBI format...\033[0m")

    try:
        # Run ebook-convert
        cmd = [
            ebook_convert,
            opf_file,
            output_mobi,
            '--mobi-file-type=old',  # Use old MOBI format for better dictionary support
            '--no-inline-toc',  # Don't generate inline TOC for dictionaries
            '--mobi-ignore-margins',  # Ignore margins
        ]

        # Show live output instead of capturing it
        result = subprocess.run(cmd)

        if result.returncode == 0:
            file_size = os.path.getsize(output_mobi) / (1024 * 1024)
            print(f"\n\033[1;32mSUCCESS - Created {output_mobi}\033[0m")
            print(f"\033[1;32m  File size: {file_size:.1f} MB\033[0m\n")

            print("\033[1;36mNext steps:\033[0m")
            print("1. Copy the MOBI file to your Kindle's 'documents' folder")
            print("2. On your Kindle, go to Settings > Your Account > Language & Dictionaries")
            print("3. Select this dictionary as the default Ukrainian dictionary\n")
            return True
        else:
            print(f"\033[1;31mError during conversion (exit code {result.returncode})\033[0m")
            return False

    except Exception as e:
        print(f"\033[1;31mError: {e}\033[0m")
        return False


if __name__ == "__main__":
    success = build_mobi()
    sys.exit(0 if success else 1)
