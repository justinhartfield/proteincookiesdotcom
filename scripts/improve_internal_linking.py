#!/usr/bin/env python3
"""
Improve Internal Linking in Recipe Pages
Add contextual links to related recipes within the content
"""

import os
import re

# Configuration
HTML_DIR = ".."

# Internal linking opportunities - keywords to link and their targets
LINKING_RULES = {
    'protein-banana-muffins.html': [
        ('chocolate chip', 'chocolate-chip-protein-muffins.html', 'chocolate chip protein muffins'),
        ('blueberry', 'protein-blueberry-muffins.html', 'blueberry protein muffins'),
        ('pumpkin', 'protein-pumpkin-muffins.html', 'pumpkin protein muffins'),
    ],
    'chocolate-protein-muffins.html': [
        ('banana', 'protein-banana-muffins.html', 'banana protein muffins'),
        ('double chocolate', 'double-chocolate-protein-muffins.html', 'double chocolate protein muffins'),
        ('chocolate chip', 'chocolate-chip-protein-muffins.html', 'chocolate chip protein muffins'),
    ],
    'high-protein-muffins.html': [
        ('cottage cheese', 'cottage-cheese-protein-muffins.html', 'cottage cheese protein muffins'),
        ('Greek yogurt', 'high-protein-muffins-with-greek-yogurt.html', 'Greek yogurt protein muffins'),
        ('without protein powder', 'high-protein-muffins-without-protein-powder.html', 'high protein muffins without powder'),
    ],
    'protein-blueberry-muffins.html': [
        ('banana', 'protein-banana-muffins.html', 'banana protein muffins'),
        ('lemon', 'lemon-blueberry-protein-muffins.html', 'lemon blueberry protein muffins'),
        ('healthy', 'healthy-protein-muffins.html', 'healthy protein muffins'),
    ],
    'cottage-cheese-protein-muffins.html': [
        ('Greek yogurt', 'high-protein-muffins-with-greek-yogurt.html', 'Greek yogurt protein muffins'),
        ('without protein powder', 'high-protein-muffins-without-protein-powder.html', 'protein muffins without powder'),
        ('high protein', 'high-protein-muffins.html', 'high protein muffins'),
    ],
    'protein-pumpkin-muffins.html': [
        ('banana', 'protein-banana-muffins.html', 'banana protein muffins'),
        ('carrot cake', 'protein-carrot-cake-muffins.html', 'carrot cake protein muffins'),
        ('apple', 'apple-protein-muffins.html', 'apple protein muffins'),
    ],
    'healthy-protein-muffins.html': [
        ('low calorie', 'protein-mini-muffins.html', 'mini protein muffins'),
        ('Greek yogurt', 'high-protein-muffins-with-greek-yogurt.html', 'Greek yogurt protein muffins'),
        ('whole food', 'high-protein-muffins-without-protein-powder.html', 'whole food protein muffins'),
    ],
    'vegan-protein-muffins.html': [
        ('gluten-free', 'gluten-free-protein-muffins.html', 'gluten-free protein muffins'),
        ('banana', 'protein-banana-muffins.html', 'banana protein muffins'),
        ('chocolate', 'chocolate-protein-muffins.html', 'chocolate protein muffins'),
    ],
    'gluten-free-protein-muffins.html': [
        ('vegan', 'vegan-protein-muffins.html', 'vegan protein muffins'),
        ('healthy', 'healthy-protein-muffins.html', 'healthy protein muffins'),
        ('banana', 'protein-banana-muffins.html', 'banana protein muffins'),
    ],
    'protein-muffins-for-kids.html': [
        ('mini muffins', 'protein-mini-muffins.html', 'mini protein muffins'),
        ('banana', 'protein-banana-muffins.html', 'banana protein muffins'),
        ('chocolate chip', 'chocolate-chip-protein-muffins.html', 'chocolate chip protein muffins'),
    ],
}

def add_internal_link(content, keyword, target_url, link_text):
    """Add an internal link for a keyword if it exists and isn't already linked."""
    
    # Pattern to find the keyword not already in a link
    # Look for the keyword in paragraph text, not in attributes or existing links
    pattern = rf'(?<!["\'/])(?<![a-zA-Z])({re.escape(keyword)})(?![a-zA-Z])(?![^<]*>)(?![^<]*</a>)'
    
    # Check if this specific link already exists
    if f'href="{target_url}"' in content:
        return content, False
    
    # Find first occurrence in a paragraph or text content
    match = re.search(pattern, content, re.IGNORECASE)
    if match:
        original = match.group(1)
        replacement = f'<a href="{target_url}" class="text-brand-600 hover:text-brand-700 font-semibold">{original}</a>'
        # Only replace the first occurrence
        content = content[:match.start(1)] + replacement + content[match.end(1):]
        return content, True
    
    return content, False

def process_file(filepath, filename):
    """Process a single HTML file to add internal links."""
    print(f"Processing: {filename}")
    
    if filename not in LINKING_RULES:
        print(f"  No linking rules, skipping")
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    links_added = 0
    
    for keyword, target_url, link_text in LINKING_RULES[filename]:
        content, added = add_internal_link(content, keyword, target_url, link_text)
        if added:
            links_added += 1
            print(f"  Added link: '{keyword}' -> {target_url}")
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Total links added: {links_added}")
        return True
    else:
        print(f"  No new links added")
        return False

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    html_dir = os.path.join(script_dir, HTML_DIR)
    
    print(f"Improving internal linking in: {html_dir}")
    print("=" * 60)
    
    updated_count = 0
    
    for filename in LINKING_RULES.keys():
        filepath = os.path.join(html_dir, filename)
        if os.path.exists(filepath):
            if process_file(filepath, filename):
                updated_count += 1
    
    print("=" * 60)
    print(f"Files updated: {updated_count}")

if __name__ == "__main__":
    main()
