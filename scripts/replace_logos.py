import os
import re

def replace_logos(directory):
    # Header Pattern: Matches the text logo link in the header
    # Looks for <a ...>Protein<span>Muffins</span></a> with various classes
    header_pattern = re.compile(
        r'<a href="[^"]*"\s+class="[^"]*anton-text[^"]*text-3xl[^"]*"\s*>\s*Protein\s*<span\s*class="[^"]*">\s*Muffins\s*</span>\s*</a>',
        re.IGNORECASE | re.DOTALL
    )
    
    # Footer Pattern: Matches the text logo link in the footer
    # Looks for <a ...>Protein<span>Muffins</span></a> often with text-4xl or text-2xl
    footer_pattern = re.compile(
        r'<a href="[^"]*"\s+class="[^"]*anton-text[^"]*text-[24]xl[^"]*"\s*>\s*Protein\s*<span\s*class="[^"]*">\s*Muffins\s*</span>\s*</a>',
        re.IGNORECASE | re.DOTALL
    )
    
    # Replacements
    header_replacement = '<a href="/" class="flex items-center"><img src="muff-the-protein-muffins-logo.png" alt="Protein Muffins" class="h-12"></a>'
    footer_replacement = '<a href="/" class="block mb-6"><img src="muff-the-protein-muffins-logo.png" alt="Protein Muffins" class="h-16"></a>'
    
    count = 0
    files_modified = 0

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content
                
                # Replace Header
                if header_pattern.search(new_content):
                    new_content = header_pattern.sub(header_replacement, new_content)
                
                # Replace Footer
                if footer_pattern.search(new_content):
                    new_content = footer_pattern.sub(footer_replacement, new_content)
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated: {file}")
                    files_modified += 1
                else:
                    # Fallback check for any missed ones (e.g. index.html specific classes if different)
                    # Let's try a broader regex if the specific ones fail, or just report.
                    pass

    print(f"Total files modified: {files_modified}")

if __name__ == "__main__":
    replace_logos("/Users/tang/Projects/proteinmuffins")
