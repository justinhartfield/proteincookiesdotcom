// Script to update pack pages to match pack-30g-protein.html template
const fs = require('fs');
const path = require('path');

// Pack configurations with unique content
const packs = {
    'pack-blueberry.html': {
        title: 'Blueberry Protein Muffins Pack | Berry Recipes',
        description: 'The Blueberry Bundle: 4 berry protein muffin recipes including classic blueberry, lemon blueberry, and more.',
        pdf: 'guides/pack-blueberry.pdf',
        successPage: 'success__blueberry_pack_delivery.html',
        packName: 'Blueberry Pack',
        heroTitle: 'THE BLUEBERRY',
        heroSubtitle: 'BUNDLE',
        heroTagline: 'FLAVOR PACK',
        heroDescription: '4 berry variations. <span class="text-white font-bold">Fresh, frozen, or freeze-dried</span>—we\'ve got you covered.',
        accentColor: 'indigo',
        checklist: ['4 Tested Blueberry Recipes', 'Fresh vs Frozen Guide', '14-22g Protein Per Muffin'],
        pdfMockupTitle: 'BLUEBERRY BUNDLE',
        pdfMockupSubtitle: '4 Recipes + Berry Guide',
        pdfBadge: '4',
        pdfBadgeLabel: 'Recipes',
        features: [
            { icon: '🫐', title: '4 BERRY RECIPES', desc: 'Classic, lemon blueberry, yogurt berry, and no-powder—all packed with antioxidants and protein.' },
            { icon: 'check', title: 'BERRY TYPE GUIDE', desc: 'Fresh vs frozen vs freeze-dried—know which works best for each recipe.' },
            { icon: 'bolt', title: 'ANTI-SINK TIPS', desc: 'How to keep berries evenly distributed instead of sinking to the bottom.' }
        ],
        recipes: [
            { emoji: '🫐', name: 'CLASSIC', protein: '19g', desc: 'Fresh or frozen berries' },
            { emoji: '🍋🫐', name: 'LEMON BERRY', protein: '18g', desc: 'Bright, zesty flavor' },
            { emoji: '🥛🫐', name: 'YOGURT BERRY', protein: '22g', desc: 'Extra creamy texture' },
            { emoji: '💜🫐', name: 'NO POWDER', protein: '14g', desc: 'Whole food only' }
        ],
        guideTitle: 'FRESH VS FROZEN',
        guideCards: [
            { emoji: '🧊', title: 'FROZEN (Recommended)', desc: 'Cheaper, available year-round, less bleed into batter. Fold in frozen—don\'t thaw!' },
            { emoji: '🫐', title: 'FRESH', desc: 'Best in summer. Coat with 1 tsp flour before folding to prevent sinking.' }
        ],
        finalCta: 'BERRY GOOD 🫐',
        finalBgText: 'BERRY',
        image: 'recipe_images/blueberry-protein-muffins.png',
        mobileCta: 'GET BLUEBERRY BUNDLE'
    },
    'pack-chocolate.html': {
        title: 'Chocolate Protein Muffins Pack | Double Chocolate Recipes',
        description: 'The Chocolate Collection: chocolate base, double chocolate, and chocolate yogurt muffin recipes.',
        pdf: 'guides/pack-chocolate.pdf',
        successPage: 'success__chocolate_pack_delivery.html',
        packName: 'Chocolate Pack',
        heroTitle: 'THE CHOCOLATE',
        heroSubtitle: 'COLLECTION',
        heroTagline: 'INDULGENT PACK',
        heroDescription: 'Rich, decadent, high-protein. <span class="text-white font-bold">4 chocolate recipes</span> from classic to triple fudge.',
        accentColor: 'amber',
        checklist: ['4 Tested Chocolate Recipes', 'Cocoa Type Guide', '20-26g Protein Per Muffin'],
        pdfMockupTitle: 'CHOCOLATE PACK',
        pdfMockupSubtitle: '4 Recipes + Cocoa Guide',
        pdfBadge: '4',
        pdfBadgeLabel: 'Recipes',
        features: [
            { icon: '🍫', title: '4 CHOCOLATE RECIPES', desc: 'Classic, double choc, choc yogurt, and choc PB—satisfy your cravings with protein.' },
            { icon: 'check', title: 'COCOA TYPE GUIDE', desc: 'Dutch process vs natural vs cacao—know which works best for rich flavor.' },
            { icon: 'bolt', title: 'TEXTURE TIPS', desc: 'How to get fudgy vs cakey texture depending on your preference.' }
        ],
        recipes: [
            { emoji: '🍫', name: 'CLASSIC', protein: '20g', desc: 'Cocoa base recipe' },
            { emoji: '🍫🍫', name: 'DOUBLE CHOC', protein: '24g', desc: 'Cocoa + chocolate protein' },
            { emoji: '🥛🍫', name: 'CHOC YOGURT', protein: '22g', desc: 'Extra fudgy texture' },
            { emoji: '🍫🥜', name: 'CHOC PB', protein: '26g', desc: 'Peanut butter swirl' }
        ],
        guideTitle: 'COCOA MATTERS',
        guideCards: [
            { emoji: '🟤', title: 'DUTCH PROCESS', desc: 'Richer, darker, less bitter. Recommended for muffins.' },
            { emoji: '🍫', title: 'NATURAL', desc: 'More acidic, works with baking soda. Classic flavor.' },
            { emoji: '🌿', title: 'CACAO', desc: 'Raw, bitter. Add more sweetener if using.' }
        ],
        finalCta: 'CHOCOLATE HEAVEN 🍫',
        finalBgText: 'CHOCO',
        image: 'recipe_images/double-choc-protein-muffins.png',
        mobileCta: 'GET CHOCOLATE PACK'
    },
    'pack-pumpkin.html': {
        title: 'Pumpkin Protein Muffins Pack | Seasonal Recipes',
        description: 'The Pumpkin Spice Pack: 4 pumpkin protein muffin recipes perfect for fall.',
        pdf: 'guides/pack-pumpkin.pdf',
        successPage: 'success__pumpkin_pack_delivery.html',
        packName: 'Pumpkin Pack',
        heroTitle: 'PUMPKIN',
        heroSubtitle: 'SPICE PACK',
        heroTagline: 'SEASONAL FAVORITE',
        heroDescription: 'Fall\'s favorite flavor meets protein. <span class="text-white font-bold">4 variations</span> from classic to chocolate pumpkin.',
        accentColor: 'orange',
        checklist: ['4 Tested Pumpkin Recipes', 'Canned vs Fresh Guide', '20-22g Protein Per Muffin'],
        pdfMockupTitle: 'PUMPKIN PACK',
        pdfMockupSubtitle: '4 Recipes + Prep Guide',
        pdfBadge: '4',
        pdfBadgeLabel: 'Recipes',
        features: [
            { icon: '🎃', title: '4 PUMPKIN RECIPES', desc: 'Classic, spiced, choc pumpkin, and cream cheese—perfect for fall baking.' },
            { icon: 'check', title: 'PUMPKIN PREP GUIDE', desc: 'Canned vs fresh—know which works best and how to prep each.' },
            { icon: 'bolt', title: 'SPICE BLEND', desc: 'The perfect pumpkin spice ratio for maximum fall flavor.' }
        ],
        recipes: [
            { emoji: '🎃', name: 'CLASSIC', protein: '20g', desc: 'Pure pumpkin flavor' },
            { emoji: '🎃✨', name: 'SPICED', protein: '20g', desc: 'Cinnamon, nutmeg, ginger' },
            { emoji: '🍫🎃', name: 'CHOC PUMPKIN', protein: '22g', desc: 'Cocoa + pumpkin combo' },
            { emoji: '🧀🎃', name: 'CREAM CHEESE', protein: '21g', desc: 'With protein frosting' }
        ],
        guideTitle: 'CANNED VS FRESH',
        guideCards: [
            { emoji: '🥫', title: 'CANNED (Recommended)', desc: 'More consistent, less water. Use 100% pure pumpkin, NOT pie filling!' },
            { emoji: '🎃', title: 'FRESH', desc: 'Roast, puree, and strain excess water first. More work but tastes amazing.' }
        ],
        finalCta: 'IT\'S PUMPKIN SEASON 🎃',
        finalBgText: 'PUMPKIN',
        image: 'recipe_images/apple-spiced-protein-muffins.png',
        mobileCta: 'GET PUMPKIN PACK'
    },
    'pack-chocolate-chip.html': {
        title: 'Chocolate Chip Protein Muffins Pack | Classic Recipes',
        description: 'The Chocolate Chip Pack: 4 chocolate chip protein muffin recipes with perfect chip distribution.',
        pdf: 'guides/pack-chocolate-chip.pdf',
        successPage: 'success__chocolate_chip_pack_delivery.html',
        packName: 'Chocolate Chip Pack',
        heroTitle: 'CHOCOLATE CHIP',
        heroSubtitle: 'PACK',
        heroTagline: 'CLASSIC FAVORITE',
        heroDescription: 'The perfect chip-to-muffin ratio. <span class="text-white font-bold">4 chocolate chip variations</span> for every taste.',
        accentColor: 'amber',
        checklist: ['4 Tested Choc Chip Recipes', 'Chip Distribution Guide', '18-22g Protein Per Muffin'],
        pdfMockupTitle: 'CHOC CHIP PACK',
        pdfMockupSubtitle: '4 Recipes + Chip Guide',
        pdfBadge: '4',
        pdfBadgeLabel: 'Recipes',
        features: [
            { icon: '🍪', title: '4 CHOC CHIP RECIPES', desc: 'Classic, double chip, banana chip, and mini chip—all with perfect distribution.' },
            { icon: 'check', title: 'CHIP GUIDE', desc: 'Mini vs regular vs chunks—which works best for each recipe.' },
            { icon: 'bolt', title: 'MELT-PROOF TIPS', desc: 'How to keep chips intact and evenly distributed.' }
        ],
        recipes: [
            { emoji: '🍪', name: 'CLASSIC', protein: '19g', desc: 'Perfect chip ratio' },
            { emoji: '🍪🍪', name: 'DOUBLE CHIP', protein: '20g', desc: 'Extra chocolate chips' },
            { emoji: '🍌🍪', name: 'BANANA CHIP', protein: '19g', desc: 'Banana + chocolate combo' },
            { emoji: '✨🍪', name: 'MINI CHIP', protein: '18g', desc: 'Mini chips throughout' }
        ],
        guideTitle: 'CHIP SIZES',
        guideCards: [
            { emoji: '⚫', title: 'MINI CHIPS', desc: 'Best distribution, less sinking. Perfect for uniform texture.' },
            { emoji: '🍫', title: 'REGULAR CHIPS', desc: 'Classic size. Fold in gently to prevent breaking.' }
        ],
        finalCta: 'CHIP CHIP HOORAY 🍪',
        finalBgText: 'CHIPS',
        image: 'recipe_images/choc-chip-protein-muffins.png',
        mobileCta: 'GET CHOC CHIP PACK'
    },
    'pack-cottage-cheese.html': {
        title: 'Cottage Cheese Protein Muffins Pack | High Protein Recipes',
        description: 'The Cottage Cheese Pack: 4 ultra-high protein muffin recipes using cottage cheese as a protein base.',
        pdf: 'guides/pack-cottage-cheese.pdf',
        successPage: 'success__cottage_cheese_pack_delivery.html',
        packName: 'Cottage Cheese Pack',
        heroTitle: 'COTTAGE CHEESE',
        heroSubtitle: 'PACK',
        heroTagline: 'HIGH PROTEIN',
        heroDescription: 'The secret ingredient for ultra-high protein. <span class="text-white font-bold">4 cottage cheese recipes</span> with incredible texture.',
        accentColor: 'emerald',
        checklist: ['4 Tested Cottage Cheese Recipes', 'Blending Guide', '22-28g Protein Per Muffin'],
        pdfMockupTitle: 'COTTAGE PACK',
        pdfMockupSubtitle: '4 Recipes + Blending Guide',
        pdfBadge: '28g',
        pdfBadgeLabel: 'Protein',
        features: [
            { icon: '🧀', title: '4 COTTAGE RECIPES', desc: 'Classic, blueberry, banana, and savory—all with 22-28g protein per muffin.' },
            { icon: 'check', title: 'BLENDING GUIDE', desc: 'How to blend cottage cheese smooth for invisible texture.' },
            { icon: 'bolt', title: 'TEXTURE TIPS', desc: 'The secret to fluffy, not dense, cottage cheese muffins.' }
        ],
        recipes: [
            { emoji: '🧀', name: 'CLASSIC', protein: '24g', desc: 'Pure cottage cheese base' },
            { emoji: '🫐🧀', name: 'BLUEBERRY', protein: '25g', desc: 'Berry + cottage combo' },
            { emoji: '🍌🧀', name: 'BANANA', protein: '26g', desc: 'Banana + cottage combo' },
            { emoji: '🧀✨', name: 'ULTRA HIGH', protein: '28g', desc: 'Maximum protein density' }
        ],
        guideTitle: 'BLENDING MATTERS',
        guideCards: [
            { emoji: '🔄', title: 'BLEND SMOOTH', desc: 'Blend cottage cheese until completely smooth—no lumps. This is the secret to invisible texture.' },
            { emoji: '🧀', title: 'CHOOSE RIGHT', desc: 'Use full-fat or 2% for best texture. Fat-free can be gummy.' }
        ],
        finalCta: 'MAX PROTEIN 🧀',
        finalBgText: 'PROTEIN',
        image: 'recipe_images/cottage-cheese-protein-muffins.png',
        mobileCta: 'GET COTTAGE PACK'
    },
    'pack-greek-yogurt.html': {
        title: 'Greek Yogurt Protein Muffins Pack | Creamy Recipes',
        description: 'The Greek Yogurt Pack: 4 extra-moist protein muffin recipes using Greek yogurt as a base.',
        pdf: 'guides/pack-greek-yogurt.pdf',
        successPage: 'success__greek_yogurt_pack_delivery.html',
        packName: 'Greek Yogurt Pack',
        heroTitle: 'GREEK YOGURT',
        heroSubtitle: 'PACK',
        heroTagline: 'EXTRA MOIST',
        heroDescription: 'The secret to extra-moist muffins. <span class="text-white font-bold">4 Greek yogurt recipes</span> with incredible texture.',
        accentColor: 'sky',
        checklist: ['4 Tested Greek Yogurt Recipes', 'Yogurt Selection Guide', '20-24g Protein Per Muffin'],
        pdfMockupTitle: 'YOGURT PACK',
        pdfMockupSubtitle: '4 Recipes + Yogurt Guide',
        pdfBadge: '4',
        pdfBadgeLabel: 'Recipes',
        features: [
            { icon: '🥛', title: '4 YOGURT RECIPES', desc: 'Classic, berry, vanilla, and honey—all with extra-moist texture.' },
            { icon: 'check', title: 'YOGURT GUIDE', desc: 'Full-fat vs 0%—which works best for each recipe and why.' },
            { icon: 'bolt', title: 'MOISTURE TIPS', desc: 'How to get perfectly moist (not soggy) muffins every time.' }
        ],
        recipes: [
            { emoji: '🥛', name: 'CLASSIC', protein: '22g', desc: 'Pure yogurt base' },
            { emoji: '🫐🥛', name: 'BERRY', protein: '21g', desc: 'Berry + yogurt combo' },
            { emoji: '🍦🥛', name: 'VANILLA', protein: '20g', desc: 'Vanilla bean flavor' },
            { emoji: '🍯🥛', name: 'HONEY', protein: '21g', desc: 'Natural honey sweetness' }
        ],
        guideTitle: 'YOGURT SELECTION',
        guideCards: [
            { emoji: '🥛', title: 'FULL-FAT (Recommended)', desc: 'Best flavor and texture. More protein per serving too.' },
            { emoji: '💧', title: '0% FAT', desc: 'Lower calorie but can be tangier. Add a bit more sweetener.' }
        ],
        finalCta: 'YOGURT POWER 🥛',
        finalBgText: 'YOGURT',
        image: 'recipe_images/greek-yogurt-protein-muffins.png',
        mobileCta: 'GET YOGURT PACK'
    },
    'pack-veggie.html': {
        title: 'Veggie Protein Muffins Pack | Vegetable-Based Recipes',
        description: 'The Veggie Pack: 4 vegetable-based protein muffin recipes including zucchini, carrot, and more.',
        pdf: 'guides/pack-veggie.pdf',
        successPage: 'success__veggie_pack_delivery.html',
        packName: 'Veggie Pack',
        heroTitle: 'THE VEGGIE',
        heroSubtitle: 'PACK',
        heroTagline: 'HIDDEN VEGGIES',
        heroDescription: 'Sneak in your veggies! <span class="text-white font-bold">4 vegetable-based recipes</span> that taste like dessert.',
        accentColor: 'green',
        checklist: ['4 Tested Veggie Recipes', 'Veggie Prep Guide', '18-21g Protein Per Muffin'],
        pdfMockupTitle: 'VEGGIE PACK',
        pdfMockupSubtitle: '4 Recipes + Prep Guide',
        pdfBadge: '4',
        pdfBadgeLabel: 'Recipes',
        features: [
            { icon: '🥕', title: '4 VEGGIE RECIPES', desc: 'Zucchini, carrot cake, sweet potato, and spinach—veggies that taste like dessert.' },
            { icon: 'check', title: 'VEGGIE PREP GUIDE', desc: 'How to prep each vegetable for best muffin texture.' },
            { icon: 'bolt', title: 'MOISTURE TIPS', desc: 'How to squeeze excess water from zucchini and other veggies.' }
        ],
        recipes: [
            { emoji: '🥒', name: 'ZUCCHINI', protein: '19g', desc: 'Hidden veggie classic' },
            { emoji: '🥕', name: 'CARROT CAKE', protein: '20g', desc: 'Spiced carrot flavor' },
            { emoji: '🍠', name: 'SWEET POTATO', protein: '18g', desc: 'Natural sweetness' },
            { emoji: '🥬', name: 'SPINACH', protein: '21g', desc: 'Green power boost' }
        ],
        guideTitle: 'VEGGIE PREP',
        guideCards: [
            { emoji: '💧', title: 'SQUEEZE THE WATER', desc: 'Zucchini and spinach release water. Squeeze them dry before adding to batter.' },
            { emoji: '🥕', title: 'SHRED FINE', desc: 'Fine shreds disappear into the batter. Chunky pieces are detectable.' }
        ],
        finalCta: 'EAT YOUR VEGGIES 🥕',
        finalBgText: 'VEGGIE',
        image: 'recipe_images/zucchini-protein-muffins.png',
        mobileCta: 'GET VEGGIE PACK'
    }
};

