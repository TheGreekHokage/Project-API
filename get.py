import requests

BASE = "http://127.0.0.1:5000/"
APP_VERSION = "v1/"
# response = requests.get(BASE + APP_VERSION + "monster/66")
# print(response.json())

import random
import string


def generate_random_string(length):
    # Get all the ASCII letters in lowercase and uppercase
    letters = string.ascii_letters
    # Randomly choose characters from letters for the given length of the string
    random_string = "".join(random.choice(letters) for i in range(length))
    return random_string


# Example usage: generate a random string of length 10
# printing digits
letters = string.digits
a = "".join(random.choice(letters) for i in range(2))
print(a)

# now to test if I can make this app pick a number at random using the random # code generator
import requests

BASE = "http://127.0.0.1:5000/"
APP_VERSION = "v1/"
response = requests.get(BASE + APP_VERSION + "monster/" + a)
print(response.json())
