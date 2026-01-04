#!/usr/bin/env node
/**
 * SEO Enhancement Script for ProteinMuffins.com
 * Adds canonical URLs, Open Graph tags, Twitter cards, theme color, favicon, and performance hints
 * to all recipe HTML files.
 */

const fs = require('fs');
const path = require('path');

// Recipe files to process
const recipeFiles = [
    'high-protein-muffins.html',
    'protein-muffins-recipe.html',
    'protein-pumpkin-muffins.html',
    'protein-blueberry-muffins.html',
    'chocolate-protein-muffins.html',
    'healthy-protein-muffins.html',
    'double-chocolate-protein-muffins.html',
    'chocolate-chip-protein-muffins.html',
    'protein-powder-muffins.html',
    'high-protein-muffins-without-protein-powder.html',
    'high-protein-muffins-with-greek-yogurt.html',
    'cottage-cheese-protein-muffins.html',
    'gluten-free-protein-muffins.html',
    'vegan-protein-muffins.html',
    'protein-breakfast-muffins.html',
    'protein-muffins-for-kids.html',
    'protein-mini-muffins.html',
    'protein-pancake-muffins.html',
    'zucchini-protein-muffins.html',
    'banana-chocolate-chip-protein-muffins.html',
    'banana-nut-protein-muffins.html',
    'apple-protein-muffins.html',
    'lemon-blueberry-protein-muffins.html',
    'protein-carrot-cake-muffins.html',
];

// SEO template to insert after meta description
const getSeoTags = (filename, title, description, image) => {
    const url = `https://proteinmuffins.com/${filename}`;
    const ogImage = image ? `https://proteinmuffins.com/${image}` : 'https://proteinmuffins.com/muff-the-protein-muffins-logo.png';

    return `
    <!-- SEO -->
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="${url}">
    
    <!-- Open Graph -->
    <meta property="og:type" content="article">
    <meta property="og:site_name" content="ProteinMuffins.com">
    <meta property="og:title" content="${title}">
    <meta property="og:description" content="${description.substring(0, 150)}">
    <meta property="og:image" content="${ogImage}">
    <meta property="og:url" content="${url}">
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="${title}">
    <meta name="twitter:image" content="${ogImage}">
    
    <!-- Theme & Favicon -->
    <meta name="theme-color" content="#f59e0b">
    <link rel="icon" type="image/png" href="/muff-the-protein-muffins-logo.png">
    
    <!-- Performance -->
    <link rel="dns-prefetch" href="//cdn.tailwindcss.com">
    `;
};

function processFile(filename) {
    const filepath = path.join(__dirname, '..', filename);

    if (!fs.existsSync(filepath)) {
        console.log(`⚠️  Skipped: ${filename} (not found)`);
        return;
    }

    let content = fs.readFileSync(filepath, 'utf8');

    // Skip if already has canonical tag
    if (content.includes('rel="canonical"')) {
        console.log(`⏭️  Skipped: ${filename} (already has canonical)`);
        return;
    }

    // Extract title
    const titleMatch = content.match(/<title>([^<]+)<\/title>/);
    const title = titleMatch ? titleMatch[1].replace(' | ProteinMuffins.com', '') : filename;

    // Extract meta description
    const descMatch = content.match(/<meta name="description"[^>]*content="([^"]+)"/);
    const description = descMatch ? descMatch[1] : title;

    // Extract recipe image from JSON-LD
    const imageMatch = content.match(/"image":\s*"([^"]+)"/);
    const image = imageMatch ? imageMatch[1] : null;

    // Find insertion point (after meta description closing tag)
    const descEndPattern = /(<meta name="description"[^>]*>)/;
    const match = content.match(descEndPattern);

    if (match) {
        const seoTags = getSeoTags(filename, title, description, image);
        content = content.replace(descEndPattern, `$1${seoTags}`);

        fs.writeFileSync(filepath, content, 'utf8');
        console.log(`✅ Updated: ${filename}`);
    } else {
        console.log(`⚠️  Skipped: ${filename} (no meta description found)`);
    }
}

console.log('🚀 Starting SEO enhancement for recipe pages...\n');

recipeFiles.forEach(processFile);

console.log('\n✨ SEO enhancement complete!');
