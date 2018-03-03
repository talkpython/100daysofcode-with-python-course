#!python3

import json
import requests
from pprint import pprint

r = requests.get('https://us.api.battle.net/wow/character/Cenarion%20Circle/Ardy?fields=mounts&locale=en_US&apikey=')

data = json.loads(r.text)

for item in data.items():
    print(item)

#Hard to read

for item in data.items():
    pprint(item)

#easier to read
