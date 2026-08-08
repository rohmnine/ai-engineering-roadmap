import requests

response = requests.post(
    "http://127.0.0.1:8000/chat",
    json={"text": "", "user": "Tom", "time": "2027-06-01 10:00:00"}
)

print(response.json())