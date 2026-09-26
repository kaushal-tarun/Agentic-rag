from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "project": "Agentic RAG",
        "status": "running"
    }