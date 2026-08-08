# Day 4 FastAPI REST API


## 学习内容

- POST请求
- Request Body
- Pydantic
- BaseModel
- Response Model


## 项目

chat-api-demo


## API


POST /chat


请求:

{
    "text":"你好"
}


返回:

{
    "answer":"hello"
}



## 遇到的问题


### 1. Pydantic是什么？

Pydantic用于数据验证。

FastAPI通过Pydantic自动检查请求参数。


### 2. Request Model作用？

定义客户端发送的数据结构。


例如:

class ChatRequest(BaseModel):

    text:str



## 启动方式


安装:

pip install -r requirements.txt


运行:

uvicorn app.main:app --reload



访问:

http://127.0.0.1:8000/docs