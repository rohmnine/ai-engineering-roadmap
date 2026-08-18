# Day 05 - FastAPI 工程结构学习

## 项目介绍

本项目是 AI 应用开发学习路线 Day 5 项目。

主要学习 FastAPI 企业级项目结构设计，将之前简单的单文件 FastAPI 接口，拆分为：

- API 层（Controller）
- Service 层（业务逻辑）
- Config 层（配置管理）

通过项目拆分，理解 FastAPI 项目如何进行工程化开发。

---

# 学习目标

- 理解 FastAPI 项目分层思想
- 掌握 APIRouter 路由拆分
- 理解 Controller / Service 分离
- 学习 Python package 结构
- 理解 FastAPI 与 SpringBoot 架构对应关系


---

# 技术栈

- Python 3.10
- FastAPI
- Uvicorn
- Pydantic Settings


---

# 项目结构

```
05-fastapi-project

├── app
│
│   ├── api
│   │   ├── __init__.py
│   │   └── chat.py
│   │
│   ├── service
│   │   ├── __init__.py
│   │   └── chat_service.py
│   │
│   ├── config
│   │   ├── __init__.py
│   │   └── settings.py
│   │
│   └── main.py
│
├── requirements.txt
│
├── README.md
│
└── .gitignore

```

---

# SpringBoot 与 FastAPI 对照

由于之前学习 Java SpringBoot，因此使用 SpringBoot 思维理解 FastAPI。


| SpringBoot | FastAPI | 作用 |
| ---- | ---- | ---- |
| Controller | api | 接收 HTTP 请求 |
| Service | service | 处理业务逻辑 |
| DTO | schemas | 数据模型 |
| Config | config | 项目配置 |
| Application.java | main.py | 项目启动入口 |


---

# 请求流程

```
用户请求

    ↓

api/chat.py

Controller层

    ↓

service/chat_service.py

业务处理

    ↓

AI模型/API/数据库

    ↓

返回结果

```


---

# 核心代码说明


## 1. main.py

作用：

- 创建 FastAPI 实例
- 注册 Router


示例：

```python
from fastapi import FastAPI

from app.api.chat import router


app = FastAPI()


app.include_router(router)


@app.get("/")
def root():

    return {
        "message":"AI API running"
    }

```


---

## 2. API层


文件：

```
app/api/chat.py
```


职责：

- 接收请求
- 参数校验
- 调用 Service


示例：

```python
@router.post("/chat")
def create_chat(message:str):

    result = chat_service(message)

    return {
        "answer":result
    }

```


---

## 3. Service层


文件：

```
app/service/chat_service.py
```


职责：

处理业务逻辑。


示例：

```python
def chat_service(message):

    return "AI:" + message

```


---

# Config配置管理


文件：

```
app/config/settings.py
```


用于管理：

- API Key
- 模型名称
- 数据库地址
- 环境变量


示例：

```python
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    model_name:str="gpt-4"


settings = Settings()

```

---

# 项目启动


进入项目目录：

```bash
cd 05-fastapi-project
```


启动：

```bash
uvicorn app.main:app --reload
```


成功后访问：

```
http://127.0.0.1:8000/docs
```


FastAPI 自动生成 Swagger API 文档。


---

# 开发过程中遇到的问题


## 问题1：无法加载 app.main


错误：

```
ERROR:
Could not import module "app.main"
```


原因：

Uvicorn 找不到：

```
app/main.py
```


排查：

1. 检查项目结构

```
app
 └── main.py
```


2. 检查启动命令


正确：

```bash
uvicorn app.main:app --reload
```


含义：

```
app

↓

main.py

↓

app对象

```


---

# 问题2：chat.router 不存在


错误：

```
AttributeError:
'function' object has no attribute 'router'
```


错误代码：

```python
from app.api import chat


app.include_router(
    chat.router
)

```


原因：

Python 导入的 chat 不是：

```
app/api/chat.py
```

模块。


而是：

```
chat()
```

函数。


产生原因：

项目中存在同名：

```
api/chat.py

service/chat_service.py

chat()
```


Python import 时产生名称冲突。


---

# 解决方案


## 方法1：清空 api/__init__.py


不要：

```python
from .chat import chat
```


保持：

```
api
|
└── __init__.py
```


为空。


---

## 方法2：明确导入 router（推荐）


修改：

```python
from app.api.chat import router


app.include_router(router)

```


避免：

```
模块名

函数名

```

冲突。


---

# Python 包结构理解


Python 中：

目录：

```
app

```

如果想被 import：

需要：

```
__init__.py
```


例如：

```
app

├── __init__.py
├── main.py

```


类似 Java：

```
package com.xxx;

```


---

# 本日收获


完成 Day05 后：

✅ 掌握 FastAPI 项目结构

✅ 理解 Controller / Service 分层

✅ 学会 APIRouter 拆分接口

✅ 理解 Python import 机制

✅ 解决模块和函数命名冲突问题

✅ 为后续学习：

- OpenAI API调用
- LangChain
- RAG
- Agent

打下工程基础


---

# 下一步学习计划

Day06：

FastAPI + Pydantic 数据模型


学习：

- BaseModel
- Request DTO
- Response Model
- 参数校验
- 数据验证


对应 SpringBoot：

```
DTO

+
@Valid

+
ResponseEntity

```
