
```markdown
 AI应用开发工程师（LLM + Java后端）12周学习计划

> 目标：从 Java 后端开发方向转向 AI 应用开发工程师  
> 技术路线：LLM 应用开发 + RAG + Agent + 工程化部署

---
 1. 学习目标
经过12周学习，达到：
- 能独立开发基于大模型的应用
- 掌握 RAG 知识库系统开发
- 掌握 Agent 基础开发
- 能使用 Java + Python 构建 AI 服务
- 能完成 AI 应用部署
- 形成可用于求职的项目作品
---
 2. 技术路线
```
Java Spring Boot -> LLM API调用 -> Prompt Engineering -> RAG知识库系统 -> Agent应用开发 -> AI工程化部署 -> 求职项目包装
---

 Week 1-2：LLM应用基础
 学习目标
掌握：
- Python AI开发基础
- LLM API调用
- Prompt Engineering
- FastAPI基础

学习内容
  LLM基础
理解：
- Token
- Context Window
- Temperature
- Embedding

 Prompt
掌握：
- Role
- Context
- Instruction
- Output Format

 项目
完成：
  AI Chat Assistant
技术：
- Vue3
- FastAPI
- LLM API
功能：
- 对话
- Markdown渲染
- 历史记录
产出：

```

projects/
└── llm-chat-assistant

```

---

 Week 3-5：企业级RAG系统

 学习目标
掌握企业AI应用核心技术。
 学习内容
- 文档解析
- Text Split
- Embedding
- Vector Database
- Retriever
- LangChain

 项目
 企业知识库智能问答系统

架构：

```
Vue -> Spring Boot -> FastAPI -> Embedding + Vector DB -> LLM

```

功能：

- 用户管理
- 文件上传
- PDF解析
- 知识库构建
- 智能问答
- 引用来源

技术：

- Spring Boot
- FastAPI
- MySQL
- FAISS/Milvus
- Docker

产出：

```

projects/

└── enterprise-rag-system

```

---

 Week 6-8：Agent开发

  学习材料
推荐：
Datawhale Hello Agents

学习：

- Agent架构
- Tool Calling
- Function Calling
- Memory
- Workflow

项目

 AI会议助手

升级已有实习项目：

原流程：

```

音频 -> 文本 -> 总结 -> Word

```

升级：

```

音频 -> 文本 -> 知识库 -> Agent -> 任务生成 -> 报告输出

```

技术：

- LangChain
- LangGraph
- Dify
- FastAPI

产出：

```

projects/

└── meeting-agent

```

---

 Week 9-10：AI工程化


 学习目标

达到企业部署能力。
学习：

- Docker
- Docker Compose
- Linux
- Nginx
- Ollama
- Xinference

完成：

AI应用生产部署。

架构：

```

Nginx -> Spring Boot -> FastAPI -> LLM

```

---

 Week 11-12：求职准备


 技术复习

LLM：

- Transformer基本思想
- Prompt作用
- Token机制

RAG：

- 为什么需要RAG
- Embedding原理
- 如何提高检索准确率

Agent：

- Agent是什么
- Tool Calling
- Workflow设计

---

 简历项目

 项目1

企业知识库RAG系统

关键词：

- Spring Boot
- FastAPI
- LangChain
- Vector Database
- Docker

---

 项目2

Agent智能会议助手

关键词：

- Agent
- Workflow
- Tool Calling
- RAG

---

 项目3

私人媒体管理系统

体现：

- 后端开发能力
- 系统设计能力
- 部署能力

---

 GitHub维护原则

不要上传：

- 单纯课程截图
- 复制代码
- API Key

推荐上传：

- 项目代码
- 技术笔记
- 架构图
- 项目README
- 学习总结

---

核心竞争力：

```

Java后端能力
*
LLM应用开发能力
*
AI工程部署能力

---
