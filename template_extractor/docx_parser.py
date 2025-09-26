from docx import Document
# from ..section_analyzer import analyze_sections

def extract_text_from_docx(file_path: str) -> str:
    doc = Document(file_path)
    full_text = []

    for para in doc.paragraphs:
        text = para.text.strip()
        if text:
            full_text.append(text)

    return "\n".join(full_text)

def parse_docx(file_path: str) -> dict:
    text = extract_text_from_docx(file_path)
    # return analyze_sections(text, source_type="docx")
