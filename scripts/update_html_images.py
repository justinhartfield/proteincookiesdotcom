#!/usr/bin/env python3
"""
HTML Image Optimization Script for ProteinMuffins.com
- Adds width and height attributes to img tags
- Adds loading="lazy" to below-the-fold images
- Adds descriptive alt text to images missing it
- Converts img tags to picture elements with WebP support
"""

import os
import re
from pathlib import Path

# Configuration
HTML_DIR = ".."
RECIPE_IMAGES_DIR = "../recipe_images"

# Image dimensions (all recipe images are 800x800 after optimization)
IMAGE_DIMENSIONS = {
    'recipe_images/': {'width': 800, 'height': 800},
    'muff-the-protein-muffins-logo': {'width': 350, 'height': 117},
}

# Alt text mappings for common images
ALT_TEXT_MAPPINGS = {
    'muff-the-protein-muffins-logo': 'ProteinMuffins.com Logo',
    'apple-cinnamon-protein-muffins': 'Apple cinnamon protein muffins with warm spices',
    'apple-spiced-protein-muffins': 'Spiced apple protein muffins',
    'banana-choc-protein-muffins': 'Banana chocolate protein muffins',
    'banana-nut-protein-muffins': 'Banana nut protein muffins with walnuts',
    'blueberry-protein-muffins': 'Fresh blueberry protein muffins',
    'breakfast-protein-muffins': 'Protein breakfast muffins for meal prep',
    'carrot-cake-protein-muffins': 'Carrot cake protein muffins with cream cheese flavor',
    'choc-chip-protein-muffins': 'Chocolate chip protein muffins',
    'chocolate-protein-muffins': 'Rich chocolate protein muffins',
    'cottage-cheese-protein-muffins': 'Cottage cheese protein muffins',
    'double-choc-protein-muffins': 'Double chocolate protein muffins',
    'gluten-free-protein-muffins': 'Gluten-free protein muffins',
    'greek-yogurt-protein-muffins': 'Greek yogurt protein muffins',
    'healthy-protein-protein-muffins': 'Healthy protein muffins',
    'high-fiber-protein-muffins': 'High fiber protein muffins',
    'high-protein-protein-muffins': 'High protein muffins with 25g protein',
    'kids-protein-muffins': 'Kid-friendly protein muffins',
    'lemon-blueberry-protein-muffins': 'Lemon blueberry protein muffins',
    'mini-muffins-protein-muffins': 'Mini protein muffins for snacking',
    'protein-banana-bread-protein-muffins': 'Protein banana bread muffins',
    'protein-pancake-protein-muffins': 'Protein pancake muffins made with Kodiak mix',
    'protein-protein-muffins': 'Classic protein muffins recipe',
    'protein-pumpkin-muffins': 'Pumpkin protein muffins',
    'protein-pumpkin-thumb': 'Pumpkin protein muffins thumbnail',
    'vegan-protein-muffins': 'Vegan protein muffins',
    'with-protein-powder-protein-muffins': 'Protein muffins made with protein powder',
    'without-powder-protein-muffins': 'Protein muffins without protein powder',
    'zucchini-protein-muffins': 'Zucchini protein muffins',
}

def get_image_name(src):
    """Extract the base image name from a src path."""
    # Remove path and extension
    name = os.path.basename(src)
    name = os.path.splitext(name)[0]
    return name

def get_alt_text(src):
    """Get appropriate alt text for an image."""
    name = get_image_name(src)
    if name in ALT_TEXT_MAPPINGS:
        return ALT_TEXT_MAPPINGS[name]
    # Generate from filename
    alt = name.replace('-', ' ').replace('_', ' ').title()
    return alt

def get_dimensions(src):
    """Get width and height for an image."""
    if 'recipe_images/' in src:
        return IMAGE_DIMENSIONS['recipe_images/']
    for key, dims in IMAGE_DIMENSIONS.items():
        if key in src:
            return dims
    return {'width': 800, 'height': 800}  # Default

