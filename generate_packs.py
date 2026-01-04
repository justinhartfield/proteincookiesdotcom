#!/usr/bin/env python3
"""Generate recipe pack pages for ProteinCookies.com."""

import json

# Load recipe data
with open('data/recipes.json', 'r') as f:
    data = json.load(f)

recipes = data['recipes']

# Define packs
packs = {
    'no-bake': {
        'name': 'No-Bake Pack',
        'tagline': 'Quick recipes ready in 15 minutes or less',
        'description': 'Perfect for busy days when you want protein cookies without heating up the oven. All recipes are ready in 15 minutes or less.',
        'recipes': ['no-bake-protein-cookies', 'protein-cookie-dough-bites'],
        'icon': 'clock'
    },
    'peanut-butter': {
        'name': 'Peanut Butter Lovers Pack',
        'tagline': 'For the true PB enthusiast',
        'description': 'If you love peanut butter, this pack is for you. Every recipe features the rich, nutty flavor of peanut butter.',
        'recipes': ['peanut-butter-protein-cookies', 'chocolate-peanut-butter-protein-cookies'],
        'icon': 'heart'
    },
    'holiday': {
        'name': 'Holiday Cookie Pack',
        'tagline': 'Festive protein cookies for every celebration',
        'description': 'Celebrate the holidays without sacrificing your macros. These festive recipes are perfect for parties and gifts.',
        'recipes': ['gingerbread-protein-cookies', 'snickerdoodle-protein-cookies', 'red-velvet-protein-cookies', 'birthday-cake-protein-cookies', 'pumpkin-spice-protein-cookies'],
        'icon': 'gift'
    },
    'kids': {
        'name': "Kids' Lunchbox Pack",
        'tagline': 'Kid-approved protein cookies',
        'description': 'Recipes your kids will actually eat. Perfect for school lunches, after-school snacks, and sports practice.',
        'recipes': ['protein-cookies-for-kids', 'birthday-cake-protein-cookies', 'chocolate-chip-protein-cookies'],
        'icon': 'smile'
    },
    'high-protein': {
        'name': '25g+ Muscle Pack',
        'tagline': 'Maximum protein for serious gains',
        'description': 'When you need maximum protein per cookie. Every recipe in this pack delivers 25g+ protein per serving.',
        'recipes': ['high-protein-cookies-30g', 'peanut-butter-protein-cookies', 'cottage-cheese-protein-cookies'],
        'icon': 'lightning'
    }
}

def get_pack_recipes(pack_slugs):
    return [r for r in recipes if r['slug'] in pack_slugs]

def get_icon_svg(icon):
    icons = {
        'clock': '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>',
        'heart': '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path>',
        'gift': '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v13m0-13V6a2 2 0 112 2h-2zm0 0V5.5A2.5 2.5 0 109.5 8H12zm-7 4h14M5 12a2 2 0 110-4h14a2 2 0 110 4M5 12v7a2 2 0 002 2h10a2 2 0 002-2v-7"></path>',
        'smile': '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>',
        'lightning': '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>'
    }
    return icons.get(icon, icons['lightning'])

