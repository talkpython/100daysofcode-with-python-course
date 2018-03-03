#!python3

import json
import requests
from pprint import pprint

r = requests.get('https://us.api.battle.net/wow/character/Cenarion%20Circle/Ardy?fields=mounts&locale=en_US&apikey=')

data = json.loads(r.text)

for item in data['mounts']:
    pprint(item)

#Only the first level is printed.

for item in data['mounts']['collected']:
    pprint(item)

#Prints ALL the data associated with 'collected mounts'.


for item in data['mounts']['collected']:
    pprint(item['name'])

#Prints just the data associated with the 'name' key.


is_flying = []
for mount in data['mounts']['collected']:
    if mount['isFlying']:
        is_flying.append(mount)

#Collects all of the applicable mounts and stores them as a list of dicts

#You can then work with the data as normal:

len(is_flying)
65

for i in is_flying:
    print(i)

for i in is_flying:
    print(i['name'])

