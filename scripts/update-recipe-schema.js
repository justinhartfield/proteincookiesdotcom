#!/usr/bin/env node
/**
 * Enhanced Recipe Schema Script for ProteinMuffins.com
 * Updates JSON-LD schema in recipe pages to include:
 * - recipeIngredient array
 * - recipeInstructions as HowToStep array
 * - recipeCuisine
 * - recipeCategory
 * - Absolute image URLs
 */

const fs = require('fs');
const path = require('path');

// Recipe configurations with ingredients and instructions for each recipe
const recipeConfigs = {
    'protein-banana-muffins.html': {
        name: 'Protein Banana Muffins',
        category: 'Breakfast',
        cuisine: 'American',
        ingredients: [
            '50g oat flour',
            '210g vanilla whey protein powder',
            '6g baking powder',
            '350g mashed ripe bananas (about 4 medium)',
            '300g nonfat Greek yogurt',
            '200g liquid egg whites'
        ]
    },
    'high-protein-muffins.html': {
        name: 'High Protein Muffins',
        category: 'Breakfast',
        cuisine: 'American',
        ingredients: [
            '50g oat flour',
            '120g vanilla whey protein powder',
            '6g baking powder',
            '300g mashed bananas',
            '200g nonfat Greek yogurt',
            '150g liquid egg whites'
        ]
    },
    'chocolate-protein-muffins.html': {
        name: 'Chocolate Protein Muffins',
        category: 'Dessert',
        cuisine: 'American',
        ingredients: [
            '60g oat flour',
            '180g chocolate whey protein powder',
            '30g unsweetened cocoa powder',
            '6g baking powder',
            '300g mashed bananas',
            '250g nonfat Greek yogurt',
            '150g liquid egg whites'
        ]
    },
    'protein-blueberry-muffins.html': {
        name: 'Protein Blueberry Muffins',
        category: 'Breakfast',
        cuisine: 'American',
        ingredients: [
            '60g oat flour',
            '180g vanilla whey protein powder',
            '6g baking powder',
            '300g mashed bananas',
            '250g nonfat Greek yogurt',
            '150g liquid egg whites',
            '150g fresh or frozen blueberries'
        ]
    },
    'cottage-cheese-protein-muffins.html': {
        name: 'Cottage Cheese Protein Muffins',
        category: 'Breakfast',
        cuisine: 'American',
        ingredients: [
            '80g oat flour',
            '120g vanilla whey protein powder',
            '6g baking powder',
            '300g mashed bananas',
            '400g low-fat cottage cheese',
            '100g liquid egg whites'
        ]
    },
    'gluten-free-protein-muffins.html': {
        name: 'Gluten-Free Protein Muffins',
        category: 'Breakfast',
        cuisine: 'American',
        ingredients: [
            '80g gluten-free 1-to-1 flour blend',
            '150g vanilla whey protein powder',
            '6g baking powder',
            '300g mashed bananas',
            '250g nonfat Greek yogurt',
            '150g liquid egg whites'
        ]
    },
    'vegan-protein-muffins.html': {
        name: 'Vegan Protein Muffins',
        category: 'Breakfast',
        cuisine: 'American',
        ingredients: [
            '100g oat flour',
            '120g pea protein powder',
            '6g baking powder',
            '300g mashed bananas',
            '250g coconut yogurt',
            '90g flax eggs (3 tbsp ground flax + 9 tbsp water)'
        ]
    }
};

// Default instructions for all recipes
const defaultInstructions = [
    {
        "@type": "HowToStep",
        "name": "Preheat and Prep",
        "text": "Preheat your oven to 375°F (190°C). Spray a 12-slot muffin tin with non-stick cooking spray or use silicone muffin cups."
    },
    {
        "@type": "HowToStep",
        "name": "Mix Dry Ingredients",
        "text": "In a large bowl, whisk together the flour, protein powder, and baking powder until well combined to prevent protein clumps."
    },
    {
        "@type": "HowToStep",
        "name": "Combine Wet Ingredients",
        "text": "In a separate bowl, mash the bananas until smooth. Add the yogurt and egg whites, stirring until uniform."
    },
    {
        "@type": "HowToStep",
        "name": "Fold and Bake",
        "text": "Gently fold the wet mixture into the dry ingredients—do not overmix. Fill muffin cups 3/4 full. Bake at 375°F for 5 minutes, then reduce to 350°F for 13-15 more minutes until a toothpick comes out clean."
    }
];

function updateRecipeSchema(filename) {
    const filepath = path.join(__dirname, '..', filename);

    if (!fs.existsSync(filepath)) {
        console.log(`⚠️  Skipped: ${filename} (not found)`);
        return;
    }

    let content = fs.readFileSync(filepath, 'utf8');

    // Check if already has recipeIngredient (already updated)
    if (content.includes('"recipeIngredient"')) {
        console.log(`⏭️  Skipped: ${filename} (already has recipeIngredient)`);
        return;
    }

    // Find and parse existing JSON-LD
    const jsonLdMatch = content.match(/<script type="application\/ld\+json">\s*(\{[\s\S]*?\})\s*<\/script>/);
    if (!jsonLdMatch) {
        console.log(`⚠️  Skipped: ${filename} (no JSON-LD found)`);
        return;
    }

    try {
        const schema = JSON.parse(jsonLdMatch[1]);

        // Get config or use defaults
        const config = recipeConfigs[filename] || {
            category: 'Breakfast',
            cuisine: 'American',
            ingredients: [
                '60g oat flour',
                '180g vanilla whey protein powder',
                '6g baking powder',
                '300g mashed bananas',
                '250g nonfat Greek yogurt',
                '150g liquid egg whites'
            ]
        };

        // Enhance the schema
        schema.image = [`https://proteinmuffins.com/${schema.image}`];
        schema.datePublished = '2026-01-01';
        schema.recipeCategory = config.category;
        schema.recipeCuisine = config.cuisine;
        schema.recipeIngredient = config.ingredients;
        schema.recipeInstructions = defaultInstructions;

        // Update author to Organization
        schema.author = {
            "@type": "Organization",
            "name": "ProteinMuffins.com",
            "url": "https://proteinmuffins.com"
        };

        // Enhance nutrition
        if (schema.nutrition) {
            schema.nutrition.servingSize = "1 muffin";
            if (schema.nutrition.calories) {
                schema.nutrition.calories = schema.nutrition.calories.replace(' calories', ' kcal');
            }
            schema.nutrition.fiberContent = schema.nutrition.fiberContent || "1g";
            schema.nutrition.sugarContent = schema.nutrition.sugarContent || "5g";
        }

        // Generate new JSON-LD
        const newJsonLd = JSON.stringify(schema, null, 6).replace(/^/gm, '    ').trim();
        const newScript = `<script type="application/ld+json">\n    ${newJsonLd}\n    </script>`;

        // Replace in content
        content = content.replace(/<script type="application\/ld\+json">[\s\S]*?<\/script>/, newScript);

        fs.writeFileSync(filepath, content, 'utf8');
        console.log(`✅ Updated: ${filename}`);

    } catch (e) {
        console.log(`❌ Error: ${filename} - ${e.message}`);
    }
}

// Get all recipe files
const recipeFiles = [
    'protein-banana-muffins.html',
    'high-protein-muffins.html',
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

console.log('🚀 Updating Recipe Schema for Rich Results...\n');

recipeFiles.forEach(updateRecipeSchema);

console.log('\n✨ Schema update complete!');
