from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Engineering is the future of technology!"}

@app.get("/user")
def user():
    return {"name": "AI Engineer","level":"beginner"}