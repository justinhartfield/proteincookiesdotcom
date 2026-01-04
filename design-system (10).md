This Design System documentation is reverse-engineered from the provided HTML for **ProteinMuffins.com**.

# Design System: ProteinMuffins.com (The Optimized Macro-Verified Hub)

## 1. Core Principles
*   **High-Performance Aesthetic**: A high-contrast, "Cyber-Fitness" vibe that emphasizes energy, precision, and optimization.
*   **Brutalist-Lite**: Uses heavy, aggressive typography (Anton) paired with neon accents to create a sense of urgency and strength.
*   **Glassmorphism**: Utilizes blurred overlays and subtle borders to create depth within a dark, monochromatic environment.
*   **Dark Mode First**: The interface is built on a near-black foundation to allow the "Volt" accent color to pop significantly.

## 2. Color Palette

### Primary Colors
| Name | Hex | Tailwind Class | Usage |
| :--- | :--- | :--- | :--- |
| **Volt** | `#D4FF00` | `bg-volt`, `text-volt` | Primary actions, branding, highlights, scrollbars. |
| **Deep** | `#0A0A0B` | `bg-deep` | Main application background. |

### Secondary & UI Colors
| Name | Hex | Tailwind Class | Usage |
| :--- | :--- | :--- | :--- |
| **Slate 800** | `#1E1E22` | `bg-slate800` | Card backgrounds, component surfaces. |
| **Cobalt** | `#2E5BFF` | `text-cobalt` | Secondary accents, links, or info states. |
| **White** | `#FFFFFF` | `text-white` | Primary body text and headings. |

### Effects
*   **Glow**: `box-shadow: 0 0 20px rgba(212, 255, 0, 0.15)` (Used for `volt` themed elements).
*   **Glass**: `rgba(30, 30, 34, 0.7)` with `12px` backdrop blur and `5%` white border.

## 3. Typography

### Font Families
*   **Display/Heading**: `Anton`, sans-serif. Used for high-impact branding and section titles.
*   **UI/Body**: `Inter`, sans-serif. Used for readability in data, descriptions, and navigation.

### Typographic Styles
*   **Hero/Impact**: Large `font-anton` with optional `.text-stroke` (transparent fill, volt outline).
*   **Body Text**: `font-sans` (Inter) with weights ranging from 300 (Light) to 800 (Extra Bold).
*   **Coloring**: Default text is `white`. Emphasis is handled via `text-volt`.

## 4. Spacing & Layout
*   **Container**: Standard Tailwind container logic (implied).
*   **Scrolling**: Smooth scrolling enabled (`scroll-smooth`).
*   **Scrollbar**: Custom ultra-thin (4px) scrollbar with a `volt` thumb and `deep` track.
*   **Grid/Flex**: Standard Tailwind utility patterns for layout.

## 5. Components

### Cards / Containers
*   **Muffin Card**: Uses a hover state that scales the internal image (`.muffin-img`) by 1.05x.
*   **Glass Container**: Uses the `.glass` class for a semi-transparent, blurred background effect.

### Interactive Elements
*   **Hover Effects**: Smooth transitions for scaling and color shifts.
*   **Navigation**: Likely utilizes the `.glass` effect for sticky positioning (implied by the "scroll-smooth" and "glass" definitions).

## 6. Iconography
*   **Style**: While not explicitly rendered in the snippet, the design language dictates the use of **Lucide** or similar thin-stroke, geometric icons to match the `Inter` typeface and the technical "Optimized" theme.

---

## Reference HTML

```html
<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ProteinMuffins.com | The Optimized Macro-Verified Hub</title>
    <!-- Google Fonts: Anton (Primary) and Inter (UI/Body) -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@300;400;600;800&display=swap" rel="stylesheet">
    
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Alpine.js CDN -->
    <script defer src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>

    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        volt: '#D4FF00',
                        deep: '#0A0A0B',
                        slate800: '#1E1E22',
                        cobalt: '#2E5BFF',
                    },
                    fontFamily: {
                        anton: ['Anton', 'sans-serif'],
                        sans: ['Inter', 'sans-serif'],
                    },
                    boxShadow: {
                        'glow': '0 0 20px rgba(212, 255, 0, 0.15)',
                    }
                }
            }
        }
    </script>
    <style>
        [x-cloak] { display: none !important; }
        .muffin-card:hover .muffin-img { transform: scale(1.05); }
        .glass { background: rgba(30, 30, 34, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.05); }
        .text-stroke { -webkit-text-stroke: 1px #D4FF00; color: transparent; }
        .custom-scrollbar::-webkit-scrollbar { width: 4px; }
        .custom-scrollbar::-webkit-scrollbar-track { background: #0A0A0B; }
        .custom-scrollbar::-webkit-scrollbar-thumb { background: #D4FF00; border-radius: 10px; }
    </style>
</head>
<body 
    class="bg-deep text-white font-sans min-h-screen custom-scrollbar">
```