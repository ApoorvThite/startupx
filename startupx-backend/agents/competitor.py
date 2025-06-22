# agents/competitor.py

import os
import openai
import json
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class CompetitorScoutAgent:
    @staticmethod
    def run(idea: str):
        system_prompt = """
You are a startup scout agent.

Your task is to find 4-5 real, existing startups that are close competitors to the user's idea.
Each competitor must have:
- name
- a 2-3 sentence description
- a working URL (preferably from ProductHunt, Crunchbase, or the official homepage)

Include a field called 'differentiator' explaining what makes the competitor stand out.
Also, Focus on early-stage startups or trending projects from the last 2 years

Respond only with a JSON list like:
[
  {
    "name": "StartupName",
    "description": "What it does...",
    "url": "https://producthunt.com/posts/startupname",
    "differentiator": "Optional detail..."
  },
  ...
]
        """.strip()

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"The idea is: {idea}"}
                ],
                temperature=0.7
            )
            content = response.choices[0].message.content.strip()
            return json.loads(content)
        except Exception as e:
            print(f"Agent Error: {e}")
            return []

