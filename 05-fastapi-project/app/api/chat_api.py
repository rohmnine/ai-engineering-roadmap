from fastapi import APIRouter
from pydantic import BaseModel
from app.service.chat_service import chat_service

router = APIRouter(
    prefix="/chat",
    tags=["chat"]
)

class ChatRequest(BaseModel):
    message:str
    user:str

@router.post("")
def create_chat(request:ChatRequest):

    return{
        "user":request.user,
        "answer":chat_service(request.message)
    }