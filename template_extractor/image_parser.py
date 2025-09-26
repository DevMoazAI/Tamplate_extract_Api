from PIL import Image
import pytesseract
# from .section_analyzer import analyze_sections

def extract_text_from_image(file_path: str) -> str:
    image = Image.open(file_path)
    text = pytesseract.image_to_string(image)
    return text.strip()

def parse_image(file_path: str) -> dict:
    text = extract_text_from_image(file_path)
    # return analyze_sections(text, source_type="image")
