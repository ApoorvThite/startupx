# agents/swot.py
import os
import openai
import json
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


class SWOTAgent:
    @staticmethod
    def run(idea: str):
        prompt = f"""
You are a startup strategist.

Perform a SWOT analysis (Strengths, Weaknesses, Opportunities, Threats) for the startup idea: "{idea}".

Return the output as a JSON object like this:

{{
  "strengths": ["..."],
  "weaknesses": ["..."],
  "opportunities": ["..."],
  "threats": ["..."]
}}
        """.strip()

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
            )
            content = response.choices[0].message.content
            return json.loads(content)
        except Exception as e:
            print(f"SWOT Agent Error: {e}")
            return {
                "strengths": [],
                "weaknesses": [],
                "opportunities": [],
                "threats": []
            }