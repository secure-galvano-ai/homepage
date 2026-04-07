"""Generate favicon, apple-touch-icon, and OG image from logo."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).parent
logo = Image.open(ROOT / "logo.png")

# Favicon 32x32
img_32 = logo.resize((32, 32), Image.LANCZOS)
img_32.save(ROOT / "favicon.ico", format="ICO", sizes=[(32, 32)])

# Apple touch icon 180x180
img_180 = logo.resize((180, 180), Image.LANCZOS)
img_180.save(ROOT / "apple-touch-icon.png")

# OG image 1200x630: logo centered on dark blue background with text
og = Image.new("RGBA", (1200, 630), (27, 42, 74, 255))
logo_size = 160
logo_resized = logo.resize((logo_size, logo_size), Image.LANCZOS)
x = (1200 - logo_size) // 2
og.paste(logo_resized, (x, 160), logo_resized)

# Add text below logo
draw = ImageDraw.Draw(og)
try:
    font_large = ImageFont.truetype("arial.ttf", 36)
    font_small = ImageFont.truetype("arial.ttf", 20)
except OSError:
    font_large = ImageFont.load_default()
    font_small = ImageFont.load_default()

title = "secure galvano ai"
subtitle = "Sichere KI für Galvanik & Beschichtung"
draw.text((600, 370), title, fill=(255, 255, 255), font=font_large, anchor="mt")
draw.text((600, 420), subtitle, fill=(180, 190, 210), font=font_small, anchor="mt")

og_rgb = og.convert("RGB")
og_rgb.save(ROOT / "og-image.jpg", quality=90)

print("Generated: favicon.ico, apple-touch-icon.png, og-image.jpg")
