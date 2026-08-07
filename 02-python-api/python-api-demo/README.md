# Day 02 - Python API 调用

## 学习目标

掌握 Python 调用 HTTP API 的基础能力，为后续 AI 应用开发中的：

* 大模型 API 调用
* 第三方服务集成
* FastAPI 后端开发
* Agent 工具调用

建立基础。

---

# 学习内容

## 1. HTTP API 基础

学习：

* HTTP Request / Response
* REST API 基本概念
* GET 请求
* POST 请求
* URL 参数
* Header
* Token认证

基本流程：

```
Python程序

↓

HTTP Request

↓

API服务器

↓

JSON Response

↓

Python解析

```

---

# 2. requests库

学习官方文档：

https://requests.readthedocs.io/

掌握：

## GET请求

用于获取数据：

```python
requests.get(url)
```

## POST请求

用于提交数据：

```python
requests.post(
    url,
    json=data
)
```

## Header

用于传递额外信息：

```python
headers={
    "Authorization":"Bearer TOKEN"
}
```

## JSON解析

API返回：

```json
{
    "name":"OpenAI"
}
```

Python解析：

```python
data=response.json()

print(data["name"])
```

---

# 实战项目

## Python API Demo

项目位置：

```
python-api-demo
```

实现功能：

### 1. Github API调用

功能：

根据 Github 用户名获取用户信息。

调用流程：

```
Python

↓

Github API

↓

JSON数据

↓

Python dict

↓

打印结果
```

示例：

```python
get_github_user_info("openai")
```

返回：

```json
{
    "name":"OpenAI",
    "followers":128854,
    "public_repos":268
}
```

---

### 2. Weather API调用

使用：

Open-Meteo API

功能：

获取实时天气数据。

流程：

```
Python

↓

Weather API

↓

JSON

↓

解析天气信息
```

返回：

```json
{
    "temperature":26.8,
    "windspeed":15.4
}
```

---

# 项目结构

```
02-python-api

├── README.md

└── python-api-demo

    ├── main.py

    ├── github_api.py

    ├── weather_api.py

    ├── requirements.txt

    └── .gitignore

```

---

# 环境配置

创建虚拟环境：

```bash
python -m venv .venv
```

激活：

```powershell
.\.venv\Scripts\activate
```

安装依赖：

```bash
pip install requests python-dotenv
```

运行：

```bash
python python-api-demo/main.py
```

---

# 今日产出

完成：

* [x] requests环境配置
* [x] GET请求
* [x] POST请求
* [x] JSON解析
* [x] Header学习
* [x] Token认证基础
* [x] Github API调用
* [x] Weather API调用
* [x] Python API Demo项目

---

# 学习总结

Day02主要学习 Python 如何与外部世界通信。

通过 API 调用，实现：

```
Python程序

↓

调用外部服务

↓

获取数据

↓

处理结果

```

这是 AI 应用开发的重要基础。

后续学习：

Day03 - FastAPI

目标：

将 Python 程序封装成自己的 Web API。

# 遇到的问题与解决方案

## 问题1：安装依赖后无法导入 python-dotenv

### 问题现象

执行：

```bash
pip install python-dotenv
```

显示：

```
Requirement already satisfied: python-dotenv
```

但是运行程序：

```bash
python github_api.py
```

出现：

```
ModuleNotFoundError:
No module named 'dotenv'
```

### 原因分析

电脑中存在多个 Python 环境。

安装依赖时使用的是：

```
Anaconda Python
```

安装位置：

```
G:\pycham\anaconda\lib\site-packages
```

但是运行代码使用的是：

```
Python312
```

运行路径：

```
C:\Users\86138\AppData\Local\Programs\Python\Python312
```

两个 Python 环境不同，导致：

```
安装环境 != 运行环境
```

### 解决方案

为当前项目创建独立虚拟环境：

```bash
python -m venv .venv
```

激活：

```powershell
.\.venv\Scripts\activate
```

重新安装依赖：

```bash
pip install requests python-dotenv
```

之后使用：

```bash
python main.py
```

运行项目。

### 学习总结

Python项目应该遵循：

```
项目

↓

虚拟环境

↓

项目依赖

↓

requirements.txt
```

避免不同项目之间产生依赖冲突。

---

# 问题2：ImportError 模块函数不存在

## 问题现象

运行：

```bash
python main.py
```

出现：

```
ImportError:
cannot import name 'get_github_user'
```

以及：

```
ImportError:
cannot import name 'get_weather'
```

### 原因分析

`main.py` 中导入：

```python
from github_api import get_github_user
```

但是：

`github_api.py` 中实际定义：

```python
def get_github_user_info():
```

函数名称不一致。

同样：

`weather_api.py` 中定义：

```python
def get_weather_info():
```

但是：

`main.py` 导入：

```python
from weather_api import get_weather
```

导致 Python 无法找到对应函数。

### 解决方案

统一模块接口名称。

例如：

github_api.py:

```python
def get_github_user_info():
    pass
```

weather_api.py:

```python
def get_weather():
    pass
```

main.py:

```python
from github_api import get_github_user_info
from weather_api import get_weather
```

### 学习总结

Python项目中：

文件名、函数名、导入名称必须保持一致。

推荐开发习惯：

```
模块文件

↓

提供明确函数接口

↓

main.py负责调用
```

例如：

```
github_api.py

    get_github_user_info()


weather_api.py

    get_weather()


main.py

    调用业务逻辑
```

---

# 今日开发经验总结

通过 Day02 项目，理解了真实 Python 工程开发流程：

```
创建项目

↓

配置虚拟环境

↓

安装依赖

↓

编写模块

↓

调用外部API

↓

处理JSON数据

↓

调试错误

↓

提交Git
```

遇到错误并解决的过程，也是工程能力提升的重要部分。
