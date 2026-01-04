#!/usr/bin/env python3
"""
Script to update navigation across all HTML pages to match the canonical navigation from index.html.
"""

import os
import re
from pathlib import Path

# Canonical navigation for internal pages (not index.html)
CANONICAL_DESKTOP_NAV = '''<nav class="hidden md:flex space-x-8 items-center">
                    <a href="index.html#recipes"
                        class="text-slate-600 hover:text-brand-600 font-semibold text-sm uppercase tracking-wider">Recipes</a>
                    <a href="recipe-packs.html"
                        class="text-slate-600 hover:text-brand-600 font-semibold text-sm uppercase tracking-wider">Recipe
                        Packs</a>
                    <a href="lead_magnet__clean_label_pack_opt_in.html"
                        class="text-slate-600 hover:text-brand-600 font-semibold text-sm uppercase tracking-wider">Macro
                        Guide</a>
                    <a href="pack-starter.html"
                        class="bg-brand-600 text-white px-5 py-2.5 rounded-full font-bold text-sm hover:bg-brand-900 transition shadow-lg shadow-brand-500/30">STARTER
                        PACK (FREE)</a>
                </nav>'''

CANONICAL_MOBILE_NAV = '''<!-- Mobile Menu Overlay -->
        <div x-show="mobileMenu" x-transition x-cloak
            class="md:hidden bg-white border-t border-slate-100 p-6 space-y-4 shadow-xl">
            <a href="index.html#recipes" class="block text-xl anton-text text-slate-900">RECIPES</a>
            <a href="recipe-packs.html" class="block text-xl anton-text text-slate-900">RECIPE PACKS</a>
            <a href="lead_magnet__clean_label_pack_opt_in.html" class="block text-xl anton-text text-slate-900">MACRO
                GUIDE</a>
            <a href="pack-starter.html"
                class="block text-center w-full bg-brand-600 text-white py-4 rounded-xl font-bold anton-text text-lg">GET
                STARTER PACK</a>
        </div>'''

# For index.html, use #recipes instead of index.html#recipes
INDEX_DESKTOP_NAV = '''<nav class="hidden md:flex space-x-8 items-center">
                    <a href="#recipes"
                        class="text-slate-600 hover:text-brand-600 font-semibold text-sm uppercase tracking-wider">Recipes</a>
                    <a href="recipe-packs.html"
                        class="text-slate-600 hover:text-brand-600 font-semibold text-sm uppercase tracking-wider">Recipe
                        Packs</a>
                    <a href="lead_magnet__clean_label_pack_opt_in.html"
                        class="text-slate-600 hover:text-brand-600 font-semibold text-sm uppercase tracking-wider">Macro
                        Guide</a>
                    <a href="pack-starter.html"
                        class="bg-brand-600 text-white px-5 py-2.5 rounded-full font-bold text-sm hover:bg-brand-900 transition shadow-lg shadow-brand-500/30">STARTER
                        PACK (FREE)</a>
                </nav>'''

INDEX_MOBILE_NAV = '''<!-- Mobile Menu Overlay -->
        <div x-show="mobileMenu" x-transition x-cloak
            class="md:hidden bg-white border-t border-slate-100 p-6 space-y-4 shadow-xl">
            <a href="#recipes" class="block text-xl anton-text text-slate-900">RECIPES</a>
            <a href="recipe-packs.html" class="block text-xl anton-text text-slate-900">RECIPE PACKS</a>
            <a href="lead_magnet__clean_label_pack_opt_in.html" class="block text-xl anton-text text-slate-900">MACRO
                GUIDE</a>
            <a href="pack-starter.html"
                class="block text-center w-full bg-brand-600 text-white py-4 rounded-xl font-bold anton-text text-lg">GET
                STARTER PACK</a>
        </div>'''


def update_navigation(content, is_index=False):
    """Update the navigation in the HTML content."""
    
    desktop_nav = INDEX_DESKTOP_NAV if is_index else CANONICAL_DESKTOP_NAV
    mobile_nav = INDEX_MOBILE_NAV if is_index else CANONICAL_MOBILE_NAV
    
    # Pattern to match desktop nav - matches from <nav class="hidden md:flex to closing </nav>
    desktop_pattern = r'<nav class="hidden md:flex[^>]*>[\s\S]*?</nav>'
    
    # Update desktop nav
    if re.search(desktop_pattern, content):
        content = re.sub(desktop_pattern, desktop_nav, content, count=1)
    
    # Pattern to match mobile menu within header
    # Look for the mobile menu div after the header's mobile menu button
    # This pattern looks for the mobile menu div that's inside the header
    mobile_pattern = r'(</div>\s*</div>\s*)(<!-- Mobile Menu[^>]*>[\s\S]*?</div>|<div x-show="mobileMenu"[^>]*>[\s\S]*?</div>)(\s*</header>)'
    
    # First check if there's an existing mobile menu to replace
    if re.search(mobile_pattern, content):
        content = re.sub(mobile_pattern, r'\1' + mobile_nav + r'\3', content, count=1)
    else:
        # Try alternative pattern - mobile menu right before </header>
        alt_pattern = r'(<div x-show="mobileMenu"[^>]*>[\s\S]*?</div>)(\s*</header>)'
        if re.search(alt_pattern, content):
            content = re.sub(alt_pattern, mobile_nav + r'\2', content, count=1)
    
    return content


def process_file(filepath):
    """Process a single HTML file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        is_index = filepath.name == 'index.html'
        
        # Check if file has a header with navigation
        if '<header class="sticky' not in content:
            return False, "No sticky header found"
        
        if '<nav class="hidden md:flex' not in content:
            return False, "No desktop nav found"
        
        original_content = content
        content = update_navigation(content, is_index)
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, "Updated"
        else:
            return False, "No changes needed"
            
    except Exception as e:
        return False, str(e)


def main():
    """Main function to update all HTML files."""
    project_root = Path(__file__).parent.parent
    html_files = list(project_root.glob('*.html'))
    
    updated_count = 0
    skipped_count = 0
    error_count = 0
    
    print(f"Found {len(html_files)} HTML files to process\n")
    
    for filepath in sorted(html_files):
        success, message = process_file(filepath)
        
        if success:
            print(f"✅ {filepath.name}: {message}")
            updated_count += 1
        elif message == "No changes needed":
            print(f"⏭️  {filepath.name}: {message}")
            skipped_count += 1
        else:
            print(f"❌ {filepath.name}: {message}")
            error_count += 1
    
    print(f"\n{'='*50}")
    print(f"Summary:")
    print(f"  Updated: {updated_count}")
    print(f"  Skipped: {skipped_count}")
    print(f"  Errors:  {error_count}")


if __name__ == "__main__":
    main()
