#!/usr/bin/env python3
"""
Generate Recipe Pages for ProteinCookies.com - Light Theme
"""

import json

# Load recipes
with open('data/recipes.json', 'r') as f:
    data = json.load(f)
    recipes = data['recipes']

RECIPE_TEMPLATE = '''<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | ProteinCookies.com</title>
    
    <meta name="description" content="{description}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://proteincookies.com/{slug}.html">
    
    <meta property="og:type" content="article">
    <meta property="og:title" content="{title} | ProteinCookies.com">
    <meta property="og:description" content="{description}">
    <meta property="og:image" content="https://proteincookies.com/recipe_images/{image}">
    <meta property="og:url" content="https://proteincookies.com/{slug}.html">
    
    <meta name="theme-color" content="#f59e0b">
    <link rel="icon" type="image/png" href="/images/favicon.png">
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    
    <script src="https://cdn.tailwindcss.com"></script>
    
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org/",
      "@type": "Recipe",
      "name": "{title}",
      "description": "{description}",
      "image": "https://proteincookies.com/recipe_images/{image}",
      "author": {{"@type": "Organization", "name": "ProteinCookies.com"}},
      "prepTime": "PT{prepTime}M",
      "cookTime": "PT{cookTime}M",
      "totalTime": "PT{totalTime}M",
      "recipeYield": "{yield_amount}",
      "recipeCategory": "Cookies",
      "recipeCuisine": "American",
      "nutrition": {{
        "@type": "NutritionInformation",
        "calories": "{calories} calories",
        "proteinContent": "{protein}g",
        "carbohydrateContent": "{carbs}g",
        "fatContent": "{fat}g",
        "fiberContent": "{fiber}g",
        "sugarContent": "{sugar}g"
      }},
      "recipeIngredient": {ingredients_json},
      "recipeInstructions": {instructions_json}
    }}
    </script>
    
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        'anton': ['Anton', 'sans-serif'],
                        'sans': ['Inter', 'sans-serif'],
                    }},
                    colors: {{
                        brand: {{
                            50: '#fffbeb',
                            100: '#fef3c7',
                            500: '#f59e0b',
                            600: '#d97706',
                            900: '#451a03',
                        }},
                        accent: {{
                            500: '#10b981',
                        }}
                    }}
                }}
            }}
        }}
    </script>
    <style>
        .anton-text {{ font-family: 'Anton', sans-serif; letter-spacing: 0.05em; }}
        .glass-nav {{ background: rgba(255, 255, 255, 0.8); backdrop-filter: blur(12px); }}
    </style>
</head>

<body class="min-h-screen bg-slate-50 text-slate-900 font-sans">
    <!-- Navigation -->
    <nav class="glass-nav fixed top-0 left-0 right-0 z-50 border-b border-slate-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-20">
                <a href="/" class="flex items-center space-x-3">
                    <img src="images/logo.png" alt="ProteinCookies" class="h-12 w-12 rounded-xl shadow-lg">
                    <span class="anton-text text-2xl text-brand-600">PROTEINCOOKIES</span>
                </a>
                <div class="hidden md:flex items-center space-x-8">
                    <a href="/" class="text-slate-600 hover:text-brand-600 font-semibold text-sm uppercase tracking-wider">Recipes</a>
                    <a href="category-all.html" class="text-slate-600 hover:text-brand-600 font-semibold text-sm uppercase tracking-wider">Categories</a>
                    <a href="pack-starter.html" class="bg-brand-600 text-white px-5 py-2.5 rounded-full font-bold text-sm hover:bg-brand-900 transition">STARTER PACK</a>
                </div>
            </div>
        </div>
    </nav>

    <main class="pt-20">
        <!-- Breadcrumb -->
        <div class="bg-white border-b border-slate-200">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
                <nav class="flex text-sm text-slate-500">
                    <a href="/" class="hover:text-brand-600">Home</a>
                    <span class="mx-2">/</span>
                    <a href="category-{category_slug}.html" class="hover:text-brand-600">{category}</a>
                    <span class="mx-2">/</span>
                    <span class="text-slate-900">{title}</span>
                </nav>
            </div>
        </div>

        <!-- Recipe Header -->
        <section class="bg-white py-8 lg:py-12">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="grid lg:grid-cols-2 gap-8 lg:gap-12">
                    <!-- Image -->
                    <div class="relative">
                        <img src="recipe_images/{image}" alt="{title}" class="w-full rounded-2xl shadow-xl">
                        <span class="absolute top-4 left-4 bg-brand-600 text-white px-4 py-2 rounded-full font-bold text-lg shadow-lg">{protein}g PROTEIN</span>
                    </div>
                    
                    <!-- Info -->
                    <div>
                        <span class="inline-block px-3 py-1 bg-brand-100 text-brand-600 text-xs font-bold uppercase tracking-wider rounded-full mb-4">{category}</span>
                        <h1 class="anton-text text-4xl lg:text-5xl text-slate-900 mb-4">{title_upper}</h1>
                        <p class="text-slate-600 text-lg mb-8">{description}</p>
                        
                        <!-- Quick Stats -->
                        <div class="grid grid-cols-4 gap-4 mb-8">
                            <div class="text-center p-4 bg-slate-100 rounded-xl">
                                <div class="text-2xl font-bold text-brand-600">{protein}g</div>
                                <div class="text-xs text-slate-500 uppercase">Protein</div>
                            </div>
                            <div class="text-center p-4 bg-slate-100 rounded-xl">
                                <div class="text-2xl font-bold text-slate-900">{calories}</div>
                                <div class="text-xs text-slate-500 uppercase">Calories</div>
                            </div>
                            <div class="text-center p-4 bg-slate-100 rounded-xl">
                                <div class="text-2xl font-bold text-slate-900">{totalTime}m</div>
                                <div class="text-xs text-slate-500 uppercase">Total Time</div>
                            </div>
                            <div class="text-center p-4 bg-slate-100 rounded-xl">
                                <div class="text-2xl font-bold text-slate-900">{yield_short}</div>
                                <div class="text-xs text-slate-500 uppercase">Yield</div>
                            </div>
                        </div>
                        
                        <!-- Full Nutrition -->
                        <div class="bg-slate-100 rounded-xl p-6">
                            <h3 class="font-bold text-slate-900 mb-4">Nutrition per {servingSize}</h3>
                            <div class="grid grid-cols-3 gap-4 text-sm">
                                <div class="flex justify-between"><span class="text-slate-500">Carbs</span><span class="font-semibold">{carbs}g</span></div>
                                <div class="flex justify-between"><span class="text-slate-500">Fat</span><span class="font-semibold">{fat}g</span></div>
                                <div class="flex justify-between"><span class="text-slate-500">Fiber</span><span class="font-semibold">{fiber}g</span></div>
                                <div class="flex justify-between"><span class="text-slate-500">Sugar</span><span class="font-semibold">{sugar}g</span></div>
                                <div class="flex justify-between"><span class="text-slate-500">Difficulty</span><span class="font-semibold">{difficulty}</span></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Recipe Content -->
        <section class="py-12 bg-slate-50">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="grid lg:grid-cols-3 gap-8">
                    <!-- Ingredients -->
                    <div class="lg:col-span-1">
                        <div class="bg-white rounded-2xl p-6 shadow-md sticky top-28">
                            <h2 class="anton-text text-2xl text-slate-900 mb-6">INGREDIENTS</h2>
                            <ul class="space-y-3">
{ingredients_html}
                            </ul>
                        </div>
                    </div>
                    
                    <!-- Instructions -->
                    <div class="lg:col-span-2">
                        <div class="bg-white rounded-2xl p-6 lg:p-8 shadow-md">
                            <h2 class="anton-text text-2xl text-slate-900 mb-6">INSTRUCTIONS</h2>
                            <div class="space-y-6">
{instructions_html}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- CTA -->
        <section class="bg-brand-600 py-12">
            <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
                <h2 class="anton-text text-3xl text-white mb-4">WANT MORE RECIPES?</h2>
                <p class="text-brand-100 mb-6">Get the Starter Pack with 5 essential protein cookie recipes.</p>
                <a href="pack-starter.html" class="inline-flex items-center gap-2 bg-white text-brand-600 px-8 py-4 rounded-xl font-bold hover:bg-brand-50 transition">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path>
                    </svg>
                    DOWNLOAD FREE PDF
                </a>
            </div>
        </section>
    </main>

    <footer class="bg-slate-900 text-white py-8">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <p class="text-slate-400 text-sm">&copy; 2026 ProteinCookies.com. All rights reserved.</p>
            <p class="text-slate-500 text-xs mt-2">Nutrition data verified using USDA FoodData Central.</p>
        </div>
    </footer>
</body>
</html>
'''

