# agents/market_scope.py
import openai
import os
from dotenv import load_dotenv
import json

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class MarketScopeAgent:
    @staticmethod
    def run(idea: str):
        prompt = f"""
You're a market sizing analyst.

Estimate the following for the startup idea: "{idea}".

- TAM: Total addressable market (describe and provide rough $ size or user volume)
- SAM: Serviceable market (based on geography, audience, or use-case limitations)
- SOM: Serviceable obtainable market (what % of SAM could this idea realistically capture)

Return this as a JSON:
{{
  "tam": "...",
  "sam": "...",
  "som": "..."
}}
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
            print(f"MarketScopeAgent error: {e}")
            return {
                "tam": "N/A",
                "sam": "N/A",
                "som": "N/A"
            }