


# # # import re

# # # def detect_sections_from_text(text: str):
# # #     lines = [line.strip() for line in text.splitlines() if line.strip()]
# # #     sections = []

# # #     table_keywords = ["DATE", "TREATMENT", "DESCRIPTION"]
# # #     table_section_detected = False

# # #     for line in lines:
# # #         upper_line = line.upper()

# # #         # Table-like detection
# # #         if not table_section_detected and all(keyword in upper_line for keyword in table_keywords):
# # #             sections.append({
# # #                 "title": "Treatment Table",
# # #                 "content_type": "table",
# # #                 "verbosity": "detailed",
# # #                 "columns": table_keywords
# # #             })
# # #             table_section_detected = True
# # #             continue

# # #         # Fields (name, age, gender etc.)
# # #         if re.search(r":|\bAGE\b|\bGENDER\b|\bWEIGHT\b|\bHEIGHT\b|\bDOCTOR\b|\bPATIENT\b", upper_line):
# # #             matches = re.findall(r"([A-Z ]+):?", upper_line)
# # #             for match in matches:
# # #                 sections.append({
# # #                     "title": match.title(),
# # #                     "content_type": "field",
# # #                     "verbosity": "concise"
# # #                 })
# # #             continue

# # #         # Heading section
# # #         if upper_line.isupper() and len(upper_line) < 40:
# # #             sections.append({
# # #                 "title": line.title(),
# # #                 "content_type": "paragraph",
# # #                 "verbosity": "concise"
# # #             })
# # #             continue

# # #         # Long content section (fallback)
# # #         if len(line.split()) > 5:
# # #             sections.append({
# # #                 "title": line[:30] + ("..." if len(line) > 30 else ""),
# # #                 "content_type": "paragraph",
# # #                 "verbosity": "detailed"
# # #             })

# # #     return sections




# import re

# # Define a list of known medical terms that are likely headings
# KNOWN_HEADINGS = {
#     "patient", "age", "gender", "weight", "height", "doctor",
#     "temperature", "heart rate", "blood pressure", "treatment",
#     "description", "allergies", "records", "medical history", "history",
#     "assessment", "plan", "diagnosis", "vitals"
# }

# # Optional: for common OCR misspellings
# CORRECTIONS = {
#     "blood preasure": "blood pressure",
#     "foryour": "",
#     "bp": "blood pressure"
# }

# def clean_heading(text: str) -> str:
#     """Cleans and normalizes heading text."""
#     text = text.strip()
#     text = re.sub(r"\s+", " ", text)  # remove extra spaces
#     text = text.lower()

#     # Correct known typos
#     if text in CORRECTIONS:
#         text = CORRECTIONS[text]

#     return text.title().strip()


# def detect_sections_from_text(extracted_text: str) -> list:
#     lines = extracted_text.splitlines()
#     seen = set()
#     sections = []

#     for line in lines:
#         line_clean = line.strip()

#         # Ignore empty or very short lines
#         if not line_clean or len(line_clean) < 3:
#             continue

#         # Reject lines that are clearly non-heading
#         if len(line_clean.split()) > 6:  # Too long for heading
#             continue

#         cleaned = clean_heading(line_clean)

#         if not cleaned or cleaned.lower() in seen:
#             continue

#         # Match known headings or use heuristics
#         is_known = cleaned.lower() in KNOWN_HEADINGS
#         looks_like_heading = cleaned.istitle() or cleaned.isupper()

#         if is_known or looks_like_heading:
#             # Decide content type based on heading nature
#             content_type = "field" if any(word in cleaned.lower() for word in ["age", "gender", "height", "weight", "patient", "doctor"]) else "paragraph"
#             sections.append({
#                 "title": cleaned,
#                 "content_type": content_type,
#                 "verbosity": "concise"
#             })
#             seen.add(cleaned.lower())

#     return sections
