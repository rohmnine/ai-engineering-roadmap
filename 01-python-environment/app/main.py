import requests
def test_request():
    response = requests.get(
        "https://www.bing.com"
    )

    print(response.status_code)

if __name__ == "__main__":
    test_request()