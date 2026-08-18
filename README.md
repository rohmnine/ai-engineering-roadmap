# AI Engineering Roadmap


AI Application Engineer Learning Journey


## Progress


## Day01 Python Environment

Completed:

- venv
- pip
- requests
- pytest


## Roadmap


30天路线总览
阶段	时间	目标
阶段1	Day1-5	Python + FastAPI工程基础
阶段2	Day6-10	LLM API + Prompt工程
阶段3	Day11-15	AI应用项目：简历分析助手
阶段4	Day16-22	RAG知识库开发
阶段5	Day23-26	AI Agent开发
阶段6	Day27-30	工程化部署 + 求职准备
第一阶段：Python + FastAPI基础
Day 1：Python工程环境
学习

目标：

掌握：

venv
pip
poetry
requirements

学习：

Python虚拟环境：

https://docs.python.org/3/library/venv.html

Poetry：

https://python-poetry.org/docs/

编码任务

创建：

ai-engineering-learning


├── app
├── tests
├── requirements.txt
└── README.md

完成：

python -m venv .venv


pip install requests
pip freeze > requirements.txt
今日产出

GitHub：

python-env-demo
Day 2：Python API调用

学习：

requests：

https://requests.readthedocs.io/

掌握：

GET
POST
JSON
Header
Token

编码：

调用：

天气API / Github API

完成：

Python程序


↓


HTTP API


↓


JSON解析


↓


打印结果

产出：

python-api-demo
Day 3：FastAPI入门

学习：

官方：

https://fastapi.tiangolo.com/tutorial/

掌握：

FastAPI
uvicorn
路由

代码：

实现：

GET /hello

返回：

{
"message":"hello AI"
}

产出：

fastapi-demo
Day 4：FastAPI REST接口

学习：

重点：

POST
Pydantic
Request Model

实现：

接口：

POST /chat

输入：

{
"text":"你好"
}

输出：

{
"answer":"hello"
}

产出：

chat-api-demo
Day 5：FastAPI工程结构

学习：

项目拆分：

controller
service
utils
config

对应你的Java经验：

SpringBoot：

Controller
Service
DTO
Config

完成：

标准项目结构：

app


├── api
├── service
├── config
└── main.py
第二阶段：LLM开发基础
Day 6：认识LLM API

学习：

理解：

Token
Context Window
Temperature
Model

阅读：

OpenAI API：

https://platform.openai.com/docs

任务：

调用：

LLM API

实现：

用户输入


↓


模型


↓


回答
Day 7：封装LLM Service

代码：

创建：

llm.py

实现：

def ask_llm(prompt):
    pass

目标：

业务代码不要直接调用模型。

Day 8：Prompt Engineering

学习：

Prompt结构：

Role


Context


Task


Constraint


Output

练习：

写：

招聘专家Prompt

输入：

简历

输出：

评价

Day 9：Few-shot + CoT

学习：

Few Shot：

给案例

CoT：

复杂任务拆解

练习：

让AI完成：

Java代码Review

Day 10：Structured Output

学习：

JSON输出

目标：

模型输出：

{
"score":90,
"skills":[
"Java",
"Spring"
]
}
第三阶段：AI简历分析助手
Day 11：项目设计

设计：

用户上传PDF


↓


PDF解析


↓


Prompt


↓


LLM


↓


JSON结果

技术：

FastAPI

PyPDF

LLM

Day 12：PDF解析

学习：

PyPDF：

https://pypdf.readthedocs.io/

完成：

上传PDF

读取文本

Day 13：简历Prompt设计

设计：

System Prompt：

你是一名技术招聘专家
分析候选人能力

输出：

技能评分
优势
不足
建议
Day 14：接口开发

完成：

接口：

POST /resume/analyze
Day 15：项目完善

增加：

README
Docker
Demo截图

上传GitHub

项目：

ai-resume-analyzer
第四阶段：RAG知识库
Day 16：理解RAG

学习：

概念：

Document


↓


Embedding


↓


Vector DB


↓


Retriever


↓


LLM

学习：

LangChain：

https://python.langchain.com/

Day 17：Embedding

学习：

理解：

文本：

↓

向量

练习：

生成文本Embedding

Day 18：Vector Database

学习：

FAISS

文档：

https://github.com/facebookresearch/faiss

完成：

存储：

文本
+
向量
Day 19：RAG Pipeline

实现：

PDF


↓


Chunk


↓


Embedding


↓


Search


↓


Answer
Day 20：企业知识库项目

项目：

company-knowledge-rag

功能：

上传：

员工手册

提问：

公司制度

Day 21-22：RAG优化

学习：

Chunk策略
Metadata
Retrieval

优化：

回答准确率

第五阶段：Agent开发
Day 23：Agent基础

学习：

Agent：

LLM


+


Tools


+


Memory


Day 24：Function Calling

学习：

模型调用工具：

例如：

查询数据库


调用API


搜索
Day 25：LangGraph

学习：

https://langchain-ai.github.io/langgraph/

完成：

简单Agent：

用户问题


↓


判断


↓


调用工具


↓


回答
Day 26：AI助手项目

项目：

ai-agent-assistant

功能：

自动：

搜索资料
总结
输出报告
第六阶段：工程化
Day 27：Docker

学习：

https://docs.docker.com/get-started/

掌握：

Dockerfile

镜像

容器

完成：

所有项目Docker化

Day 28：部署

学习：

Linux：

SSH
Nginx
环境变量

部署：

云服务器

Day 29：Java整合AI

学习：

Spring AI：

https://spring.io/projects/spring-ai

完成：

SpringBoot调用LLM

项目：

spring-ai-demo
Day 30：求职准备

整理：

GitHub：

README


架构图


运行截图


技术总结

简历关键词：

LLM


RAG


Agent


LangChain


FastAPI


Spring AI


Docker


Vector Database
每天时间安排（推荐）

如果每天4小时：

30分钟
看课程


1小时
看文档


2小时
写代码


30分钟
总结上传GitHub
推荐学习资源清单
Python

官方：
https://docs.python.org/3/

FastAPI

https://fastapi.tiangolo.com/

OpenAI API

https://platform.openai.com/docs

Prompt Engineering

https://platform.openai.com/docs/guides/prompt-engineering

LangChain

https://python.langchain.com/

LangGraph

https://langchain-ai.github.io/langgraph/

HuggingFace

https://huggingface.co/docs

Docker

https://docs.docker.com/

30天后的能力模型

你应该达到：

✅ 能写 FastAPI AI服务
✅ 能调用LLM API
✅ 能设计Prompt
✅ 能做Structured Output
✅ 能开发RAG知识库
✅ 能开发简单Agent
✅ 能Docker部署
✅ 能用Spring Boot接入AI