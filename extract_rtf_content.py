import re

# Read the RTF file
with open(r'c:\Users\Anton\Documents\GitHub\Houdini-Code\Houdini FX notes.rtf', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Extract text between \loch\f31506 and other formatting markers
# This pattern captures actual text content
pattern = r'\\loch\\f31506\s+(.*?)(?=\\par|\\page|\\}|$)'
matches = re.findall(pattern, content, re.DOTALL)

# Also extract text with different font markers
pattern2 = r'\\dbch\\af43\\loch\\f31506\s+(.*?)(?=\\par|\\page|\\}|$)'
matches2 = re.findall(pattern2, content, re.DOTALL)

# Combine and clean
all_text = []
for match in matches + matches2:
    # Remove RTF formatting codes
    cleaned = re.sub(r'\\[a-z]+\d*\s*', ' ', match)
    cleaned = re.sub(r'[{}]', '', cleaned)
    cleaned = cleaned.strip()
    if cleaned and len(cleaned) > 2:
        all_text.append(cleaned)

# Write to output file
with open(r'c:\Users\Anton\Documents\GitHub\Houdini-Code\extracted_content.txt', 'w', encoding='utf-8') as f:
    for line in all_text:
        f.write(line + '\n')

print(f"Extracted {len(all_text)} text segments")
