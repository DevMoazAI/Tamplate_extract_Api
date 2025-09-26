from fastapi import FastAPI, UploadFile, File
import os
import json
from template_extractor.extractor import extract_text_and_type
from template_extractor.llm_template_extractor import extract_structure_using_llm

app = FastAPI(title="Template Extractor API")

TEMPLATE_DIR = "templates"
os.makedirs(TEMPLATE_DIR, exist_ok=True)

def save_template_to_file(template_data: dict, filename: str):
    path = os.path.join(TEMPLATE_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(template_data, f, indent=4)

@app.post("/extract-template/")
async def extract_template(file: UploadFile = File(...)):
    contents = await file.read()
    file_path = os.path.join("temp_upload", file.filename)
    os.makedirs("temp_upload", exist_ok=True)

    with open(file_path, "wb") as f:
        f.write(contents)

    try:
        extracted_text, file_type = extract_text_and_type(file_path)

        structured_sections = extract_structure_using_llm(extracted_text)

        template_json = {
            "template_title": "Extracted Template",
            "source_type": file_type,
            "sections": structured_sections
        }

        json_filename = f"{os.path.splitext(file.filename)[0]}_template.json"
        save_template_to_file(template_json, json_filename)

        return {
            "message": "Template extracted and saved",
            "filename": json_filename,
            "template": template_json
        }

    except Exception as e:
        return {"error": str(e)}
