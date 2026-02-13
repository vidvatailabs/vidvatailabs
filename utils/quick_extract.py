#!/usr/bin/env python3
"""
Quick color extraction - tries multiple methods
"""
import sys
import subprocess
import os

# Try to install Pillow using pip3 directly
print("Attempting to install Pillow...")
try:
    result = subprocess.run([sys.executable, "-m", "pip", "install", "--user", "Pillow"], 
                          capture_output=True, text=True, timeout=60)
    if result.returncode == 0:
        print("Pillow installed successfully!")
    else:
        print(f"Installation attempt completed with code {result.returncode}")
        print("Trying alternative method...")
except Exception as e:
    print(f"Error: {e}")

# Now try to import and use
try:
    from PIL import Image
    import colorsys
    from collections import Counter
    
    print("\nExtracting colors from logo...")
    img = Image.open('images/logo.webp')
    
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    pixels = list(img.getdata())
    
    # Filter pixels
    filtered_pixels = []
    for r, g, b in pixels[::10]:  # Sample every 10th pixel
        brightness = (r + g + b) / 3
        if 30 < brightness < 240:
            filtered_pixels.append((r, g, b))
    
    if not filtered_pixels:
        filtered_pixels = pixels[::10]
    
    # Count colors
    color_counts = Counter(filtered_pixels)
    top_colors = color_counts.most_common(5)
    
    print("\n" + "="*60)
    print("COLORS EXTRACTED FROM LOGO")
    print("="*60)
    print("\nTop 5 colors:")
    for i, ((r, g, b), count) in enumerate(top_colors, 1):
        hex_color = f"#{r:02x}{g:02x}{b:02x}".upper()
        print(f"{i}. RGB({r:3d}, {g:3d}, {b:3d}) = {hex_color}")
    
    # Get primary color
    primary_r, primary_g, primary_b = top_colors[0][0]
    primary_hex = f"#{primary_r:02x}{primary_g:02x}{primary_b:02x}".upper()
    
    primary_dark_r = max(0, primary_r - 30)
    primary_dark_g = max(0, primary_g - 30)
    primary_dark_b = max(0, primary_b - 30)
    primary_dark_hex = f"#{primary_dark_r:02x}{primary_dark_g:02x}{primary_dark_b:02x}".upper()
    
    secondary = top_colors[1][0] if len(top_colors) > 1 else top_colors[0][0]
    secondary_hex = f"#{secondary[0]:02x}{secondary[1]:02x}{secondary[2]:02x}".upper()
    
    print("\n" + "="*60)
    print("SUGGESTED CSS VARIABLES:")
    print("="*60)
    css = f""":root {{
    --primary: {primary_hex};
    --primary-dark: {primary_dark_hex};
    --secondary: {secondary_hex};
}}"""
    print(css)
    
    # Save to file
    with open('extracted_colors.txt', 'w') as f:
        f.write("Extracted Colors:\n")
        f.write("="*60 + "\n")
        for i, ((r, g, b), count) in enumerate(top_colors, 1):
            hex_color = f"#{r:02x}{g:02x}{b:02x}".upper()
            f.write(f"{i}. RGB({r:3d}, {g:3d}, {b:3d}) = {hex_color}\n")
        f.write("\n" + "="*60 + "\n")
        f.write("CSS Variables:\n")
        f.write(css)
    
    print("\nColors saved to extracted_colors.txt")
    
except ImportError:
    print("\nPillow is not installed. Please run:")
    print("  pip3 install --user Pillow")
    print("or")
    print("  python3 -m pip install --user Pillow")
    sys.exit(1)
except Exception as e:
    print(f"\nError extracting colors: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
