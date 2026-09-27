from fastapi import FastAPI
from backend.models.chat import ChatRequest
from backend.agents.graph import agent

app = FastAPI()


@app.get("/")
def home():
    return {
        "project": "Agentic RAG",
        "status": "running"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    result = agent.invoke(
        {
            "message": request.message,
            "response": ""
        }
    )

    return result