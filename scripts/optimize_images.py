#!/usr/bin/env python3
"""
Image Optimization Script for ProteinMuffins.com
- Resizes images to max 800x800 (appropriate for recipe display)
- Compresses and converts to WebP format
- Keeps original PNG as fallback
"""

import os
from PIL import Image
import subprocess

# Configuration
INPUT_DIR = "../recipe_images"
MAX_SIZE = 800  # Max width/height in pixels
WEBP_QUALITY = 85  # Quality for WebP (0-100)
PNG_COMPRESS_LEVEL = 9  # Max PNG compression

def optimize_image(input_path):
    """Optimize a single image: resize, compress PNG, and create WebP version."""
    filename = os.path.basename(input_path)
    name, ext = os.path.splitext(filename)
    
    if ext.lower() != '.png':
        print(f"Skipping non-PNG file: {filename}")
        return
    
    print(f"Processing: {filename}")
    
    # Open image
    img = Image.open(input_path)
    original_size = os.path.getsize(input_path)
    original_dims = img.size
    
    # Convert to RGB if necessary (for WebP compatibility)
    if img.mode in ('RGBA', 'P'):
        # Create a white background for transparency
        background = Image.new('RGB', img.size, (255, 255, 255))
        if img.mode == 'P':
            img = img.convert('RGBA')
        background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
        img = background
    elif img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Resize if larger than MAX_SIZE
    if img.width > MAX_SIZE or img.height > MAX_SIZE:
        img.thumbnail((MAX_SIZE, MAX_SIZE), Image.Resampling.LANCZOS)
        print(f"  Resized: {original_dims} -> {img.size}")
    
    # Save optimized PNG (overwrite original)
    img.save(input_path, 'PNG', optimize=True, compress_level=PNG_COMPRESS_LEVEL)
    new_png_size = os.path.getsize(input_path)
    
    # Create WebP version
    webp_path = os.path.join(os.path.dirname(input_path), f"{name}.webp")
    img.save(webp_path, 'WEBP', quality=WEBP_QUALITY, method=6)
    webp_size = os.path.getsize(webp_path)
    
    # Report savings
    png_savings = (1 - new_png_size / original_size) * 100
    webp_savings = (1 - webp_size / original_size) * 100
    
    print(f"  Original: {original_size / 1024:.1f}KB")
    print(f"  PNG: {new_png_size / 1024:.1f}KB ({png_savings:.1f}% smaller)")
    print(f"  WebP: {webp_size / 1024:.1f}KB ({webp_savings:.1f}% smaller)")
    
    return {
        'filename': filename,
        'original_size': original_size,
        'png_size': new_png_size,
        'webp_size': webp_size,
        'original_dims': original_dims,
        'new_dims': img.size
    }

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(script_dir, INPUT_DIR)
    
    print(f"Optimizing images in: {input_dir}")
    print("=" * 60)
    
    results = []
    total_original = 0
    total_png = 0
    total_webp = 0
    
    for filename in sorted(os.listdir(input_dir)):
        if filename.lower().endswith('.png'):
            input_path = os.path.join(input_dir, filename)
            result = optimize_image(input_path)
            if result:
                results.append(result)
                total_original += result['original_size']
                total_png += result['png_size']
                total_webp += result['webp_size']
    
    print("=" * 60)
    print(f"Total images processed: {len(results)}")
    print(f"Total original size: {total_original / 1024 / 1024:.2f}MB")
    print(f"Total PNG size: {total_png / 1024 / 1024:.2f}MB ({(1 - total_png/total_original)*100:.1f}% smaller)")
    print(f"Total WebP size: {total_webp / 1024 / 1024:.2f}MB ({(1 - total_webp/total_original)*100:.1f}% smaller)")

if __name__ == "__main__":
    main()
