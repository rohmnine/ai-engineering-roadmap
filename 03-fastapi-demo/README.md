# Day03 FastAPI Demo


## 学习内容

- FastAPI
- Uvicorn
- Route
- JSON Response


## 项目功能

实现简单HTTP API。


## 环境

Python 3.10


## 安装


```bash
pip install -r requirements.txt
```


## 运行


```bash
uvicorn main:app --reload
```


## API


### GET /hello


返回：

```json
{
    "message":"hello AI"
}
```


## 项目结构


```
fastapi-demo

├── main.py
├── requirements.txt
└── README.md

```


## 今日问题记录


### 1. uvicorn启动失败

原因：

没有激活虚拟环境


解决：

重新执行：

```bash
.\.venv\Scripts\activate
```

