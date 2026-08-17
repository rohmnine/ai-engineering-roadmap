from fastapi import FastAPI

from app.api.chat_api import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def root():
    return  {
        "message":"AI API running"
    }