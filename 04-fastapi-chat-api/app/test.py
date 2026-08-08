import requests

response = requests.post(
    "http://127.0.0.1:8000/chat",
    json={"text": "你好"}
)

print(response.json())