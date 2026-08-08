from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from app.models import ChatRequest, ChatResponse

app = FastAPI()

@app.exception_handler(ValueError)
async def value_error_exception_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},
    )

@app.post("/chat")
def chat(request: ChatRequest):

    if request.text.strip() == "":
        raise ValueError("text不能为空")
    return {
        "answer": f"输入了：{request.text}，用户是：{request.user},时间是：{request.time}"
    }
        