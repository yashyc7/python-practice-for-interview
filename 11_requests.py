import requests


def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url, timeout=10)
    except requests.exceptions.RequestException as e:
        print("Request failed : ", e)
        return

    users = response.json()

    for user in users:
        print(f"{user['name']} | {user['email']} | {user['address']['city']}")


fetch_users()
