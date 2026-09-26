from fastapi import FastAPI
from backend.models.chat import ChatRequest

app = FastAPI()


@app.get("/")
def home():
    return {
        "project": "Agentic RAG",
        "status": "running"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    return {
        "received": request.message
    }