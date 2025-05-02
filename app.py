import os
from PIL import Image

def compress_image(input_path, output_path, max_size_kb=250):
    img = Image.open(input_path).convert("RGB")
    quality = 100
    step = 5

    while quality > 0:
        img.save(output_path, format='WEBP', quality=quality, method=6)
        size_kb = os.path.getsize(output_path) / 1024

        if size_kb <= max_size_kb:
            print(f"✅ {os.path.basename(input_path)} -> {size_kb:.2f} KB (quality={quality})")
            return True
        
        quality -= step

    print(f"❌ {os.path.basename(input_path)} could not compress under {max_size_kb}KB.")
    return False

def compress_folder(input_folder, output_folder, max_size_kb=250):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(input_folder, filename)
            output_name = os.path.splitext(filename)[0] + '.webp'
            output_path = os.path.join(output_folder, output_name)

            compress_image(input_path, output_path, max_size_kb)

# Example usage:
input_folder = "images"          # Your source folder with .jpg/.png files
output_folder = "compressed"     # Output folder for .webp files

compress_folder(input_folder, output_folder)
