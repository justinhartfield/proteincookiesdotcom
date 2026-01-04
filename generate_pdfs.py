#!/usr/bin/env python3
"""
Generate PDF Recipe Packs for ProteinCookies.com
"""

import json
from fpdf import FPDF
from datetime import datetime
import os

# Load recipes
with open('data/recipes.json', 'r') as f:
    data = json.load(f)
    recipes = data['recipes']

# Create a lookup by slug
recipe_lookup = {r['slug']: r for r in recipes}

# Define the packs
PACKS = {
    'starter': {
        'title': 'THE STARTER PACK',
        'subtitle': '5 Essential Protein Cookie Recipes',
        'description': 'Everything you need to start making delicious, macro-verified protein cookies at home.',
        'recipes': [
            'chocolate-chip-protein-cookies',
            'peanut-butter-protein-cookies', 
            'no-bake-protein-cookies',
            'double-chocolate-protein-cookies',
            'oatmeal-raisin-protein-cookies'
        ]
    },
    'no-bake': {
        'title': 'THE NO-BAKE PACK',
        'subtitle': 'Quick Recipes Ready in 15 Minutes',
        'description': 'No oven required! These quick and easy protein cookies are perfect for busy days.',
        'recipes': [
            'no-bake-protein-cookies',
            'protein-cookie-dough-bites',
            'peanut-butter-protein-cookies'
        ]
    },
    'peanut-butter': {
        'title': 'THE PEANUT BUTTER LOVERS PACK',
        'subtitle': 'All the PB Recipes You Need',
        'description': 'For the true peanut butter enthusiast. Rich, nutty, and packed with protein.',
        'recipes': [
            'peanut-butter-protein-cookies',
            'chocolate-peanut-butter-protein-cookies',
            'no-bake-protein-cookies',
            'monster-protein-cookies'
        ]
    },
    'holiday': {
        'title': 'THE HOLIDAY COOKIE PACK',
        'subtitle': 'Festive Protein Cookies for Every Celebration',
        'description': 'Healthy holiday treats that taste indulgent. Perfect for parties and gifts.',
        'recipes': [
            'gingerbread-protein-cookies',
            'snickerdoodle-protein-cookies',
            'pumpkin-spice-protein-cookies',
            'red-velvet-protein-cookies',
            'sugar-free-protein-cookies'
        ]
    },
    'kids': {
        'title': 'THE KIDS LUNCHBOX PACK',
        'subtitle': 'Kid-Approved Protein Cookies',
        'description': 'Healthy cookies kids will actually eat. Perfect for school lunches and snacks.',
        'recipes': [
            'protein-cookies-for-kids',
            'birthday-cake-protein-cookies',
            'chocolate-chip-protein-cookies',
            'peanut-butter-protein-cookies'
        ]
    },
    'high-protein': {
        'title': 'THE 25g+ MUSCLE PACK',
        'subtitle': 'Maximum Protein Recipes for Serious Gains',
        'description': 'Our highest protein recipes for athletes and fitness enthusiasts.',
        'recipes': [
            'high-protein-cookies-30g',
            'peanut-butter-protein-cookies',
            'cottage-cheese-protein-cookies',
            'chocolate-peanut-butter-protein-cookies',
            'greek-yogurt-protein-cookies'
        ]
    }
}

