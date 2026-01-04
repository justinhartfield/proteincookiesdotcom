#!/usr/bin/env python3
"""
Generate Success/Download Pages for ProteinCookies.com - Light Theme
"""

# Define the packs with their details
PACKS = {
    'starter': {
        'title': 'STARTER PACK',
        'subtitle': '5 Essential Protein Cookie Recipes',
        'pdf': 'proteincookies-starter-pack.pdf',
        'recipes': [
            ('Chocolate Chip Protein Cookies', '21g protein per cookie'),
            ('Peanut Butter Protein Cookies', '24g protein per cookie'),
            ('No-Bake Protein Cookies', '18g protein per cookie'),
            ('Oatmeal Raisin Protein Cookies', '19g protein per cookie'),
            ('Double Chocolate Protein Cookies', '22g protein per cookie'),
        ]
    },
    'no-bake': {
        'title': 'NO-BAKE PACK',
        'subtitle': 'Quick Recipes Ready in 15 Minutes',
        'pdf': 'proteincookies-no-bake-pack.pdf',
        'recipes': [
            ('No-Bake Protein Cookies', '18g protein per cookie'),
            ('Protein Cookie Dough Bites', '15g protein per serving'),
            ('Peanut Butter Protein Cookies', '24g protein per cookie'),
        ]
    },
    'peanut-butter': {
        'title': 'PEANUT BUTTER LOVERS PACK',
        'subtitle': 'All the PB Recipes You Need',
        'pdf': 'proteincookies-peanut-butter-pack.pdf',
        'recipes': [
            ('Peanut Butter Protein Cookies', '24g protein per cookie'),
            ('Chocolate Peanut Butter Cookies', '23g protein per cookie'),
            ('No-Bake Protein Cookies', '18g protein per cookie'),
            ('Monster Protein Cookies', '20g protein per cookie'),
        ]
    },
    'holiday': {
        'title': 'HOLIDAY COOKIE PACK',
        'subtitle': 'Festive Protein Cookies for Every Celebration',
        'pdf': 'proteincookies-holiday-pack.pdf',
        'recipes': [
            ('Gingerbread Protein Cookies', '17g protein per cookie'),
            ('Snickerdoodle Protein Cookies', '20g protein per cookie'),
            ('Pumpkin Spice Protein Cookies', '18g protein per cookie'),
            ('Red Velvet Protein Cookies', '19g protein per cookie'),
            ('Sugar-Free Protein Cookies', '18g protein per cookie'),
        ]
    },
    'kids': {
        'title': 'KIDS LUNCHBOX PACK',
        'subtitle': 'Kid-Approved Protein Cookies',
        'pdf': 'proteincookies-kids-pack.pdf',
        'recipes': [
            ('Protein Cookies for Kids', '12g protein per cookie'),
            ('Birthday Cake Protein Cookies', '19g protein per cookie'),
            ('Chocolate Chip Protein Cookies', '21g protein per cookie'),
            ('Banana Oat Protein Cookies', '17g protein per cookie'),
        ]
    },
    'high-protein': {
        'title': '25g+ MUSCLE PACK',
        'subtitle': 'Maximum Protein Recipes for Serious Gains',
        'pdf': 'proteincookies-high-protein-pack.pdf',
        'recipes': [
            ('High Protein Cookies (30g)', '30g protein per cookie'),
            ('Peanut Butter Protein Cookies', '24g protein per cookie'),
            ('Cottage Cheese Protein Cookies', '23g protein per cookie'),
            ('Chocolate Peanut Butter Cookies', '23g protein per cookie'),
            ('Greek Yogurt Protein Cookies', '21g protein per cookie'),
        ]
    },
}

