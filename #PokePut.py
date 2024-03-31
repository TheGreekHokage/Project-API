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