class CookiePDF(FPDF):
    def __init__(self, pack_name):
        super().__init__()
        self.pack_name = pack_name
        self.brand_color = (0, 212, 255)  # Cyan
        self.dark_bg = (10, 22, 40)
        
    def header(self):
        if self.page_no() > 1:
            self.set_fill_color(*self.dark_bg)
            self.rect(0, 0, 210, 15, 'F')
            self.set_font('Helvetica', 'B', 10)
            self.set_text_color(*self.brand_color)
            self.set_xy(10, 5)
            self.cell(0, 5, 'PROTEINCOOKIES.COM', 0, 0, 'L')
            self.set_text_color(150, 150, 150)
            self.cell(0, 5, self.pack_name.upper(), 0, 0, 'R')
            self.ln(15)
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', '', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def cover_page(self, pack_info):
        self.add_page()
        
        # Dark background
        self.set_fill_color(*self.dark_bg)
        self.rect(0, 0, 210, 297, 'F')
        
        # Brand name
        self.set_font('Helvetica', 'B', 24)
        self.set_text_color(*self.brand_color)
        self.set_xy(0, 40)
        self.cell(0, 10, 'PROTEINCOOKIES.COM', 0, 1, 'C')
        
        # Pack title
        self.set_font('Helvetica', 'B', 36)
        self.set_text_color(255, 255, 255)
        self.set_xy(0, 80)
        self.multi_cell(0, 15, pack_info['title'], 0, 'C')
        
        # Subtitle
        self.set_font('Helvetica', '', 16)
        self.set_text_color(*self.brand_color)
        self.set_xy(0, 130)
        self.cell(0, 10, pack_info['subtitle'], 0, 1, 'C')
        
        # Description
        self.set_font('Helvetica', '', 12)
        self.set_text_color(180, 180, 180)
        self.set_xy(30, 160)
        self.multi_cell(150, 6, pack_info['description'], 0, 'C')
        
        # Recipe count
        self.set_font('Helvetica', 'B', 48)
        self.set_text_color(*self.brand_color)
        self.set_xy(0, 200)
        self.cell(0, 20, str(len(pack_info['recipes'])), 0, 1, 'C')
        
        self.set_font('Helvetica', '', 14)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, 'MACRO-VERIFIED RECIPES', 0, 1, 'C')
        
        # Footer
        self.set_font('Helvetica', '', 10)
        self.set_text_color(100, 100, 100)
        self.set_xy(0, 270)
        self.cell(0, 5, f'Generated {datetime.now().strftime("%B %Y")}', 0, 1, 'C')
        self.cell(0, 5, 'proteincookies.com', 0, 1, 'C')

    def table_of_contents(self, pack_info):
        self.add_page()
        
        self.set_font('Helvetica', 'B', 24)
        self.set_text_color(30, 30, 30)
        self.cell(0, 15, 'WHATS INSIDE', 0, 1, 'L')
        
        self.ln(5)
        
        for i, slug in enumerate(pack_info['recipes'], 1):
            recipe = recipe_lookup.get(slug)
            if recipe:
                self.set_font('Helvetica', 'B', 14)
                self.set_text_color(30, 30, 30)
                self.cell(10, 10, f'{i}.', 0, 0)
                self.cell(0, 10, recipe['title'], 0, 1)
                
                self.set_font('Helvetica', '', 10)
                self.set_text_color(100, 100, 100)
                self.set_x(20)
                self.cell(0, 6, f"{recipe['protein']}g protein | {recipe['calories']} cal | {recipe['totalTime']} min", 0, 1)
                self.ln(3)
        
        self.ln(10)
        
        # What's included section
        self.set_font('Helvetica', 'B', 16)
        self.set_text_color(30, 30, 30)
        self.cell(0, 10, 'ALSO INCLUDED:', 0, 1)
        
        self.set_font('Helvetica', '', 11)
        self.set_text_color(60, 60, 60)
        items = [
            'Complete gram-based shopping list',
            'Nutrition facts for every recipe',
            'Storage and meal prep tips',
            'Printable recipe cards'
        ]
        for item in items:
            self.cell(5, 7, '', 0, 0)
            self.set_text_color(*self.brand_color)
            self.cell(5, 7, '>', 0, 0)  # Arrow
            self.set_text_color(60, 60, 60)
            self.cell(0, 7, f'  {item}', 0, 1)

    def recipe_page(self, recipe):
        self.add_page()
        
        # Recipe title
        self.set_font('Helvetica', 'B', 22)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 10, recipe['title'].upper(), 0, 'L')
        
        # Category tag
        self.set_font('Helvetica', 'B', 9)
        self.set_fill_color(*self.brand_color)
        self.set_text_color(10, 22, 40)
        self.cell(30, 6, f"  {recipe['category'].upper()}  ", 0, 0, 'C', True)
        self.ln(10)
        
        # Description
        self.set_font('Helvetica', '', 10)
        self.set_text_color(80, 80, 80)
        self.multi_cell(0, 5, recipe['description'], 0, 'L')
        self.ln(5)
        
        # Nutrition box
        self.set_fill_color(245, 245, 245)
        self.rect(10, self.get_y(), 190, 25, 'F')
        
        y_pos = self.get_y() + 3
        self.set_xy(15, y_pos)
        
        # Nutrition values
        nutrition = [
            ('PROTEIN', f"{recipe['protein']}g"),
            ('CALORIES', f"{recipe['calories']}"),
            ('CARBS', f"{recipe['carbs']}g"),
            ('FAT', f"{recipe['fat']}g"),
            ('FIBER', f"{recipe['fiber']}g")
        ]
        
        col_width = 36
        for label, value in nutrition:
            self.set_font('Helvetica', 'B', 14)
            self.set_text_color(*self.brand_color)
            self.cell(col_width, 8, value, 0, 0, 'C')
        
        self.set_xy(15, y_pos + 10)
        for label, value in nutrition:
            self.set_font('Helvetica', '', 7)
            self.set_text_color(100, 100, 100)
            self.cell(col_width, 5, label, 0, 0, 'C')
        
        self.ln(25)
        
        # Time and yield info
        self.set_font('Helvetica', '', 9)
        self.set_text_color(80, 80, 80)
        self.cell(0, 6, f"Time: {recipe['totalTime']} min  |  Yield: {recipe['yield']}  |  Difficulty: {recipe['difficulty']}", 0, 1, 'L')
        self.ln(5)
        
        # Two column layout
        col_width = 85
        left_margin = 10
        right_margin = 110
        
        # Ingredients column
        self.set_font('Helvetica', 'B', 12)
        self.set_text_color(30, 30, 30)
        self.set_x(left_margin)
        self.cell(col_width, 8, 'INGREDIENTS', 0, 1)
        
        self.set_font('Helvetica', '', 9)
        self.set_text_color(60, 60, 60)
        
        ingredients_y = self.get_y()
        for ing in recipe['ingredients']:
            self.set_x(left_margin)
            self.set_text_color(*self.brand_color)
            self.cell(3, 5, '-', 0, 0)  # Bullet
            self.set_text_color(60, 60, 60)
            self.cell(col_width - 3, 5, f' {ing}', 0, 1)
        
        # Instructions column
        self.set_xy(right_margin, ingredients_y - 8)
        self.set_font('Helvetica', 'B', 12)
        self.set_text_color(30, 30, 30)
        self.cell(col_width, 8, 'INSTRUCTIONS', 0, 1)
        
        self.set_font('Helvetica', '', 9)
        for i, step in enumerate(recipe['instructions'], 1):
            self.set_x(right_margin)
            self.set_font('Helvetica', 'B', 9)
            self.set_text_color(*self.brand_color)
            self.cell(6, 5, f'{i}.', 0, 0)
            self.set_font('Helvetica', 'B', 9)
            self.set_text_color(30, 30, 30)
            self.cell(col_width - 6, 5, step['step'], 0, 1)
            
            self.set_x(right_margin + 6)
            self.set_font('Helvetica', '', 8)
            self.set_text_color(80, 80, 80)
            self.multi_cell(col_width - 6, 4, step['text'], 0, 'L')
            self.ln(2)

    def shopping_list(self, pack_info):
        self.add_page()
        
        self.set_font('Helvetica', 'B', 24)
        self.set_text_color(30, 30, 30)
        self.cell(0, 15, 'SHOPPING LIST', 0, 1, 'L')
        
        self.set_font('Helvetica', '', 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 6, 'Combined ingredients for all recipes in this pack', 0, 1)
        self.ln(5)
        
        # Collect all ingredients
        all_ingredients = []
        for slug in pack_info['recipes']:
            recipe = recipe_lookup.get(slug)
            if recipe:
                all_ingredients.extend(recipe['ingredients'])
        
        # Categorize ingredients
        categories = {
            'Dry Goods': [],
            'Proteins & Dairy': [],
            'Nut Butters & Oils': [],
            'Sweeteners': [],
            'Extras': []
        }
        
        for ing in all_ingredients:
            ing_lower = ing.lower()
            if any(x in ing_lower for x in ['flour', 'oat', 'cocoa', 'baking', 'salt', 'cinnamon', 'cream of tartar']):
                categories['Dry Goods'].append(ing)
            elif any(x in ing_lower for x in ['protein', 'egg', 'yogurt', 'cheese', 'milk']):
                categories['Proteins & Dairy'].append(ing)
            elif any(x in ing_lower for x in ['butter', 'oil']):
                categories['Nut Butters & Oils'].append(ing)
            elif any(x in ing_lower for x in ['syrup', 'honey', 'sweetener', 'sugar']):
                categories['Sweeteners'].append(ing)
            else:
                categories['Extras'].append(ing)
        
        for cat_name, items in categories.items():
            if items:
                self.set_font('Helvetica', 'B', 11)
                self.set_text_color(30, 30, 30)
                self.cell(0, 8, cat_name.upper(), 0, 1)
                
                # Remove duplicates while preserving order
                seen = set()
                unique_items = []
                for item in items:
                    if item not in seen:
                        seen.add(item)
                        unique_items.append(item)
                
                self.set_font('Helvetica', '', 9)
                for item in unique_items:
                    self.set_text_color(150, 150, 150)
                    self.cell(5, 5, '[ ]', 0, 0)  # Checkbox
                    self.set_text_color(60, 60, 60)
                    self.cell(0, 5, f' {item}', 0, 1)
                self.ln(3)

    def tips_page(self):
        self.add_page()
        
        self.set_font('Helvetica', 'B', 24)
        self.set_text_color(30, 30, 30)
        self.cell(0, 15, 'PRO TIPS', 0, 1, 'L')
        self.ln(5)
        
        tips = [
            {
                'title': 'USE A KITCHEN SCALE',
                'text': 'All our recipes use gram measurements for precision. A kitchen scale ensures accurate macros every time.'
            },
            {
                'title': 'DONT OVERBAKE',
                'text': 'Protein cookies firm up significantly as they cool. Remove from oven when centers still look slightly underdone.'
            },
            {
                'title': 'PROTEIN POWDER MATTERS',
                'text': 'Different protein powders absorb liquid differently. If dough is too dry, add liquid 1 tbsp at a time.'
            },
            {
                'title': 'STORAGE TIPS',
                'text': 'Store in an airtight container at room temperature for 5 days, refrigerate for 2 weeks, or freeze for 3 months.'
            },
            {
                'title': 'MEAL PREP FRIENDLY',
                'text': 'Make a double batch on Sunday. Freeze individually wrapped cookies for grab-and-go protein throughout the week.'
            },
            {
                'title': 'CUSTOMIZE YOUR MACROS',
                'text': 'Swap chocolate chips for nuts, use different nut butters, or adjust sweetener to fit your goals.'
            }
        ]
        
        for tip in tips:
            self.set_fill_color(245, 245, 245)
            self.rect(10, self.get_y(), 190, 22, 'F')
            
            self.set_xy(15, self.get_y() + 3)
            self.set_font('Helvetica', 'B', 10)
            self.set_text_color(*self.brand_color)
            self.cell(0, 6, tip['title'], 0, 1)
            
            self.set_x(15)
            self.set_font('Helvetica', '', 9)
            self.set_text_color(60, 60, 60)
            self.multi_cell(180, 4, tip['text'], 0, 'L')
            self.ln(8)

    def final_page(self):
        self.add_page()
        
        # Dark background
        self.set_fill_color(*self.dark_bg)
        self.rect(0, 0, 210, 297, 'F')
        
        self.set_font('Helvetica', 'B', 28)
        self.set_text_color(255, 255, 255)
        self.set_xy(0, 80)
        self.cell(0, 15, 'WANT MORE RECIPES?', 0, 1, 'C')
        
        self.set_font('Helvetica', '', 12)
        self.set_text_color(180, 180, 180)
        self.set_xy(30, 110)
        self.multi_cell(150, 6, 'Visit ProteinCookies.com for 25+ macro-verified protein cookie recipes, more recipe packs, and weekly new recipes.', 0, 'C')
        
        self.set_font('Helvetica', 'B', 18)
        self.set_text_color(*self.brand_color)
        self.set_xy(0, 150)
        self.cell(0, 10, 'PROTEINCOOKIES.COM', 0, 1, 'C')
        
        self.set_font('Helvetica', '', 10)
        self.set_text_color(100, 100, 100)
        self.set_xy(0, 250)
        self.multi_cell(0, 5, 'All recipes are macro-verified using USDA FoodData Central.\nNutrition values are estimates and may vary based on specific ingredients used.', 0, 'C')


