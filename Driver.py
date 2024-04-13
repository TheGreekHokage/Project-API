import requests
import csv
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
# YugiPut
import pandas as pd
import requests

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


# Fetch data from the Yu-Gi-Oh! API
# api_url = "https://db.ygoprodeck.com/api/v7/cardinfo.php?fname=Wizard&attribute=light&race=spellcaster"
# data = fetch_data_from_api(api_url)
import numpy as np


api_url = "https://db.ygoprodeck.com/api/v7/cardinfo.php?archetype=Blue-Eyes"
data = fetch_data_from_api(api_url)

# remember to do this for the digimon and yugioh, so that we can have the same number of monsters for each to make this thing work well
if data:
    starting_id = 33
    num_monsters = 33
    monster_ids = [starting_id + i for i in range(num_monsters)]

    # Yugioh does not have an hp value so it is defaulted to 1000 for all the monsters, I also found the enumerate() func which allows me to create a list easily
    for i, item in enumerate(data["data"]):
        hp_value = item.get("hp", 1000)

        if i < len(monster_ids):
            monster_id = monster_ids[i]
            print(
                f"Processing monster ID: {monster_id} and monster name: {item.get('name')}"
            )
            endpoint = BASE + APP_VERSION + f"monster/{monster_id}"
            check_response = requests.get(endpoint)
            if check_response.status_code == 404:
                monster_data = {
                    "id": monster_id,
                    "attack": 0,
                    "name": item.get("name", ""),
                    "hp": hp_value,
                }
                response = requests.put(endpoint, json=monster_data)
                print(response.json())
else:
    print("Failed to fetch data from API")
# PokePut
import pandas as pd
import requests

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


api_url = "https://api.pokemontcg.io/v2/cards"
data = fetch_data_from_api(api_url)

# remember to do this for the digimon and yugioh, so that we can have the same number of monsters for each to make this thing work well
if data:
    starting_id = 67
    num_monsters = 33
    monster_ids = [starting_id + i for i in range(num_monsters)]

    for i, item in enumerate(data["data"]):
        hp_value = item.get("hp")
        if hp_value is not None:
            if i < len(monster_ids):
                monster_id = monster_ids[i]
                print(
                    f"Processing monster ID: {monster_id} and monster name: {item.get('name')}"
                )
                endpoint = BASE + APP_VERSION + f"monster/{monster_id}"
                check_response = requests.get(endpoint)
                if check_response.status_code == 404:
                    monster_data = {
                        "id": monster_id,
                        "attack": 0,
                        "name": item.get("name", ""),
                        "hp": hp_value,
                    }
                    response = requests.put(endpoint, json=monster_data)
                    print(response.json())
else:
    print("Failed to fetch data from API")