def generate_pack_page(pack_slug, pack_info):
    pack_recipes = get_pack_recipes(pack_info['recipes'])
    
    recipes_list = '\n'.join([f'''
    <div class="flex items-center gap-3">
        <svg class="w-6 h-6 text-brand-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
        </svg>
        <span class="text-slate-300">{r['title']} ({r['protein']}g protein)</span>
    </div>''' for r in pack_recipes])
    
    recipes_grid = '\n'.join([f'''
    <a href="{r['slug']}.html" class="bg-brand-900/50 border border-brand-500/20 rounded-2xl overflow-hidden hover:border-brand-500/50 transition group">
        <div class="relative h-40 overflow-hidden">
            <img src="recipe_images/{r['image']}" alt="{r['title']}" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <div class="absolute top-3 right-3 bg-brand-500 text-brand-900 w-10 h-10 flex flex-col items-center justify-center rounded-lg">
                <span class="text-xs anton-text leading-none">{r['protein']}g</span>
            </div>
        </div>
        <div class="p-4">
            <h4 class="anton-text text-lg text-white group-hover:text-brand-500 transition">{r['title']}</h4>
            <p class="text-sm text-slate-400">{r['calories']} cal · {r['totalTime']}m</p>
        </div>
    </a>''' for r in pack_recipes])
    
    html = f'''<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{pack_info['name']} | ProteinCookies.com</title>
    
    <meta name="description" content="{pack_info['description']}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://proteincookies.com/pack-{pack_slug}.html">
    
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="ProteinCookies.com">
    <meta property="og:title" content="{pack_info['name']} | ProteinCookies.com">
    <meta property="og:description" content="{pack_info['description']}">
    
    <meta name="theme-color" content="#00D4FF">
    <link rel="icon" type="image/png" href="/images/favicon.png">
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    
    <script src="https://cdn.tailwindcss.com"></script>
    
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
                            50: '#e0faff',
                            100: '#b3f3ff',
                            500: '#00D4FF',
                            600: '#00b8e6',
                            900: '#0a1628',
                        }}
                    }}
                }}
            }}
        }}
    </script>
    <style>
        .anton-text {{ font-family: 'Anton', sans-serif; letter-spacing: 0.05em; }}
        .glass-nav {{ background: rgba(10, 22, 40, 0.9); backdrop-filter: blur(12px); }}
        .cyber-glow {{ box-shadow: 0 0 20px rgba(0, 212, 255, 0.3); }}
    </style>
</head>

<body class="min-h-screen bg-brand-900 text-white font-sans">
    <!-- Navigation -->
    <nav class="glass-nav fixed top-0 left-0 right-0 z-50 border-b border-brand-500/20">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-20">
                <a href="/" class="flex items-center space-x-3">
                    <img src="images/logo.png" alt="ProteinCookies" class="h-12 w-12 rounded-xl">
                    <span class="anton-text text-2xl text-brand-500">PROTEINCOOKIES</span>
                </a>
                <div class="hidden md:flex items-center space-x-8">
                    <a href="/#recipes" class="text-slate-300 hover:text-brand-500 transition font-medium">Recipes</a>
                    <a href="/#packs" class="text-brand-500 font-medium">Recipe Packs</a>
                    <a href="category-all.html" class="text-slate-300 hover:text-brand-500 transition font-medium">Categories</a>
                    <a href="pack-starter.html" class="bg-brand-500 text-brand-900 px-6 py-2.5 rounded-xl font-bold hover:bg-brand-600 transition cyber-glow">GET FREE PACK</a>
                </div>
            </div>
        </div>
    </nav>

    <main class="pt-20">
        <!-- Hero Section -->
        <section class="py-20 border-b border-brand-500/20">
            <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="grid lg:grid-cols-2 gap-12 items-center">
                    <div>
                        <div class="w-20 h-20 bg-brand-500/20 text-brand-500 rounded-2xl flex items-center justify-center mb-6">
                            <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                {get_icon_svg(pack_info['icon'])}
                            </svg>
                        </div>
                        <h1 class="anton-text text-4xl lg:text-6xl text-white mb-4">{pack_info['name'].upper()}</h1>
                        <p class="text-xl text-brand-500 mb-4">{pack_info['tagline']}</p>
                        <p class="text-lg text-slate-400 mb-8">{pack_info['description']}</p>
                        
                        <div class="space-y-3 mb-8">
                            {recipes_list}
                        </div>
                    </div>
                    
                    <!-- Email Signup Form -->
                    <div class="bg-brand-900/50 border border-brand-500/30 rounded-3xl p-8 lg:p-10">
                        <h2 class="anton-text text-2xl text-white mb-2">GET THIS PACK</h2>
                        <p class="text-slate-400 mb-6">Enter your email to download the PDF with all {len(pack_recipes)} recipes.</p>
                        
                        <form class="space-y-4" action="#" method="POST">
                            <div>
                                <label for="email" class="block text-sm font-medium text-slate-400 mb-2">Email Address</label>
                                <input type="email" id="email" name="email" required
                                    class="w-full bg-brand-900 border border-brand-500/30 rounded-xl px-4 py-4 text-white placeholder-slate-500 focus:outline-none focus:border-brand-500 transition"
                                    placeholder="your@email.com">
                            </div>
                            <button type="submit"
                                class="w-full bg-brand-500 text-brand-900 py-4 rounded-xl font-bold text-lg hover:bg-brand-600 transition cyber-glow flex items-center justify-center gap-2">
                                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path>
                                </svg>
                                DOWNLOAD PDF
                            </button>
                            <p class="text-xs text-slate-500 text-center">No spam. Unsubscribe anytime.</p>
                        </form>
                    </div>
                </div>
            </div>
        </section>

        <!-- Recipes in Pack -->
        <section class="py-20">
            <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
                <h2 class="anton-text text-3xl text-white text-center mb-12">RECIPES IN THIS PACK</h2>
                <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {recipes_grid}
                </div>
            </div>
        </section>

        <!-- Other Packs -->
        <section class="py-20 border-t border-brand-500/20">
            <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
                <h2 class="anton-text text-3xl text-white text-center mb-12">MORE RECIPE PACKS</h2>
                
                <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
                    <a href="pack-starter.html" class="bg-brand-900/50 border border-brand-500/20 rounded-2xl p-6 hover:border-brand-500/50 transition group">
                        <h3 class="anton-text text-lg text-white mb-2 group-hover:text-brand-500">STARTER PACK</h3>
                        <p class="text-sm text-slate-400">5 essential recipes to get started.</p>
                    </a>
                    <a href="pack-no-bake.html" class="bg-brand-900/50 border border-brand-500/20 rounded-2xl p-6 hover:border-brand-500/50 transition group">
                        <h3 class="anton-text text-lg text-white mb-2 group-hover:text-brand-500">NO-BAKE PACK</h3>
                        <p class="text-sm text-slate-400">Quick recipes in 15 minutes.</p>
                    </a>
                    <a href="pack-high-protein.html" class="bg-brand-900/50 border border-brand-500/20 rounded-2xl p-6 hover:border-brand-500/50 transition group">
                        <h3 class="anton-text text-lg text-white mb-2 group-hover:text-brand-500">25g+ MUSCLE PACK</h3>
                        <p class="text-sm text-slate-400">Maximum protein recipes.</p>
                    </a>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="bg-brand-900 border-t border-brand-500/20 pt-16 pb-8">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col md:flex-row justify-between items-center gap-4">
                <a href="/" class="flex items-center space-x-3">
                    <img src="images/logo.png" alt="ProteinCookies" class="h-10 w-10 rounded-xl">
                    <span class="anton-text text-lg text-brand-500">PROTEINCOOKIES</span>
                </a>
                <div class="flex items-center space-x-6 text-sm">
                    <a href="privacy.html" class="text-slate-500 hover:text-white transition">Privacy</a>
                    <a href="terms.html" class="text-slate-500 hover:text-white transition">Terms</a>
                    <a href="/" class="text-slate-500 hover:text-white transition">Home</a>
                </div>
            </div>
            <div class="mt-8 text-center">
                <p class="text-slate-500 text-xs">© 2026 ProteinCookies.com. All rights reserved.</p>
            </div>
        </div>
    </footer>
</body>
</html>'''
    
    return html

# Generate all pack pages
for slug, info in packs.items():
    filename = f"pack-{slug}.html"
    html = generate_pack_page(slug, info)
    with open(filename, 'w') as f:
        f.write(html)
    print(f"Generated: {filename}")

print(f"\nTotal: {len(packs)} pack pages generated")
