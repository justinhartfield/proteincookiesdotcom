#!/usr/bin/env python3
"""
Add BreadcrumbList Schema to Recipe and Category Pages
"""

import os
import re
import json

# Configuration
HTML_DIR = ".."

# Breadcrumb mappings based on page type and category
CATEGORY_MAPPINGS = {
    'category-fruit.html': {'name': 'Fruit & Berry Muffins', 'position': 2},
    'category-dessert.html': {'name': 'Dessert Muffins', 'position': 2},
    'category-classic.html': {'name': 'Classic Muffins', 'position': 2},
    'category-whole-food.html': {'name': 'Whole Food Muffins', 'position': 2},
    'category-gluten-free.html': {'name': 'Gluten-Free Muffins', 'position': 2},
    'category-vegan.html': {'name': 'Vegan Muffins', 'position': 2},
    'category-savory.html': {'name': 'Savory Muffins', 'position': 2},
    'category-kids.html': {'name': 'Kids Muffins', 'position': 2},
    'category-low-cal.html': {'name': 'Low-Calorie Muffins', 'position': 2},
    'category-quick.html': {'name': 'Quick & Easy Muffins', 'position': 2},
    'category-high-protein.html': {'name': 'High Protein Muffins', 'position': 2},
}

# Recipe to category mappings
RECIPE_CATEGORIES = {
    'protein-banana-muffins.html': ('category-fruit.html', 'Fruit & Berry Muffins', 'Protein Banana Muffins'),
    'protein-blueberry-muffins.html': ('category-fruit.html', 'Fruit & Berry Muffins', 'Protein Blueberry Muffins'),
    'protein-pumpkin-muffins.html': ('category-fruit.html', 'Fruit & Berry Muffins', 'Protein Pumpkin Muffins'),
    'apple-protein-muffins.html': ('category-fruit.html', 'Fruit & Berry Muffins', 'Apple Protein Muffins'),
    'lemon-blueberry-protein-muffins.html': ('category-fruit.html', 'Fruit & Berry Muffins', 'Lemon Blueberry Protein Muffins'),
    'zucchini-protein-muffins.html': ('category-fruit.html', 'Fruit & Berry Muffins', 'Zucchini Protein Muffins'),
    'banana-chocolate-chip-protein-muffins.html': ('category-fruit.html', 'Fruit & Berry Muffins', 'Banana Chocolate Chip Protein Muffins'),
    'banana-nut-protein-muffins.html': ('category-fruit.html', 'Fruit & Berry Muffins', 'Banana Nut Protein Muffins'),
    'protein-carrot-cake-muffins.html': ('category-fruit.html', 'Fruit & Berry Muffins', 'Protein Carrot Cake Muffins'),
    
    'chocolate-protein-muffins.html': ('category-dessert.html', 'Dessert Muffins', 'Chocolate Protein Muffins'),
    'double-chocolate-protein-muffins.html': ('category-dessert.html', 'Dessert Muffins', 'Double Chocolate Protein Muffins'),
    'chocolate-chip-protein-muffins.html': ('category-dessert.html', 'Dessert Muffins', 'Chocolate Chip Protein Muffins'),
    
    'protein-muffins-recipe.html': ('category-classic.html', 'Classic Muffins', 'Protein Muffins Recipe'),
    'protein-powder-muffins.html': ('category-classic.html', 'Classic Muffins', 'Protein Powder Muffins'),
    'healthy-protein-muffins.html': ('category-classic.html', 'Classic Muffins', 'Healthy Protein Muffins'),
    
    'high-protein-muffins-without-protein-powder.html': ('category-whole-food.html', 'Whole Food Muffins', 'High Protein Muffins Without Powder'),
    'high-protein-muffins-with-greek-yogurt.html': ('category-whole-food.html', 'Whole Food Muffins', 'Greek Yogurt Protein Muffins'),
    'cottage-cheese-protein-muffins.html': ('category-whole-food.html', 'Whole Food Muffins', 'Cottage Cheese Protein Muffins'),
    
    'gluten-free-protein-muffins.html': ('category-gluten-free.html', 'Gluten-Free Muffins', 'Gluten-Free Protein Muffins'),
    'vegan-protein-muffins.html': ('category-vegan.html', 'Vegan Muffins', 'Vegan Protein Muffins'),
    'protein-breakfast-muffins.html': ('category-savory.html', 'Savory Muffins', 'Protein Breakfast Muffins'),
    'protein-muffins-for-kids.html': ('category-kids.html', 'Kids Muffins', 'Protein Muffins for Kids'),
    'protein-mini-muffins.html': ('category-low-cal.html', 'Low-Calorie Muffins', 'Protein Mini Muffins'),
    'protein-pancake-muffins.html': ('category-quick.html', 'Quick & Easy Muffins', 'Protein Pancake Muffins'),
    'high-protein-muffins.html': ('category-high-protein.html', 'High Protein Muffins', 'High Protein Muffins'),
    'high-fiber-protein-muffins.html': ('category-high-protein.html', 'High Protein Muffins', 'High Fiber Protein Muffins'),
}

