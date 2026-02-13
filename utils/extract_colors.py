#!/usr/bin/env python3
"""
Extract dominant colors from logo image
Run: python3 extract_colors.py
"""

try:
    from PIL import Image
    import colorsys
    from collections import Counter
except ImportError:
    print("Pillow not installed. Installing...")
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow", "--quiet"])
    from PIL import Image
    import colorsys
    from collections import Counter

# Open the image
img = Image.open('images/logo.webp')

# Convert to RGB if needed
if img.mode != 'RGB':
    img = img.convert('RGB')

# Get all pixels
pixels = list(img.getdata())

# Filter out very light/white and very dark/black pixels (likely background)
filtered_pixels = []
for r, g, b in pixels:
    brightness = (r + g + b) / 3
    # Keep pixels that aren't too light (white) or too dark (black)
    if 30 < brightness < 240:
        filtered_pixels.append((r, g, b))

if not filtered_pixels:
    # If filtering removed everything, use all pixels
    filtered_pixels = pixels

# Count color frequencies
color_counts = Counter(filtered_pixels)

# Get top 5 most common colors
top_colors = color_counts.most_common(5)

print("=" * 60)
print("COLORS EXTRACTED FROM LOGO")
print("=" * 60)
print("\nTop 5 most common colors:")
for i, ((r, g, b), count) in enumerate(top_colors, 1):
    hex_color = f"#{r:02x}{g:02x}{b:02x}".upper()
    print(f"{i}. RGB({r:3d}, {g:3d}, {b:3d}) = {hex_color}")

# Also get a vibrant primary color (highest saturation)
most_saturated = None
max_saturation = 0

sample_size = min(5000, len(filtered_pixels))
for r, g, b in filtered_pixels[:sample_size]:
    h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
    if s > max_saturation and v > 0.3 and v < 0.95:  # Not too dark or too light
        max_saturation = s
        most_saturated = (r, g, b)

if most_saturated:
    r, g, b = most_saturated
    hex_color = f"#{r:02x}{g:02x}{b:02x}".upper()
    print(f"\nMost saturated (primary) color: RGB({r:3d}, {g:3d}, {b:3d}) = {hex_color}")

# Get average color
if filtered_pixels:
    avg_r = sum(p[0] for p in filtered_pixels) // len(filtered_pixels)
    avg_g = sum(p[1] for p in filtered_pixels) // len(filtered_pixels)
    avg_b = sum(p[2] for p in filtered_pixels) // len(filtered_pixels)
    avg_hex = f"#{avg_r:02x}{avg_g:02x}{avg_b:02x}".upper()
    print(f"\nAverage color: RGB({avg_r:3d}, {avg_g:3d}, {avg_b:3d}) = {avg_hex}")

print("\n" + "=" * 60)
print("SUGGESTED COLOR SCHEME:")
print("=" * 60)
if top_colors:
    primary_r, primary_g, primary_b = top_colors[0][0]
    primary_hex = f"#{primary_r:02x}{primary_g:02x}{primary_b:02x}".upper()
    
    # Create darker version for primary-dark
    primary_dark_r = max(0, primary_r - 30)
    primary_dark_g = max(0, primary_g - 30)
    primary_dark_b = max(0, primary_b - 30)
    primary_dark_hex = f"#{primary_dark_r:02x}{primary_dark_g:02x}{primary_dark_b:02x}".upper()
    
    print(f"--primary: {primary_hex};")
    print(f"--primary-dark: {primary_dark_hex};")
    
    if len(top_colors) > 1:
        secondary_r, secondary_g, secondary_b = top_colors[1][0]
        secondary_hex = f"#{secondary_r:02x}{secondary_g:02x}{secondary_b:02x}".upper()
        print(f"--secondary: {secondary_hex};")
