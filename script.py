from fpdf import FPDF
from PIL import Image
import os

input_folder = "./input"
output_folder = "./output"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

for filename in sorted(os.listdir(input_folder)):
    if filename.lower().endswith(".jpg"):
        image_path = os.path.join(input_folder, filename)
        im = Image.open(image_path)
        width, height = im.size

        # Rotate if landscape
        if width > height:
            im = im.transpose(Image.ROTATE_270)

        temp_path = os.path.join(output_folder, "temp.jpg")
        im.save(temp_path)

        # Create PDF
        pdf = FPDF(unit="mm", format="A4")
        pdf.add_page()
        pdf.image(temp_path, 0, 0, 210, 297)
        output_pdf_path = os.path.join(
            output_folder, f"{os.path.splitext(filename)[0]}.pdf")
        pdf.output(output_pdf_path, "F")
        os.remove(temp_path)
        print(f"PDF generated: {output_pdf_path}")
