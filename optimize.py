import os
from PIL import Image

def optimize_image(full_path):
    print(f"optimizing {full_path}...")
    filename = os.path.basename(full_path)
    if filename.lower().endswith(('.png', '.jpg','.jpeg')):

        # Open the image
        with Image.open(full_path) as img:
            # Convert to RGB if necessary
            rgb_img = img.convert('RGB')

            rgb_img.thumbnail((700,500))

            # Save as WebP
            webp_filepath = f"{os.path.splitext(full_path)[0]}.webp"
            rgb_img.save(webp_filepath, 'WEBP', quality=100)

            # Optionally delete the original file
            # os.remove(filepath)
            print(f"Optimized: {filename}")

for path in os.listdir("./static/img/"):
    optimize_image("./static/img/"+path)
