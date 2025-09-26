# import os
# from template_extractor.pdf_parser import extract_text_from_text_pdf, extract_text_from_scanned_pdf
# from template_extractor.docx_parser import extract_text_from_docx
# from template_extractor.image_parser import extract_text_from_image
# # from llm_template_extractor import extract_template_with_llm


# # structured_template = extract_template_with_llm(ocr_or_doc_text)

# def extract_text_and_type(file_path: str) -> tuple[str, str]:
#     ext = os.path.splitext(file_path)[-1].lower()

#     if ext == ".pdf":
#         text = extract_text_from_text_pdf(file_path)
#         if len(text.strip()) < 20:
#             text = extract_text_from_scanned_pdf(file_path)
#         file_type = "pdf"

#     elif ext == ".docx":
#         text = extract_text_from_docx(file_path)
#         file_type = "docx"

#     elif ext in [".jpg", ".jpeg", ".png"]:
#         text = extract_text_from_image(file_path)
#         file_type = "image"

#     else:
#         raise ValueError("Unsupported file type")

#     return text, file_type









import os
from typing import Tuple
from template_extractor.pdf_parser import extract_text_from_text_pdf, extract_text_from_scanned_pdf
from template_extractor.docx_parser import extract_text_from_docx
from template_extractor.image_parser import extract_text_from_image

def extract_text_and_type(file_path: str) -> Tuple[str, str]:
    ext = os.path.splitext(file_path)[-1].lower()

    if ext == ".pdf":
        # Try to extract from text-based PDF first
        text = extract_text_from_text_pdf(file_path)
        if not text or len(text.strip()) < 20:
            # Fallback to OCR for scanned PDF
            text = extract_text_from_scanned_pdf(file_path)
        file_type = "pdf"

    elif ext == ".docx":
        text = extract_text_from_docx(file_path)
        file_type = "docx"

    elif ext in [".jpg", ".jpeg", ".png"]:
        text = extract_text_from_image(file_path)
        file_type = "image"

    else:
        raise ValueError(f"Unsupported file type: {ext}")

    # Final validation
    if not text or len(text.strip()) < 20:
        raise ValueError("Extracted text is empty or too short to process.")

    return text.strip(), file_type

