import json
import os
import zipfile

def convert_json_to_txt(zip_path, output_path):
    """
    Convert the Ukrainian-English JSON dictionary to tab-separated format.
    Args:
        zip_path (str): Path to the ZIP file containing the JSON.
        output_path (str): Path to the output TXT file.
    """
    # Extract and load JSON from zip
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        json_filename = zip_ref.namelist()[0]  # Get the first file in zip
        with zip_ref.open(json_filename) as f:
            data = json.load(f)

    lines = []

    for entry in data:
        word = entry['word']
        pos = entry.get('pos', '')
        defs = entry.get('defs', [])
        info = entry.get('info', '')

        if not word or not defs:
            continue

        # Build the definition with markup
        definition_parts = []

        # Add part of speech if available
        if pos:
            definition_parts.append(f'<em>{pos}</em>')

        # Add info if available
        if info:
            definition_parts.append(f'<i>{info}</i>')

        # Add definitions as numbered list if multiple, otherwise just the definition
        if len(defs) == 1:
            definition_parts.append(defs[0])
        else:
            for i, definition in enumerate(defs, 1):
                definition_parts.append(f'{i}) {definition}')

        # Join all parts with line breaks
        full_definition = '<br>'.join(definition_parts)

        # Create the tab-separated line
        line = f'{word}\t{full_definition}'
        lines.append(line)

    # Write to output file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')

    print(f"Converted {len(lines)} entries from JSON to TXT format")
    print(f"Output saved to: {output_path}")


if __name__ == "__main__":
    zip_path = "src/ukr-eng-words.json.zip"
    output_path = "temp/0.convert-json.txt"

    # Ensure temp directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    convert_json_to_txt(zip_path, output_path)
