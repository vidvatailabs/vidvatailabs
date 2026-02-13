# Logo Instructions

## Where to Place Your Logo

1. **Save your logo file** in this `images` folder
2. **Name it:** `logo.png` (or update the path in index.html if you use a different name)
3. **Recommended formats:** PNG, SVG, or JPG
4. **Recommended size:** 
   - Height: 40-50px for navigation (will auto-scale)
   - Transparent background preferred for best appearance

## Current Logo Path

The website is configured to look for: `images/logo.png`

If your logo has a different name or format, you'll need to update the `src` attribute in:
- Navigation bar (around line 535)
- Footer section (around line 704)

## Fallback

If the logo image is not found, the text "VidvatAI Labs" will automatically display instead.
