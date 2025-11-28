from PIL import Image, ImageDraw
import os
import random

def create_test_image(size):
    """
    Creates a test image with a gradient background and some shapes.
    This generates a more realistic, complex image for testing.
    """
    width = size
    height = size
    
    # Create a new RGB image with a horizontal gradient
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)
    
    # Generate a gradient background
    for x in range(width):
        r = int(x / width * 255)
        b = int((width - x) / width * 255)
        # Add some vertical variation
        for y in range(height):
            g = int(y / height * 255)
            draw.point((x, y), fill=(r, g, b))

    # Draw some smoother, semi-transparent shapes
    # We need to use RGBA mode for transparency
    img = img.convert('RGBA')
    
    for _ in range(15):
        x = random.randint(0, width)
        y = random.randint(0, height)
        radius = random.randint(size // 10, size // 4)
        
        color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(50, 150) # Alpha for transparency
        )
        
        # Create a new layer for each shape
        overlay = Image.new('RGBA', img.size, (0,0,0,0))
        overlay_draw = ImageDraw.Draw(overlay)
        overlay_draw.ellipse(
            [x - radius, y - radius, x + radius, y + radius],
            fill=color
        )
        # Composite the new layer onto the image
        img = Image.alpha_composite(img, overlay)

    # Convert back to RGB before saving as PNG
    img = img.convert('RGB')

    filename = f"input_{size}x{size}.png"
    img.save(filename)
    print(f"Generated: {filename}")

def main():
    # The sizes your C program needs
    sizes = [512, 1024, 2048, 4096]
    
    if not os.path.exists("output"):
        os.makedirs("output")

    print("Generating complex input images...")
    for size in sizes:
        create_test_image(size)
    
    print("\nDone! You can now run ./program4")

if __name__ == "__main__":
    main()