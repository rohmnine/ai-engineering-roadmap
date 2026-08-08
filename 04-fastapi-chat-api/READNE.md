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


## FastAPI Request Model校验问题


问题：

发送:

{
"text":""
}


返回:

422 Field required


原因：

Pydantic Request Model定义了必填字段。


解决：

给非核心字段设置默认值:

user:str | None=None

time:str | None=None


核心字段(text)由业务逻辑处理。