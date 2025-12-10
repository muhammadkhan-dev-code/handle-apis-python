import requests
def fetch_random_user():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response= requests.get(url)
    data = response.json()

    if data['success'] and "data" in data:
        user_data=data['data']
        username=user_data["login"]["username"]
        country= user_data["location"]["country"]
        return f"Username: {username}, Country: {country}"
    else:
        raise Exception("Failed to fetch user data")

def main():
    try:
        userinfo= fetch_random_user()
        print(f"\n Fetched User -{userinfo}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

    
