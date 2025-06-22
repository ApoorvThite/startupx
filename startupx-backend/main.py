from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from agents.competitor import CompetitorScoutAgent  # 👈 Import your agent
from pydantic import BaseModel
from typing import List
import random
from agents.tag_generator import TagGeneratorAgent
from agents.readiness import MarketReadinessAgent
from agents.persona import PersonaGeneratorAgent  # 👈 Import the new agent

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class IdeaRequest(BaseModel):
    idea: str

@app.get("/")
def root():
    return {"message": "StartupX backend is running"}

cache = {}

@app.post("/evaluate_idea")
async def evaluate_idea(data: IdeaRequest):
    idea = data.idea.strip().lower()

    # Check cache or initialize result dict
    if idea in cache:
        return cache[idea]

    try:
        competitors = CompetitorScoutAgent.run(idea)
    except Exception as e:
        print(f"Competitor agent failed: {e}")
        competitors = []

    try:
        tags = TagGeneratorAgent.run(idea)
    except Exception as e:
        print(f"Tag agent failed: {e}")
        tags = []

    try:
        readiness_score = MarketReadinessAgent.run(idea)
    except Exception as e:
        print(f"Readiness agent failed: {e}")
        readiness_score = 5

    try:
        personas = PersonaGeneratorAgent.run(idea)  # 👈 Add this block
    except Exception as e:
        print(f"Persona agent failed: {e}")
        personas = []

    result = {
        "competitors": competitors,
        "tags": tags,
        "readiness": readiness_score,
        "personas": personas  # 👈 Include in response
    }
    cache[idea] = result
    return result
