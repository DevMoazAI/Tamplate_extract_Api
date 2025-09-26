import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

def extract_text_from_text_pdf(file_path: str) -> str:
    doc = fitz.open(file_path)
    full_text = ""
    for page in doc:
        text = page.get_text()
        full_text += text + "\n"
    return full_text.strip()

def extract_text_from_scanned_pdf(file_path: str) -> str:
    doc = fitz.open(file_path)
    full_text = ""
    for page_index in range(len(doc)):
        pix = doc[page_index].get_pixmap(dpi=300)
        img_data = pix.tobytes("png")
        image = Image.open(io.BytesIO(img_data))
        text = pytesseract.image_to_string(image)
        full_text += text + "\n"
    return full_text.strip()

def parse_pdf(file_path: str) -> dict:
    text = extract_text_from_text_pdf(file_path)

    if len(text.strip()) < 20:  # If very little or no text, assume it's scanned
        text = extract_text_from_scanned_pdf(file_path)

    # from ..section_analyzer import analyze_sections
    # return analyze_sections(text, source_type="pdf")
