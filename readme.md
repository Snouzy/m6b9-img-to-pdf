# img-to-pdf

## 📄 Description

**img-to-pdf** is a simple Python script that automatically converts all images in a folder into individual PDF files, formatted to A4 and ready for printing or sharing.

- Place your images (`.jpg`, `.jpeg`, `.png`) in the `input/` folder.
- The script centers each image on a white A4 page, preserving the aspect ratio.
- Each image is exported to the `output/` folder with the same filename, but as a `.pdf`.

## 🚀 Quick Start

### 1. Clone or Download the Project

```bash
# Clone the repository or download the script
cd path/to/your/project
```

### 2. Set Up a Python Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install pillow
```

### 4. Add Your Images

- Place your images in the `input/` folder (create it if it doesn't exist).

### 5. Run the Script

```bash
python script.py
```

- Your PDFs will be generated in the `output/` folder.

## 🛠️ Requirements

- Python 3
- [Pillow](https://python-pillow.org/) (`pip install pillow`)
- [fpdf](https://www.fpdf.org/) (`pip install fpdf`)

## 💡 Use Cases

- Prepare images for printing or archiving
- Quickly generate PDFs from photos (scans, documents, etc.)
- Automate batch image-to-PDF conversion

---

