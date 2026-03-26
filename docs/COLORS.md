# Color Palette - Resume Website

## Current Theme: Dark Purple Gradient

### Primary Gradients

**Background Gradient:**
```css
background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
```
- `#0f0c29` - Deep dark purple (almost black)
- `#302b63` - Medium dark purple
- `#24243e` - Dark purple blue

**Button Gradient:**
```css
background: linear-gradient(135deg, #434343 0%, #000000 100%);
```
- `#434343` - Dark grey
- `#000000` - Pure black

### Accent Colors

**Primary Accent (English button, links, headings):**
- `#8b7dff` - Light purple

**Secondary Accent (Russian button):**
- `#c77dff` - Light violet purple

**Text Colors:**
- `#333333` - Dark grey (main text on white)
- `#666666` - Medium grey (secondary text)
- `#FFFFFF` - White (text on dark backgrounds)

### Background Colors

**Content Sections:**
- `#FFFFFF` - White (main container)
- `#f8f9fa` - Light grey (cards, sections)

### Border Colors

**Borders & Accents:**
- `#8b7dff` - Purple accent (experience cards, social links)
- `#c77dff` - Light violet (alternative)

## Color Psychology

- **Dark Purple/Black** → Professional, sophisticated, tech-focused
- **Light Purple Accents** → Creative, modern, approachable
- **High Contrast** → Easy to read, accessibility-friendly

## Usage Examples

### Headings
```css
color: #8b7dff;
```

### Links (hover)
```css
background: #8b7dff;
color: white;
```

### Cards
```css
border-left: 4px solid #8b7dff;
background: #f8f9fa;
```

## Customization

To change the color scheme, edit these values in `scripts/build_site.py`:

1. **Background gradient** (line ~160)
2. **Header gradient** (line ~191)
3. **Button gradients** (lines ~248-258)
4. **Accent colors** - search for `#8b7dff` and `#c77dff`

## Alternative Color Schemes

### Option 1: Blue Theme
```css
/* Background */
background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);

/* Accent */
color: #00d4ff;
```

### Option 2: Green Theme
```css
/* Background */
background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);

/* Accent */
color: #00ff88;
```

### Option 3: Red Theme
```css
/* Background */
background: linear-gradient(135deg, #1a0000 0%, #330000 50%, #4d0000 100%);

/* Accent */
color: #ff4757;
```

## Accessibility

Current contrast ratios:
- White text on dark gradient: **WCAG AAA** ✅
- Dark text on white: **WCAG AAA** ✅
- Purple accent on white: **WCAG AA** ✅

## Quick Reference

| Element | Color | Hex Code |
|---------|-------|----------|
| Dark Purple (darkest) | █ | `#0f0c29` |
| Dark Purple (medium) | █ | `#302b63` |
| Dark Purple (lighter) | █ | `#24243e` |
| Black | █ | `#000000` |
| Dark Grey | █ | `#434343` |
| Purple Accent | █ | `#8b7dff` |
| Violet Accent | █ | `#c77dff` |
| Light Grey | █ | `#f8f9fa` |
| Text Grey | █ | `#666666` |
| White | █ | `#ffffff` |
