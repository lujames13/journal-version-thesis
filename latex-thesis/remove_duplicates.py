import re

def process_bibtex(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match each block starting with @ till the closing brace of that block
    # Simple regex for top-level braces matching
    entries = re.findall(r'@[a-zA-Z]+\{[^@]+', content)
    
    unique_keys = set()
    cleaned_entries = []
    
    for entry in entries:
        # Extract the cite key
        match = re.search(r'@[a-zA-Z]+\{([^,]+),', entry)
        if match:
            key = match.group(1).strip()
            if key not in unique_keys:
                unique_keys.add(key)
                cleaned_entries.append(entry)
                
    with open(filename, 'w', encoding='utf-8') as f:
        # Reconstruct the file 
        for i, entry in enumerate(cleaned_entries):
            # Ensuring spacing between entries
            f.write(entry.strip() + '\n\n')

process_bibtex('references.bib')
print("Deduplication complete.")
