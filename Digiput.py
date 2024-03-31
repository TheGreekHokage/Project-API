import pandas as pd
import requests
from sympy import *

api_url = "https://digimoncard.io/api-public/getAllCards.php?sort=name&series=Digimon%20Card%20Game&sortdirection=asc"
BASE = "http://127.0.0.1:5000/"
APP_VERSION = "v1/"


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
    # Process fetched data
    for i, item in enumerate(
        data[:33]
    ):  # Limiting to the first 33 items, consider removing this limit
        monster_data = {
            "id": item["cardnumber"],
            "attack": 0,
            "name": item["name"],
            "hp": 0,
        }
        # Send processed data to another endpoint for storage
        try:
            response = requests.put(
                BASE + APP_VERSION + "monster/" + str(i), json=monster_data
            )
            print(response.json())  # Print response from storage endpoint
        except Exception as e:
            print("Error storing data:", e)
else:
    print("Failed to fetch data from API")

# Fetch data for monster 2000
response = requests.get(BASE + APP_VERSION + "monster/2000")
print(response.json())
