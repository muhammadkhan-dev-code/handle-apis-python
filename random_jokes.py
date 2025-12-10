import requests

def fetch_random_joke(url):
    response= requests.get(url)
    if response.status_code == 200:
        data= response.json()
        if data["success"] and "data" in data:
            joke_data= data["data"]["data"]
            for joke in joke_data:
                print(f"id: {joke['id']} \n joke : {joke['content']}")
            return joke_data[0]["id"], joke_data[0]["content"]
        else:
            raise Exception("Failed to fetch joke data")   
def main():
    try:
        joke_url="https://api.freeapi.app/api/v1/public/randomjokes"
        fetch_random_joke(joke_url)
        # for joke in joke_data:
        #  print(joke)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

