# Day 6：认识 LLM API

> AI应用开发工程师学习路线 Day6  
> 目标：理解LLM API工作原理，并完成第一个用户输入 → LLM → AI回答程序

---

# 今日学习目标

完成：
用户输入

↓

Python程序

↓

LLM API

↓

模型推理

↓

返回回答


理解：


- Token
- Context Window
- Temperature
- Model
- System Prompt
- API调用流程
- 异常处理

---


# 一、LLM API 基础理解

## 什么是 LLM API？

LLM API 是通过 HTTP 请求调用大语言模型能力。

应用程序不需要自己运行大模型，而是：



用户

↓

应用程序

↓

API请求

↓

LLM服务器

↓

模型生成回答

↓

返回结果



---


# 二、核心概念学习


## 1. Token


Token 是模型处理文本的基本单位。


流程：



文字

↓

Token

↓

数字表示

↓

模型计算



Token影响：


- API调用费用
- 最大输入长度
- 上下文容量




---


## 2. Context Window


Context Window：


> 模型一次能够处理的信息总量。




例如：



系统提示词

历史聊天记录

用户输入

文件内容



不能超过模型最大 Context Window。




聊天机器人能够记住之前内容，是因为：


程序会把历史消息重新发送给模型。




---


## 3. Temperature


Temperature 控制模型输出随机性。



低：



temperature = 0

输出稳定
适合：

编程
数据分析
企业应用


高：



temperature ↑

输出更加随机
适合：

创意写作
内容生成


---


## 4. Model


模型代表不同能力的大脑。


不同模型：


- 推理能力不同
- 速度不同
- 成本不同




选择模型需要考虑：


|场景|选择|
|-|-|
|聊天|普通模型|
|代码生成|强模型|
|复杂推理|高级模型|
|大量文本|长上下文模型|


---


# 三、项目环境搭建


项目结构：



06-llm-api

├── main.py
├── .env
├── .gitignore
└── README.md





---


安装依赖：


```bash
pip install openai python-dotenv


四、环境变量配置

创建：

.env

OPENAI_API_KEY=你的API_KEY

.gitignore：

.env
.venv/

避免：

API Key泄露
虚拟环境上传


五、第一次调用 LLM API

使用 OpenAI Responses API。

实现：

Python程序


↓


OpenAI API


↓


LLM模型


↓


文本回答


六、实现用户输入 → AI回答


运行效果：

用户:
什么是FastAPI?


AI:
FastAPI是一个Python Web框架...


七、遇到的问题记录
问题1：chat.completions 参数错误

错误：

TypeError:
Missing required arguments;
Expected either ('messages' and 'model')

原因：

使用：

client.chat.completions.create()

必须提供：

model


messages

正确：

client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role":"user",
            "content":"你好"
        }
    ]
)

解决：

学习新版 Responses API：

client.responses.create(
    model="gpt-4o-mini",
    input="你好"
)


八、练习1：基础调用

完成：

用户输入


↓


LLM


↓


返回回答


九、练习2：System Prompt
目标

让AI：

你是一名Python老师


回答必须简单易懂

代码：

response = client.responses.create(
    model="gpt-4o-mini",


    instructions="""
    你是一名Python老师。
    请使用简单易懂的语言回答。
    面向初学者解释。
    """,


    input=user_input
)
为什么需要 System Prompt？

没有prompt模型不知道：

身份
角色
输出风格
用户目标

System Prompt 可以控制：

模型行为


↓


输出风格


↓


回答范围

应用：

AI客服
AI老师
企业知识助手


十、练习3：限制输出长度

目标：

用户：

介绍Java

AI：

100字以内

方法：

Prompt限制：

instructions="""
回答要求：


1. 中文回答
2. 不超过100字
3. 简单易懂
"""

工程实践：

Prompt限制

+

程序校验


十一、练习4：异常处理

目标：

没有API Key：

输出：

请配置OPENAI_API_KEY

代码：

api_key = os.getenv(
    "OPENAI_API_KEY"
)

if not api_key:


    print(
        "请配置OPENAI_API_KEY"
    )


    exit()


十二、今日收获

今天完成了从：

Python程序到调用大语言模型的第一次连接。

理解：

用户输入


↓


Prompt


↓


API请求


↓


Token处理


↓


模型推理


↓


生成回答


↓


返回结果

AI应用开发不是训练模型，而是：

模型能力


+


工程封装


+


业务逻辑
