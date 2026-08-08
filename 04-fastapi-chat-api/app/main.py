from fastapi import FastAPI
from app.models import (ChatRequest, ChatResponse)

app = FastAPI()

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    text = request.text

    return ChatResponse(
        answer=f"你输入了:{text}"
    )