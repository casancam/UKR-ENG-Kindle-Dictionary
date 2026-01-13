#!/usr/bin/env python3
import os
import subprocess
import sys
from pathlib import Path

def find_kindlegen():
    """Find the KindleGen executable (much better for dictionaries than Calibre)."""
    common_paths = [
        'kindlegen', 
        # Windows Path (Update <YourUsername> or use the dynamic one below)
        f'C:\\Users\\Casancam\\AppData\\Local\\Amazon\\Kindle Previewer 3\\lib\\fc\\bin\\kindlegen.exe',
        # macOS Path
        '/Applications/Kindle Previewer 3.app/Contents/lib/fc/bin/kindlegen',
    ]

    for path in common_paths:
        try:
            # Check if it works
            subprocess.run([path], capture_output=True)
            return path
        except FileNotFoundError:
            continue
    return None

def build_mobi():
    print("\033[1;36mBuilding Kindle Dictionary with KindleGen\033[0m\n")

    opf_file = 'output/dictionary.opf'
    kindlegen = find_kindlegen()

    if not kindlegen:
        print("\033[1;31mError: KindleGen not found.\033[0m")
        print("Calibre's ebook-convert often strips dictionary metadata.")
        print("Please download KindleGen or Kindle Previewer 3.")
        return False

    output_mobi = 'uk-en-dictionary.mobi'
    
    # KindleGen creates the .mobi in the same folder as the .opf
    # We will move it afterwards.
    try:
        # -c2 means standard compression (smaller file)
        # -verbose helps debug why Kindle might reject a record
        cmd = [kindlegen, opf_file, '-c0', '-o', output_mobi]
        
        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd)

        # KindleGen returns 1 for warnings, 2 for errors. 
        # Usually, warnings (1) still produce a working file.
        if result.returncode in [0, 1]:
            generated_path = Path('output') / output_mobi
            final_path = Path('.') / output_mobi
            
            if generated_path.exists():
                os.replace(generated_path, final_path)
                print(f"\n\033[1;32mSUCCESS - Created {output_mobi}\033[0m")
                return True
        
        print(f"\033[1;31mError: KindleGen failed with code {result.returncode}\033[0m")
        return False

    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    success = build_mobi()
    sys.exit(0 if success else 1)