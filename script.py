from PIL import Image, ImageOps
import os

input_folder = "./input"
output_folder = "./output"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# A4 dimensions in pixels at 300 DPI
a4_width_px, a4_height_px = 2480, 3508

for filename in sorted(os.listdir(input_folder)):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        path = os.path.join(input_folder, filename)
        img = Image.open(path)
        img = ImageOps.exif_transpose(img).convert("RGB")

        # Resize while keeping the aspect ratio
        img.thumbnail((a4_width_px, a4_height_px), Image.LANCZOS)

        # Center the image on a white A4 page
        a4_page = Image.new(
            "RGB", (a4_width_px, a4_height_px), (255, 255, 255))
        offset = (
            (a4_width_px - img.width) // 2,
            (a4_height_px - img.height) // 2,
        )
        a4_page.paste(img, offset)

        # PDF file name
        base_name = os.path.splitext(filename)[0]
        output_pdf_path = os.path.join(output_folder, f"{base_name}.pdf")
        a4_page.save(output_pdf_path, "PDF")
        print(f"PDF generated: {output_pdf_path}")
