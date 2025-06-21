from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS so frontend can connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/evaluate_idea")
async def evaluate_idea(request: Request):
    data = await request.json()
    idea = data.get("idea", "")
    
    # Mock response
    return {"response": f"Evaluated idea: '{idea}' looks promising!"}