// Template function
function generatePackPage(config) {
    const colorMap = {
        indigo: { bg: 'indigo-600', dark: 'indigo-900', light: 'indigo-400', accent: 'indigo-500', subtle: 'indigo-100', text: 'indigo-600' },
        amber: { bg: 'amber-900', dark: 'amber-950', light: 'amber-400', accent: 'amber-500', subtle: 'amber-100', text: 'amber-900' },
        orange: { bg: 'orange-600', dark: 'orange-900', light: 'orange-400', accent: 'orange-500', subtle: 'orange-100', text: 'orange-600' },
        emerald: { bg: 'emerald-600', dark: 'emerald-900', light: 'emerald-400', accent: 'emerald-500', subtle: 'emerald-100', text: 'emerald-600' },
        sky: { bg: 'sky-600', dark: 'sky-900', light: 'sky-400', accent: 'sky-500', subtle: 'sky-100', text: 'sky-600' },
        green: { bg: 'green-600', dark: 'green-900', light: 'green-400', accent: 'green-500', subtle: 'green-100', text: 'green-600' }
    };
    const c = colorMap[config.accentColor] || colorMap.indigo;

    const featureIcons = {
        check: `<svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>`,
        bolt: `<svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>`
    };

    return `<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${config.title}</title>
    <meta name="description" content="${config.description}">
    <link rel="alternate" type="application/pdf" href="${config.pdf}">
    <meta name="pdf-url" content="${config.pdf}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="js/email-signup.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: { 'anton': ['Anton', 'sans-serif'], 'sans': ['Inter', 'sans-serif'] },
                    colors: { brand: { 50: '#fffbeb', 100: '#fef3c7', 500: '#f59e0b', 600: '#d97706', 900: '#451a03' }, accent: { 500: '#10b981' } },
                    backgroundImage: { 'grid-white': "url(\\"data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32' width='32' height='32' fill='none' stroke='rgb(255 255 255 / 0.05)'%3e%3cpath d='M0 .5H31.5V32'/%3e%3c/svg%3e\\")" }
                }
            }
        }
    </script>
    <style>
        [x-cloak] { display: none !important }
        .glass-nav { background: rgba(255, 255, 255, 0.8); backdrop-filter: blur(12px) }
        .anton-text { font-family: 'Anton', sans-serif; letter-spacing: 0.05em }
        @keyframes float { 0%, 100% { transform: translateY(0) } 50% { transform: translateY(-10px) } }
        .animate-float { animation: float 3s ease-in-out infinite }
    </style>
</head>
<body class="min-h-screen flex flex-col bg-slate-50 text-slate-900 font-sans" x-data="{ mobileMenu: false }" data-pdf="${config.pdf}">
    <header class="sticky top-0 z-50 glass-nav border-b border-slate-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-20">
                <a href="/" class="flex items-center"><img src="muff-the-protein-muffins-logo.png" alt="Protein Muffins" class="h-12"></a>
                <nav class="hidden md:flex space-x-8 items-center">
                    <a href="index.html#recipes" class="text-slate-600 hover:text-brand-600 font-semibold text-sm uppercase tracking-wider">Recipes</a>
                    <a href="recipe-packs.html" class="text-slate-600 hover:text-brand-600 font-semibold text-sm uppercase tracking-wider">Recipe Packs</a>
                    <a href="/pack-30g-protein.html" class="text-slate-600 hover:text-brand-600 font-semibold text-sm uppercase tracking-wider">Macro Guide</a>
                    <a href="pack-starter.html" class="bg-brand-600 text-white px-5 py-2.5 rounded-full font-bold text-sm hover:bg-brand-900 transition shadow-lg shadow-brand-500/30">STARTER PACK (FREE)</a>
                </nav>
                <button @click="mobileMenu = !mobileMenu" class="md:hidden text-slate-900">
                    <svg class="h-8 w-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path></svg>
                </button>
            </div>
        </div>
        <div x-show="mobileMenu" x-transition x-cloak class="md:hidden bg-white border-t border-slate-100 p-6 space-y-4 shadow-xl">
            <a href="index.html#recipes" class="block text-xl anton-text text-slate-900">RECIPES</a>
            <a href="recipe-packs.html" class="block text-xl anton-text text-slate-900">RECIPE PACKS</a>
            <a href="pack-30g-protein.html" class="block text-xl anton-text text-${c.text}">${config.heroTitle}</a>
        </div>
    </header>
    <main class="flex-grow">
        <!-- Hero Section -->
        <section class="relative bg-slate-900 py-16 lg:py-28 overflow-hidden">
            <div class="absolute inset-0 bg-grid-white pointer-events-none"></div>
            <div class="absolute top-0 right-0 -translate-y-1/2 translate-x-1/2 w-[600px] h-[600px] bg-${c.accent}/20 rounded-full blur-[120px]"></div>
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
                <div class="flex flex-col lg:flex-row items-center gap-16">
                    <div class="w-full lg:w-1/2">
                        <span class="inline-block px-4 py-1 bg-${c.accent} text-white font-bold text-xs uppercase tracking-widest rounded-full mb-6">${config.heroTagline}</span>
                        <h1 class="anton-text text-5xl lg:text-8xl text-white leading-none mb-6 italic">${config.heroTitle} <br><span class="text-${c.light} underline decoration-accent-500">${config.heroSubtitle}</span></h1>
                        <p class="text-slate-300 text-lg lg:text-xl mb-8 max-w-xl leading-relaxed">${config.heroDescription}</p>
                        <div class="space-y-3 mb-10">
                            ${config.checklist.map(item => `<div class="flex items-center text-slate-200"><svg class="w-5 h-5 text-${c.light} mr-3" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path></svg><span class="font-medium uppercase tracking-tight text-sm">${item}</span></div>`).join('\n                            ')}
                        </div>
                        <div class="bg-white/5 backdrop-blur-md p-2 rounded-3xl border border-white/10 max-w-md" x-data="{ email: '', loading: false }">
                            <form @submit.prevent="loading = true; EmailSignup.submit(email, '${config.packName}', '${config.successPage}')" class="flex flex-col sm:flex-row gap-2">
                                <input type="email" x-model="email" required placeholder="Enter your best email..." class="flex-grow bg-white px-6 py-4 rounded-2xl outline-none focus:ring-2 focus:ring-${c.accent} text-slate-900 font-medium">
                                <button type="submit" :disabled="loading" class="bg-${c.bg} hover:bg-${c.dark} text-white px-8 py-4 rounded-2xl font-bold anton-text tracking-wider transition shadow-lg disabled:opacity-50">
                                    <span x-show="!loading">GET PACK</span><span x-show="loading">SENDING...</span>
                                </button>
                            </form>
                        </div>
                    </div>
                    <div class="w-full lg:w-1/2 flex justify-center relative">
                        <div class="relative w-72 h-96 lg:w-96 lg:h-[520px] bg-slate-800 rounded-3xl border-8 border-slate-700 shadow-2xl overflow-hidden animate-float">
                            <div class="absolute inset-0 bg-white p-6 flex flex-col">
                                <div class="bg-${c.bg} text-white p-4 -mx-6 -mt-6 mb-6">
                                    <h4 class="anton-text text-2xl leading-none">${config.pdfMockupTitle}</h4>
                                    <p class="text-[8px] opacity-70 uppercase tracking-widest">${config.pdfMockupSubtitle}</p>
                                </div>
                                <div class="space-y-4">
                                    <div class="h-4 w-3/4 bg-slate-100 rounded"></div>
                                    <div class="grid grid-cols-2 gap-2">
                                        <div class="h-20 bg-${c.subtle} rounded-lg flex items-center justify-center"><span class="text-[10px] font-bold text-${c.text}">${config.recipes[0]?.name || 'RECIPE 1'}</span></div>
                                        <div class="h-20 bg-${c.subtle} rounded-lg flex items-center justify-center"><span class="text-[10px] font-bold text-${c.text}">${config.recipes[1]?.name || 'RECIPE 2'}</span></div>
                                    </div>
                                    <div class="space-y-2"><div class="h-2 w-full bg-slate-50 rounded"></div><div class="h-2 w-full bg-slate-50 rounded"></div><div class="h-2 w-2/3 bg-slate-50 rounded"></div></div>
                                </div>
                            </div>
                        </div>
                        <div class="absolute -bottom-6 -right-6 lg:right-12 bg-white p-6 rounded-full shadow-2xl flex flex-col items-center justify-center border-4 border-${c.accent}">
                            <span class="anton-text text-4xl text-slate-900 leading-none">${config.pdfBadge}</span>
                            <span class="text-[10px] font-black uppercase text-${c.text} tracking-tighter">${config.pdfBadgeLabel}</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- What's Inside Grid -->
        <section class="py-20 bg-white">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center mb-16">
                    <h2 class="anton-text text-4xl lg:text-5xl text-slate-900 mb-4 uppercase">Everything Inside The Bundle</h2>
                    <p class="text-slate-500 max-w-2xl mx-auto text-lg font-medium">Macro-verified recipes with step-by-step instructions.</p>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                    ${config.features.map((f, i) => `<div class="bg-slate-50 rounded-[2rem] p-8 border border-slate-100 hover:border-${c.accent}/30 hover:shadow-xl transition duration-300">
                        <div class="w-14 h-14 bg-${i === 0 ? c.subtle : (i === 1 ? 'accent-500/10' : 'blue-500/10')} text-${i === 0 ? c.text : (i === 1 ? 'accent-500' : 'blue-500')} rounded-2xl flex items-center justify-center mb-6">
                            ${f.icon.length <= 3 ? `<span class="text-2xl">${f.icon}</span>` : featureIcons[f.icon]}
                        </div>
                        <h4 class="anton-text text-xl mb-3 tracking-tight">${f.title}</h4>
                        <p class="text-slate-500 leading-relaxed text-sm">${f.desc}</p>
                    </div>`).join('\n                    ')}
                </div>
            </div>
        </section>

        <!-- Recipe Grid -->
        <section class="py-24 bg-slate-50">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center mb-16">
                    <h2 class="anton-text text-4xl lg:text-6xl text-slate-900 mb-4 uppercase">ALL ${config.recipes.length} RECIPES</h2>
                </div>
                <div class="grid grid-cols-2 lg:grid-cols-4 gap-6">
                    ${config.recipes.map(r => `<div class="bg-white p-8 rounded-3xl text-center hover:shadow-xl transition border border-slate-100">
                        <span class="text-5xl block mb-4">${r.emoji}</span>
                        <h3 class="anton-text text-xl">${r.name}</h3>
                        <p class="text-${c.text} font-bold">${r.protein} protein</p>
                        <p class="text-slate-500 text-sm mt-2">${r.desc}</p>
                    </div>`).join('\n                    ')}
                </div>
            </div>
        </section>

        <!-- Guide Section -->
        <section class="py-24 bg-${c.bg} overflow-hidden relative">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
                <div class="text-center mb-16">
                    <h2 class="anton-text text-4xl lg:text-6xl text-white mb-4 uppercase">${config.guideTitle}</h2>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-${config.guideCards.length} gap-8">
                    ${config.guideCards.map(card => `<div class="bg-white/10 backdrop-blur p-8 rounded-3xl">
                        <span class="text-4xl block mb-4">${card.emoji}</span>
                        <h3 class="font-bold text-xl text-white mb-2">${card.title}</h3>
                        <p class="text-white/80 text-sm">${card.desc}</p>
                    </div>`).join('\n                    ')}
                </div>
            </div>
        </section>

        <!-- Final CTA -->
        <section class="py-24 bg-slate-900 overflow-hidden relative">
            <div class="absolute inset-0 opacity-10 flex items-center justify-center">
                <h2 class="anton-text text-[20vw] text-white select-none pointer-events-none">${config.finalBgText}</h2>
            </div>
            <div class="max-w-4xl mx-auto px-4 relative z-10 text-center">
                <h2 class="anton-text text-5xl lg:text-7xl text-white mb-8 italic">${config.finalCta}</h2>
                <div class="bg-${c.bg} p-8 rounded-[2.5rem] shadow-2xl" x-data="{ email: '', loading: false }">
                    <p class="text-white/90 text-lg mb-8 font-medium">Download the pack now. Includes all recipes and guides.</p>
                    <form @submit.prevent="loading = true; EmailSignup.submit(email, '${config.packName}', '${config.successPage}')" class="flex flex-col sm:flex-row gap-4">
                        <input type="email" x-model="email" required placeholder="Where should we send it?" class="flex-grow px-8 py-5 rounded-2xl bg-white text-slate-900 font-bold text-lg outline-none">
                        <button type="submit" :disabled="loading" class="bg-slate-900 hover:bg-slate-800 text-white px-10 py-5 rounded-2xl font-bold anton-text text-xl tracking-wider shadow-xl transition transform hover:scale-105 disabled:opacity-50">
                            <span x-show="!loading">FREE DOWNLOAD</span><span x-show="loading">SENDING...</span>
                        </button>
                    </form>
                </div>
            </div>
        </section>
    </main>

    <!-- Sticky Mobile CTA -->
    <div class="md:hidden sticky bottom-0 z-50 bg-white border-t border-${c.subtle} p-4 shadow-[0_-10px_30px_rgba(0,0,0,0.1)]">
        <button @click="window.scrollTo({top: 0, behavior: 'smooth'})" class="w-full bg-${c.bg} text-white py-4 rounded-2xl anton-text flex items-center justify-center space-x-3 text-lg">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
            <span>${config.mobileCta}</span>
        </button>
    </div>

    <!-- Footer -->
    <footer class="bg-slate-900 text-white pt-16 pb-8">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10 mb-12">
                <div class="lg:col-span-1">
                    <a href="/" class="block mb-5"><img src="muff-the-protein-muffins-logo.png" alt="Protein Muffins" class="h-14"></a>
                    <p class="text-slate-400 text-sm leading-relaxed">The ultimate destination for macro-verified protein muffin recipes.</p>
                </div>
                <div>
                    <h4 class="anton-text text-lg mb-5 tracking-wide text-white">POPULAR RECIPES</h4>
                    <ul class="space-y-3 text-sm">
                        <li><a href="protein-banana-muffins.html" class="text-slate-400 hover:text-brand-500 transition">Protein Banana Muffins</a></li>
                        <li><a href="chocolate-protein-muffins.html" class="text-slate-400 hover:text-brand-500 transition">Chocolate Protein Muffins</a></li>
                        <li><a href="protein-blueberry-muffins.html" class="text-slate-400 hover:text-brand-500 transition">Blueberry Protein Muffins</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="anton-text text-lg mb-5 tracking-wide text-white">RECIPE PACKS</h4>
                    <ul class="space-y-3 text-sm">
                        <li><a href="pack-starter.html" class="text-slate-400 hover:text-brand-500 transition">Starter Pack (Free)</a></li>
                        <li><a href="pack-30g-protein.html" class="text-slate-400 hover:text-brand-500 transition">30g+ Protein Pack</a></li>
                        <li><a href="pack-chocolate.html" class="text-slate-400 hover:text-brand-500 transition">Chocolate Lovers Pack</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="anton-text text-lg mb-5 tracking-wide text-white">RESOURCES</h4>
                    <ul class="space-y-3 text-sm">
                        <li><a href="pack-30g-protein.html" class="text-slate-400 hover:text-brand-500 transition">Macro Guide</a></li>
                        <li><a href="recipe-packs.html" class="text-slate-400 hover:text-brand-500 transition">All Recipe Packs</a></li>
                        <li><a href="index.html#recipes" class="text-slate-400 hover:text-brand-500 transition">Browse All Recipes</a></li>
                    </ul>
                </div>
            </div>
            <div class="border-t border-slate-800 pt-8 flex flex-col md:flex-row justify-between items-center gap-4">
                <p class="text-slate-500 text-xs font-medium">© 2026 ProteinMuffins.com. All rights reserved.</p>
                <div class="flex items-center space-x-6 text-xs font-medium">
                    <a href="privacy.html" class="text-slate-500 hover:text-white transition">Privacy Policy</a>
                    <a href="terms.html" class="text-slate-500 hover:text-white transition">Terms of Use</a>
                </div>
            </div>
        </div>
    </footer>
    <script defer src="js/pack-picker.js"></script>
</body>
</html>`;
}

// Generate all pack pages
Object.entries(packs).forEach(([filename, config]) => {
    const html = generatePackPage(config);
    const filepath = path.join(__dirname, '..', filename);
    fs.writeFileSync(filepath, html);
    console.log(`✅ Generated ${filename}`);
});

console.log('\n🎉 All pack pages updated!');