TEMPLATE = '''<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Download Your {title} | ProteinCookies.com</title>
    
    <meta name="description" content="Download your {title} with protein cookie recipes.">
    <meta name="robots" content="noindex, nofollow">
    
    <meta name="theme-color" content="#f59e0b">
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
        @keyframes checkmark {{
            0% {{ transform: scale(0); opacity: 0; }}
            50% {{ transform: scale(1.2); }}
            100% {{ transform: scale(1); opacity: 1; }}
        }}
        .animate-checkmark {{ animation: checkmark 0.5s ease-out forwards; }}
    </style>
</head>

<body class="min-h-screen bg-slate-50 text-slate-900 font-sans">
    <nav class="glass-nav fixed top-0 left-0 right-0 z-50 border-b border-slate-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-20">
                <a href="/" class="flex items-center space-x-3">
                    <img src="images/logo.png" alt="ProteinCookies" class="h-12 w-12 rounded-xl shadow-lg">
                    <span class="anton-text text-2xl text-brand-600">PROTEINCOOKIES</span>
                </a>
            </div>
        </div>
    </nav>

    <main class="pt-20">
        <section class="py-20">
            <div class="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
                <div class="mb-8">
                    <div class="w-24 h-24 bg-accent-500/20 rounded-full mx-auto flex items-center justify-center">
                        <svg class="w-12 h-12 text-accent-500 animate-checkmark" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path>
                        </svg>
                    </div>
                </div>
                
                <span class="inline-block px-4 py-1 bg-accent-500/20 text-accent-500 text-sm font-bold rounded-full mb-4">SUCCESS!</span>
                
                <h1 class="anton-text text-4xl lg:text-5xl text-slate-900 mb-4">YOUR {title_upper} IS READY</h1>
                
                <p class="text-slate-500 text-lg mb-8">{subtitle}</p>
                
                <a href="guides/{pdf}" download class="inline-flex items-center justify-center gap-3 bg-brand-600 text-white px-10 py-4 rounded-xl font-bold text-lg hover:bg-brand-700 transition shadow-lg shadow-brand-500/30 mb-8">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path>
                    </svg>
                    DOWNLOAD PDF
                </a>
                
                <div class="bg-white border border-slate-200 rounded-2xl p-8 text-left mt-12 shadow-md">
                    <h2 class="anton-text text-xl text-slate-900 mb-6">WHAT'S INSIDE YOUR PACK</h2>
                    
                    <div class="space-y-4">
{recipe_list}
                    </div>
                    
                    <div class="border-t border-slate-200 mt-6 pt-6">
                        <p class="text-slate-500 text-sm">Plus: Shopping list, nutrition facts, storage tips, and printable recipe cards!</p>
                    </div>
                </div>
                
                <div class="mt-12">
                    <p class="text-slate-500 mb-4">Want more recipes?</p>
                    <a href="/" class="text-brand-600 font-semibold hover:underline">Browse all 25+ recipes &rarr;</a>
                </div>
            </div>
        </section>
    </main>

    <footer class="bg-slate-900 text-white py-8">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <p class="text-slate-400 text-sm">&copy; 2026 ProteinCookies.com. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
'''

RECIPE_ITEM_TEMPLATE = '''                        <div class="flex items-start gap-3">
                            <div class="w-6 h-6 bg-brand-100 rounded-full flex items-center justify-center flex-shrink-0 mt-0.5">
                                <span class="text-brand-600 text-sm font-bold">{num}</span>
                            </div>
                            <div>
                                <p class="text-slate-900 font-semibold">{name}</p>
                                <p class="text-slate-500 text-sm">{protein}</p>
                            </div>
                        </div>'''

def generate_success_page(pack_key, pack_info):
    """Generate a success page for a single pack"""
    
    # Build recipe list HTML
    recipe_items = []
    for i, (name, protein) in enumerate(pack_info['recipes'], 1):
        item = RECIPE_ITEM_TEMPLATE.format(num=i, name=name, protein=protein)
        recipe_items.append(item)
    
    recipe_list = '\n'.join(recipe_items)
    
    # Generate page HTML
    html = TEMPLATE.format(
        title=pack_info['title'],
        title_upper=pack_info['title'],
        subtitle=pack_info['subtitle'],
        pdf=pack_info['pdf'],
        recipe_list=recipe_list
    )
    
    # Write file
    filename = f'success-{pack_key}.html'
    with open(filename, 'w') as f:
        f.write(html)
    
    print(f'Generated: {filename}')
    return filename


if __name__ == '__main__':
    print('Generating Success Pages for ProteinCookies.com (Light Theme)\n')
    
    generated_files = []
    for pack_key, pack_info in PACKS.items():
        filename = generate_success_page(pack_key, pack_info)
        generated_files.append(filename)
    
    print(f'\nTotal: {len(generated_files)} success pages generated')
