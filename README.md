# Image Compressor (JPG/PNG to WebP)

A Python-based tool that compresses and converts `.jpg` and `.png` images into `.webp` format, ensuring each image is **under 250KB** while maintaining reasonable visual quality. Perfect for web optimization or batch processing image directories.



## 🚀 Features

-  Bulk image processing
-  Converts `.jpg` and `.png` to `.webp`
- Automatically adjusts quality to stay under 250KB
- Uses Google WebP's highest compression method (`method=6`)
- Preserves RGB color mode
- Easy-to-use input/output directory setup


## 📁 Directory Structure

📂 input_images/

├── image1.jpg

├── image2.png

└── ...

📂 output_images/

├── image1.webp

├── image2.webp

└── ...

app.py

You place your original images in `input_images/`, and compressed WebP images will be saved in `output_images/`.


## ⚙️ How It Works

1. Open each image from the input folder.
2. Convert to RGB (WebP doesn’t support RGBA/CMYK well).
3. Start saving as WebP with quality 100 and method 6 (maximum compression).
4. If the file size is more than 250KB, reduce quality step-by-step until it's small enough.
5. Save the final `.webp` image in the output folder.



## 📦 Requirements

- Python 3.x
- [Pillow](https://pypi.org/project/Pillow/)

Install dependencies with:

```bash
pip install Pillow
        or
pip install -r needs.txt
```
## 📄 License
This project is open-source and free to use under the MIT License.
