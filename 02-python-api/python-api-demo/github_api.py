import requests

def get_github_user(username):
    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
          "name":data["name"],
          "followers":data["followers"],
          "public_repos":data["public_repos"]
        }
    else:
        return None

user = get_github_user("openai")

print(user)