def generate_pack_pdf(pack_key, pack_info):
    """Generate a PDF for a single pack"""
    pdf = CookiePDF(pack_info['title'])
    pdf.set_auto_page_break(auto=True, margin=20)
    
    # Cover page
    pdf.cover_page(pack_info)
    
    # Table of contents
    pdf.table_of_contents(pack_info)
    
    # Recipe pages
    for slug in pack_info['recipes']:
        recipe = recipe_lookup.get(slug)
        if recipe:
            pdf.recipe_page(recipe)
    
    # Shopping list
    pdf.shopping_list(pack_info)
    
    # Tips page
    pdf.tips_page()
    
    # Final page
    pdf.final_page()
    
    # Save
    output_dir = 'guides'
    os.makedirs(output_dir, exist_ok=True)
    filename = f'{output_dir}/proteincookies-{pack_key}-pack.pdf'
    pdf.output(filename)
    print(f'Generated: {filename}')
    return filename


if __name__ == '__main__':
    print('Generating PDF Recipe Packs for ProteinCookies.com\n')
    
    generated_files = []
    for pack_key, pack_info in PACKS.items():
        filename = generate_pack_pdf(pack_key, pack_info)
        generated_files.append(filename)
    
    print(f'\nTotal: {len(generated_files)} PDF packs generated')
