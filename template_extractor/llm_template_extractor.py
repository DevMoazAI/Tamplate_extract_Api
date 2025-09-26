

import json
import os
from openai import OpenAI
from dotenv import load_dotenv
from template_extractor.prompt_template import STRUCTURE_EXTRACTION_PROMPT

# Load environment variables
load_dotenv()

# Create OpenAI client instance
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_URL", "https://api.openai.com/v1")
)

def extract_structure_using_llm(text: str) -> dict:
    prompt = STRUCTURE_EXTRACTION_PROMPT.format(text=text)

    try:
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_API_MODEL", "gpt-4o-mini"),
            messages=[
                {"role": "system", "content": "You are a helpful assistant that structures documents into JSON format."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        response_text = response.choices[0].message.content.strip()

        #  Clean string & try JSON parsing safely
        try:
            parsed = json.loads(response_text)
        except json.JSONDecodeError:
            # Handle common errors (extra backslashes, multiline artifacts)
            cleaned = response_text.replace('\n', '').replace('\\"', '"').strip()
            parsed = json.loads(cleaned)

        return parsed

    except Exception as e:
        raise RuntimeError(f"LLM extraction failed: {str(e)}")
