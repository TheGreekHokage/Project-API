import requests
from sympy import *

api_url = "https://digimoncard.io/api-public/getAllCards.php?sort=name&series=Digimon%20Card%20Game&sortdirection=asc"


# Define fetch_data_from_api function if not already defined
def fetch_data_from_api(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        print("Error fetching data from API:", e)
        return None


data = fetch_data_from_api(api_url)

if data:
    for i, item in enumerate(data):
        monster_data = {
            "id": item["cardnumber"],
            "attack": 0,
            "name": item["name"],
            "hp": 0,
        }
        try:
            response = requests.put(
                BASE + APP_VERSION + f"monster/{i}", json=monster_data
            )
            if response.status_code == 200:
                print(response.json())
            else:
                print("Failed to store data for monster", i)
        except Exception as e:
            print("Error storing data for monster", i, ":", e)
else:
    print("Failed to fetch data from API")

# Test fetching data for monster 2000
try:
    response = requests.get(BASE + APP_VERSION + "monster/2000")
    if response.status_code == 200:
        print(response.json())
    else:
        print("Failed to fetch data for monster 2000")
except Exception as e:
    print("Error fetching data for monster 2000:", e)
