# agents/persona.py
import os
import openai
import json
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class PersonaGeneratorAgent:
    @staticmethod
    def run(idea: str):
        prompt = f"""
You are a customer persona generator.

Given the startup idea: "{idea}", return 2-3 potential customer personas.

Each persona should include:
- name
- age
- occupation
- goals
- pain points
- how this product helps

Return as JSON like:
[
  {{
    "name": "Emily",
    "age": 29,
    "occupation": "Busy working professional",
    "goals": "Stay organized and save time on daily chores",
    "pain_points": "Forgets groceries, no time to track inventory",
    "how_product_helps": "Smart fridge reminds her what to buy and reduces food waste"
  }},
  ...
]
        """

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )
            content = response.choices[0].message.content
            return json.loads(content)
        except Exception as e:
            print(f"[PersonaAgent Error] {e}")
            return []