def create_breadcrumb_schema(items):
    """Create BreadcrumbList schema JSON-LD."""
    schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": []
    }
    
    for i, item in enumerate(items, 1):
        element = {
            "@type": "ListItem",
            "position": i,
            "name": item['name']
        }
        if 'url' in item:
            element["item"] = item['url']
        schema["itemListElement"].append(element)
    
    return schema

def add_breadcrumb_to_file(filepath, filename):
    """Add breadcrumb schema to a file."""
    print(f"Processing: {filename}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip if already has BreadcrumbList
    if 'BreadcrumbList' in content:
        print(f"  Already has breadcrumb schema, skipping")
        return False
    
    # Determine breadcrumb structure
    breadcrumbs = [{'name': 'Home', 'url': 'https://proteinmuffins.com/'}]
    
    if filename in CATEGORY_MAPPINGS:
        # Category page
        cat_info = CATEGORY_MAPPINGS[filename]
        breadcrumbs.append({
            'name': cat_info['name'],
            'url': f'https://proteinmuffins.com/{filename}'
        })
    elif filename in RECIPE_CATEGORIES:
        # Recipe page
        cat_file, cat_name, recipe_name = RECIPE_CATEGORIES[filename]
        breadcrumbs.append({
            'name': cat_name,
            'url': f'https://proteinmuffins.com/{cat_file}'
        })
        breadcrumbs.append({
            'name': recipe_name
        })
    else:
        print(f"  No breadcrumb mapping found, skipping")
        return False
    
    # Create schema
    schema = create_breadcrumb_schema(breadcrumbs)
    schema_json = json.dumps(schema, indent=6)
    
    # Create script tag
    script_tag = f'''
    <!-- Breadcrumb Schema -->
    <script type="application/ld+json">
    {schema_json}
    </script>'''
    
    # Insert before </head>
    if '</head>' in content:
        content = content.replace('</head>', f'{script_tag}\n</head>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  Added breadcrumb schema")
        return True
    
    print(f"  Could not find </head> tag")
    return False

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    html_dir = os.path.join(script_dir, HTML_DIR)
    
    print(f"Adding breadcrumb schema to files in: {html_dir}")
    print("=" * 60)
    
    updated_count = 0
    
    # Process category pages
    for filename in CATEGORY_MAPPINGS.keys():
        filepath = os.path.join(html_dir, filename)
        if os.path.exists(filepath):
            if add_breadcrumb_to_file(filepath, filename):
                updated_count += 1
    
    # Process recipe pages
    for filename in RECIPE_CATEGORIES.keys():
        filepath = os.path.join(html_dir, filename)
        if os.path.exists(filepath):
            if add_breadcrumb_to_file(filepath, filename):
                updated_count += 1
    
    print("=" * 60)
    print(f"Files updated: {updated_count}")

if __name__ == "__main__":
    main()
