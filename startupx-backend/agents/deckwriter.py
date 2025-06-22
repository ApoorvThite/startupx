# deckwriter.py
import os
import openai
from dotenv import load_dotenv
import json

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class DeckWriterAgent:
    @staticmethod
    def run(idea: str):
        prompt = f"""
You are a startup pitch deck assistant. Create a concise 5-slide outline for a startup based on this idea: "{idea}".

Each slide should have:
- Slide title
- 2-3 bullet points (short)
- No design elements, only text

Return JSON format:
[
  {{
    "title": "Slide Title",
    "bullets": ["Point 1", "Point 2", "Point 3"]
  }},
  ...
]
"""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.6
            )
            slides = response.choices[0].message.content
            return eval(slides)
        except Exception as e:
            print(f"DeckWriterAgent error: {e}")
            return []