#!/usr/bin/env python3
"""
Image Optimization Script v2 for ProteinMuffins.com
- Resizes images to max 800x800
- Uses pngquant for lossy PNG compression (much better results)
- Creates WebP versions for modern browsers
"""

import os
import subprocess
from PIL import Image

# Configuration
INPUT_DIR = "../recipe_images"
MAX_SIZE = 800  # Max width/height in pixels
WEBP_QUALITY = 85  # Quality for WebP (0-100)

def get_file_size(path):
    return os.path.getsize(path)

def optimize_image(input_path):
    """Optimize a single image: resize, compress PNG with pngquant, and create WebP version."""
    filename = os.path.basename(input_path)
    name, ext = os.path.splitext(filename)
    
    if ext.lower() != '.png':
        print(f"Skipping non-PNG file: {filename}")
        return None
    
    print(f"Processing: {filename}")
    
    original_size = get_file_size(input_path)
    
    # Open image and check dimensions
    img = Image.open(input_path)
    original_dims = img.size
    needs_resize = img.width > MAX_SIZE or img.height > MAX_SIZE
    
    # Resize if needed
    if needs_resize:
        img.thumbnail((MAX_SIZE, MAX_SIZE), Image.Resampling.LANCZOS)
        # Save resized version temporarily
        temp_path = input_path + ".temp.png"
        img.save(temp_path, 'PNG')
        os.replace(temp_path, input_path)
        print(f"  Resized: {original_dims} -> {img.size}")
    
    # Use pngquant for lossy compression (much better than PIL)
    try:
        subprocess.run([
            'pngquant', '--force', '--quality=65-80', '--speed=1',
            '--output', input_path, input_path
        ], check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        print(f"  Warning: pngquant failed, using optipng instead")
        subprocess.run(['optipng', '-o7', '-quiet', input_path], check=True)
    
    new_png_size = get_file_size(input_path)
    
    # Create WebP version using cwebp for best results
    webp_path = os.path.join(os.path.dirname(input_path), f"{name}.webp")
    subprocess.run([
        'cwebp', '-q', str(WEBP_QUALITY), '-m', '6',
        input_path, '-o', webp_path
    ], check=True, capture_output=True)
    
    webp_size = get_file_size(webp_path)
    
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
