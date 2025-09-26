# STRUCTURE_EXTRACTION_PROMPT = """
# You are an expert medical document processor.

# Your task is to analyze the following clinical or institutional document and return a structured JSON template.

# --- Text Starts ---
# {text}
# --- Text Ends ---

# Return the result in the following JSON format only:
# {
#     "template_title": "Extracted Template",
#     "source_type": "image/pdf/docx",
#     "sections": [
#         {
#             "title": "<Section Title>",
#             "content_type": "paragraph | field",
#             "verbosity": "concise"
#         },
#         ...
#     ]
# }

# - Use 'field' if it’s a short entry (like Name, Age, Gender, etc.).
# - Use 'paragraph' for longer blocks (like Medical History, Allergies).
# # - Do NOT include document headers like "Medical Report" or "For your record".
# - Group related fields under appropriate headings if applicable.

# Return only valid JSON. No explanation, no markdown, no extra text.
# """















STRUCTURE_EXTRACTION_PROMPT = """
You are a clinical documentation assistant.

Given the following raw document text, extract and return a clean structured JSON with:
- `template_title`: Title of the document (if any)
- `sections`: A list of sections. Each section must contain:
  - `section_title`: (string)
  - `fields`: list of field objects with:
      - `field_name`: (string)
      - `field_type`: (text, checkbox, date, number, dropdown, etc.)

Respond in pure JSON only. No explanations.

Here is the document:

{text}
"""
