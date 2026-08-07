import requests

def get_weather():

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
    "latitude": 37.9465,
    "longitude": 116.4,
    "current_weather": True
    }

    response = requests.get(url, params=params)

    data = response.json()

    return data["current_weather"]