# import re
# from typing import List, Dict

# def is_bullet_point(text: str) -> bool:
#     return bool(re.match(r"^\s*[-*•]\s+", text.strip()))

# def guess_content_type(content_lines: List[str]) -> str:
#     bullet_count = sum(1 for line in content_lines if is_bullet_point(line))
#     ratio = bullet_count / max(len(content_lines), 1)
#     return "bullet_points" if ratio > 0.5 else "paragraph"

# def guess_verbosity(content: str) -> str:
#     word_count = len(content.split())
#     if word_count < 30:
#         return "concise"
#     else:
#         return "detailed"

# def split_sections(text: str) -> List[Dict]:
#     lines = text.splitlines()
#     sections = []
#     current_section = {"title": "Untitled", "content": []}

#     for line in lines:
#         # Match typical section headers
#         if re.match(r"^[A-Z][A-Za-z0-9 \-/]{2,30}:?$", line.strip()):
#             # Save the previous section
#             if current_section["content"]:
#                 sections.append(current_section)
#             # Start a new one
#             current_section = {
#                 "title": line.strip().rstrip(":"),
#                 "content": []
#             }
#         else:
#             if line.strip():
#                 current_section["content"].append(line.strip())

#     # Add the final section
#     if current_section["content"]:
#         sections.append(current_section)

#     return sections

# def analyze_sections(text: str, source_type="unknown") -> dict:
#     section_data = split_sections(text)
#     structured = []

#     for sec in section_data:
#         content_text = "\n".join(sec["content"])
#         structured.append({
#             "title": sec["title"],
#             "content_type": guess_content_type(sec["content"]),
#             "verbosity": guess_verbosity(content_text)
#         })

#     return {
#         "template_title": "Extracted Template",
#         "source_type": source_type,
#         "sections": structured
#     }
