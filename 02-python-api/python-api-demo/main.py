from github_api import get_github_user
from weather_api import get_weather

user = get_github_user("openai")
weather = get_weather()

print(user)

print(get_weather())