def process_img_tag(match, is_above_fold=False):
    """Process a single img tag and enhance it."""
    full_tag = match.group(0)
    
    # Skip if it's a dynamic Alpine.js image (has :src)
    if ':src=' in full_tag:
        return full_tag
    
    # Extract src
    src_match = re.search(r'src=["\']([^"\']+)["\']', full_tag)
    if not src_match:
        return full_tag
    
    src = src_match.group(1)
    
    # Skip external images
    if src.startswith('http') and 'proteinmuffins.com' not in src:
        return full_tag
    
    # Get or generate alt text
    alt_match = re.search(r'alt=["\']([^"\']*)["\']', full_tag)
    if alt_match:
        alt_text = alt_match.group(1)
    else:
        alt_text = get_alt_text(src)
    
    # Get dimensions
    dims = get_dimensions(src)
    
    # Check if width/height already exist
    has_width = 'width=' in full_tag.lower()
    has_height = 'height=' in full_tag.lower()
    
    # Build new attributes
    new_attrs = []
    
    if not has_width:
        new_attrs.append(f'width="{dims["width"]}"')
    if not has_height:
        new_attrs.append(f'height="{dims["height"]}"')
    
    # Add loading="lazy" for below-fold images
    if not is_above_fold and 'loading=' not in full_tag.lower():
        new_attrs.append('loading="lazy"')
    
    # Add alt if missing
    if not alt_match:
        new_attrs.append(f'alt="{alt_text}"')
    
    # Insert new attributes before the closing >
    if new_attrs:
        # Find position to insert (before > or />)
        if full_tag.rstrip().endswith('/>'):
            insert_pos = full_tag.rfind('/>')
            new_tag = full_tag[:insert_pos] + ' ' + ' '.join(new_attrs) + ' ' + full_tag[insert_pos:]
        else:
            insert_pos = full_tag.rfind('>')
            new_tag = full_tag[:insert_pos] + ' ' + ' '.join(new_attrs) + full_tag[insert_pos:]
        return new_tag
    
    return full_tag

def convert_to_picture_element(img_tag, src):
    """Convert an img tag to a picture element with WebP support."""
    # Get the WebP source path
    webp_src = src.replace('.png', '.webp').replace('.jpg', '.webp').replace('.jpeg', '.webp')
    
    # Check if WebP version exists
    webp_path = os.path.join(HTML_DIR, webp_src.lstrip('/'))
    if not os.path.exists(webp_path):
        return img_tag
    
    # Create picture element
    picture = f'''<picture>
                <source srcset="{webp_src}" type="image/webp">
                {img_tag}
            </picture>'''
    
    return picture

def process_html_file(filepath):
    """Process a single HTML file."""
    print(f"Processing: {os.path.basename(filepath)}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Track if we're in the head/hero section (above fold)
    # Simple heuristic: first 2 img tags are above fold
    img_count = [0]
    
    def replace_img(match):
        img_count[0] += 1
        is_above_fold = img_count[0] <= 2
        return process_img_tag(match, is_above_fold)
    
    # Process all img tags
    content = re.sub(r'<img[^>]+>', replace_img, content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Updated {img_count[0]} img tags")
        return True
    else:
        print(f"  No changes needed")
        return False

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    html_dir = os.path.join(script_dir, HTML_DIR)
    
    print(f"Processing HTML files in: {html_dir}")
    print("=" * 60)
    
    updated_count = 0
    total_count = 0
    
    for filename in sorted(os.listdir(html_dir)):
        if filename.endswith('.html'):
            filepath = os.path.join(html_dir, filename)
            total_count += 1
            if process_html_file(filepath):
                updated_count += 1
    
    print("=" * 60)
    print(f"Total files processed: {total_count}")
    print(f"Files updated: {updated_count}")

if __name__ == "__main__":
    main()
