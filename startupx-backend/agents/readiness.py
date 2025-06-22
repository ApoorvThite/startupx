# agents/readiness.py

import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


class MarketReadinessAgent:
    @staticmethod
    def run(idea: str) -> int:
        prompt = f"""
You are a startup analyst.

On a scale of 1 to 10, how saturated is the market for the startup idea: "{idea}"?

- 1 means very fresh, very little competition.
- 10 means highly saturated, many players.

Only return the number. No explanation.
        """.strip()

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0
            )
            output = response.choices[0].message.content.strip()
            score = int(output)
            return score if 1 <= score <= 10 else 5  # fallback
        except Exception as e:
            print(f"MarketReadinessAgent Error: {e}")
            return 5  # default score