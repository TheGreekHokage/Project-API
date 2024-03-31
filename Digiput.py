import requests
from sympy import *

BASE = "http://127.0.0.1:5000/"
APP_VERSION = "v1/"


def fetch_data_from_api(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None


api_url = "https://digimoncard.io/api-public/getAllCards.php?sort=name&series=Digimon%20Card%20Game&sortdirection=asc"
data = fetch_data_from_api(api_url)
# There are over 2000 digimon so I had to lower the number pulled. For the other APIs I just pulled from smaller pools for this one, they
# only had the option to either select one or all the cards from the api url. I also found the enumerate() function that allows me to list of tuples which helped me see what I was pulling in early stages
if data:
    for i, item in enumerate(data[:33]):
        monster_data = {
            "id": item["cardnumber"],
            "attack": 0,
            "name": item["name"],
            "hp": 0,
        }
        response = requests.put(
            BASE + APP_VERSION + "monster/" + str(i), json=monster_data
        )  # Using json parameter to send JSON data
        print(response.json())
else:
    print("Failed to fetch data from API")

# Since over 2000 cards in this API I will test the 2000s
response = requests.get(BASE + APP_VERSION + "monster/2000")
print(response.json())
