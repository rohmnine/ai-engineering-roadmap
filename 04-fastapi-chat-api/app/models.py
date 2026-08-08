from pydantic import BaseModel,Field

class ChatRequest(BaseModel):

    text: str = Field(description="用户输入的文本")
    user: str | None = None
    time: str | None = None

class ChatResponse(BaseModel):
    answer: str