def generate_recipe_page(recipe):
    """Generate a single recipe page"""
    
    # Build ingredients HTML
    ingredients_html = ""
    for ing in recipe['ingredients']:
        ingredients_html += f'                                <li class="flex items-start gap-3"><span class="w-2 h-2 bg-brand-500 rounded-full mt-2 flex-shrink-0"></span><span class="text-slate-700">{ing}</span></li>\n'
    
    # Build instructions HTML
    instructions_html = ""
    for i, step in enumerate(recipe['instructions'], 1):
        instructions_html += f'''                                <div class="flex gap-4">
                                    <div class="w-10 h-10 bg-brand-600 text-white rounded-full flex items-center justify-center font-bold flex-shrink-0">{i}</div>
                                    <div>
                                        <h3 class="font-bold text-slate-900 mb-1">{step['step']}</h3>
                                        <p class="text-slate-600">{step['text']}</p>
                                    </div>
                                </div>\n'''
    
    # Build JSON arrays for schema
    ingredients_json = json.dumps(recipe['ingredients'])
    instructions_json = json.dumps([{"@type": "HowToStep", "name": s['step'], "text": s['text']} for s in recipe['instructions']])
    
    # Extract yield number
    yield_short = recipe['yield'].split()[0]
    
    # Category slug
    category_slug = recipe['category'].lower().replace(' ', '-')
    
    # Generate HTML
    html = RECIPE_TEMPLATE.format(
        title=recipe['title'],
        title_upper=recipe['title'].upper(),
        slug=recipe['slug'],
        description=recipe['description'],
        image=recipe['image'],
        protein=recipe['protein'],
        calories=recipe['calories'],
        carbs=recipe['carbs'],
        fat=recipe['fat'],
        fiber=recipe['fiber'],
        sugar=recipe['sugar'],
        prepTime=recipe['prepTime'],
        cookTime=recipe['cookTime'],
        totalTime=recipe['totalTime'],
        yield_amount=recipe['yield'],
        yield_short=yield_short,
        servingSize=recipe['servingSize'],
        difficulty=recipe['difficulty'],
        category=recipe['category'],
        category_slug=category_slug,
        ingredients_html=ingredients_html,
        instructions_html=instructions_html,
        ingredients_json=ingredients_json,
        instructions_json=instructions_json
    )
    
    # Write file
    filename = f"{recipe['slug']}.html"
    with open(filename, 'w') as f:
        f.write(html)
    
    print(f"Generated: {filename}")
    return filename


if __name__ == '__main__':
    print("Generating Recipe Pages for ProteinCookies.com (Light Theme)\n")
    
    generated_files = []
    for recipe in recipes:
        filename = generate_recipe_page(recipe)
        generated_files.append(filename)
    
    print(f"\nTotal: {len(generated_files)} recipe pages generated")
