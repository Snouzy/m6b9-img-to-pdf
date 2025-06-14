from PIL import Image, ImageOps
import os

# Dossier contenant les images
input_folder = "./input"
output_pdf = "output.pdf"

# Dimensions A4 en pixels à 300 DPI
a4_width_px, a4_height_px = 2480, 3508

images = []
for filename in sorted(os.listdir(input_folder)):
    if filename.lower().endswith(".jpg"):
        path = os.path.join(input_folder, filename)
        img = Image.open(path)
        img = ImageOps.exif_transpose(img).convert("RGB")

        # Resize tout en gardant le ratio
        img.thumbnail((a4_width_px, a4_height_px), Image.LANCZOS)

        # Centrer l'image sur une page A4 blanche
        a4_page = Image.new(
            "RGB", (a4_width_px, a4_height_px), (255, 255, 255))
        offset = (
            (a4_width_px - img.width) // 2,
            (a4_height_px - img.height) // 2,
        )
        a4_page.paste(img, offset)
        images.append(a4_page)

if images:
    images[0].save(output_pdf, save_all=True, append_images=images[1:])
    print(f"PDF généré : {output_pdf}")
else:
    print("Aucune image JPG trouvée.")
