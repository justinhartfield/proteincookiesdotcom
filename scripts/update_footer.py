#!/usr/bin/env python3
"""
Script to update all HTML files with the new unified footer.
This replaces any existing footer with the new SEO-optimized footer.
"""

import os
import re
import glob

# The new unified footer HTML
NEW_FOOTER = '''    <!-- Footer -->
    <footer class="bg-slate-900 text-white pt-16 pb-8">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10 mb-12">
                <!-- Brand Column -->
                <div class="lg:col-span-1">
                    <a href="/" class="block mb-5"><img src="muff-the-protein-muffins-logo.png" alt="Protein Muffins" class="h-14"></a>
                    <p class="text-slate-400 text-sm leading-relaxed">
                        The ultimate destination for macro-verified protein muffin recipes. Every recipe is tested, measured in grams, and verified using USDA FoodData Central for accurate nutrition facts. Perfect for meal prep, post-workout snacks, and healthy breakfast options.
                    </p>
                </div>
                <!-- Popular Recipes -->
                <div>
                    <h4 class="anton-text text-lg mb-5 tracking-wide text-white">POPULAR RECIPES</h4>
                    <ul class="space-y-3 text-sm">
                        <li><a href="protein-banana-muffins.html" class="text-slate-400 hover:text-brand-500 transition">Protein Banana Muffins</a></li>
                        <li><a href="chocolate-protein-muffins.html" class="text-slate-400 hover:text-brand-500 transition">Chocolate Protein Muffins</a></li>
                        <li><a href="protein-blueberry-muffins.html" class="text-slate-400 hover:text-brand-500 transition">Blueberry Protein Muffins</a></li>
                        <li><a href="high-protein-muffins.html" class="text-slate-400 hover:text-brand-500 transition">High Protein Muffins (25g+)</a></li>
                        <li><a href="cottage-cheese-protein-muffins.html" class="text-slate-400 hover:text-brand-500 transition">Cottage Cheese Muffins</a></li>
                        <li><a href="protein-pumpkin-muffins.html" class="text-slate-400 hover:text-brand-500 transition">Pumpkin Protein Muffins</a></li>
                    </ul>
                </div>
                <!-- Popular Packs -->
                <div>
                    <h4 class="anton-text text-lg mb-5 tracking-wide text-white">RECIPE PACKS</h4>
                    <ul class="space-y-3 text-sm">
                        <li><a href="pack-starter.html" class="text-slate-400 hover:text-brand-500 transition">Starter Pack (Free)</a></li>
                        <li><a href="pack-30g-protein.html" class="text-slate-400 hover:text-brand-500 transition">30g+ Protein Pack</a></li>
                        <li><a href="pack-chocolate.html" class="text-slate-400 hover:text-brand-500 transition">Chocolate Lovers Pack</a></li>
                        <li><a href="pack-no-powder.html" class="text-slate-400 hover:text-brand-500 transition">No Protein Powder Pack</a></li>
                        <li><a href="pack-gluten-free.html" class="text-slate-400 hover:text-brand-500 transition">Gluten-Free Pack</a></li>
                        <li><a href="pack-vegan.html" class="text-slate-400 hover:text-brand-500 transition">Vegan Pack</a></li>
                    </ul>
                </div>
                <!-- Resources -->
                <div>
                    <h4 class="anton-text text-lg mb-5 tracking-wide text-white">RESOURCES</h4>
                    <ul class="space-y-3 text-sm">
                        <li><a href="pack-30g-protein.html" class="text-slate-400 hover:text-brand-500 transition">Macro Guide</a></li>
                        <li><a href="pack-starter.html" class="text-slate-400 hover:text-brand-500 transition">Starter Pack Guide</a></li>
                        <li><a href="high-protein-muffins-without-protein-powder.html" class="text-slate-400 hover:text-brand-500 transition">No Powder Guide</a></li>
                        <li><a href="recipe-packs.html" class="text-slate-400 hover:text-brand-500 transition">All Recipe Packs</a></li>
                        <li><a href="index.html#recipes" class="text-slate-400 hover:text-brand-500 transition">Browse All Recipes</a></li>
                    </ul>
                </div>
            </div>
            <!-- Bottom Bar -->
            <div class="border-t border-slate-800 pt-8 flex flex-col md:flex-row justify-between items-center gap-4">
                <p class="text-slate-500 text-xs font-medium">© 2026 ProteinMuffins.com. All rights reserved. Data by USDA FoodData Central.</p>
                <div class="flex items-center space-x-6 text-xs font-medium">
                    <a href="privacy.html" class="text-slate-500 hover:text-white transition">Privacy Policy</a>
                    <a href="terms.html" class="text-slate-500 hover:text-white transition">Terms of Use</a>
                    <a href="sitemap.html" class="text-slate-500 hover:text-white transition">Sitemap</a>
                </div>
            </div>
        </div>
    </footer>'''


def update_footer_in_file(filepath):
    """Update the footer in a single HTML file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip files that are not HTML content files (like the new privacy, terms, sitemap)
        if 'privacy.html' in filepath or 'terms.html' in filepath or 'sitemap.html' in filepath:
            print(f"Skipping {filepath} (new page)")
            return False
        
        # Pattern to match existing footer (various formats)
        # This pattern matches from <footer or <!-- Footer to </footer>
        patterns = [
            # Pattern 1: Standard footer with comment
            r'(\s*)<!-- Footer -->\s*<footer[^>]*>.*?</footer>',
            # Pattern 2: Footer without comment
            r'(\s*)<footer[^>]*class="bg-slate-900[^"]*"[^>]*>.*?</footer>',
            # Pattern 3: Any footer tag
            r'(\s*)<footer[^>]*>.*?</footer>',
            # Pattern 4: Main Footer comment variant
            r'(\s*)<!-- Main Footer -->\s*<footer[^>]*>.*?</footer>',
        ]
        
        original_content = content
        updated = False
        
        for pattern in patterns:
            match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
            if match:
                # Preserve the indentation from the original
                content = re.sub(pattern, NEW_FOOTER, content, count=1, flags=re.DOTALL | re.IGNORECASE)
                updated = True
                break
        
        if updated and content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Updated: {filepath}")
            return True
        else:
            # Check if file has a footer at all
            if '<footer' not in content.lower():
                print(f"⚠ No footer found: {filepath}")
            else:
                print(f"- No changes needed: {filepath}")
            return False
            
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")
        return False


def main():
    """Main function to update all HTML files."""
    # Get the project root directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    # Find all HTML files in the root directory (not in subdirectories like netlify/)
    html_files = glob.glob(os.path.join(project_root, '*.html'))
    
    print(f"\nFound {len(html_files)} HTML files to process\n")
    print("=" * 60)
    
    updated_count = 0
    for filepath in sorted(html_files):
        if update_footer_in_file(filepath):
            updated_count += 1
    
    print("=" * 60)
    print(f"\nCompleted! Updated {updated_count} of {len(html_files)} files.")


if __name__ == '__main__':
    main()

