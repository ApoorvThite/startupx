# agents/tag_generator.py
import os
import openai
import json
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class TagGeneratorAgent:
    @staticmethod
    def run(idea: str):
        prompt = f"""
You are a helpful AI assistant.

Given the startup idea: "{idea}", generate 3 to 5 relevant hashtags that describe the idea.

Only return a JSON array of strings, like:
[
  "#AI",
  "#Healthcare",
  "#MentalHealth"
]
        """.strip()

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )
            content = response.choices[0].message.content
            return json.loads(content)
        except Exception as e:
            print(f"Tag Agent Error: {e}")
            return []