# startupx-backend/agents/pitch.py

import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


class PitchGeneratorAgent:
    @staticmethod
    def run(idea: str) -> str:
        prompt = f"""
You are a startup pitch coach.

Based on the startup idea below, generate a short, punchy 2–3 line elevator pitch.

Startup idea: "{idea}"

Return only the pitch text.
        """.strip()

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"[Pitch Agent Error]: {e}")
            return "Pitch unavailable at the moment."