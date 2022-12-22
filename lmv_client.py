import json

import requests


rootURL = "https://api.discogs.com/database/search?artist=Heptones&format=LP&type=master"
rootURL = "https://api.discogs.com/releases/3721310"

response = requests.get(
        rootURL,
        headers={'Authorization': 'Discogs token=AugrlbeikovAiGkBIqufmThyfiuRkyNboopdSFWD'})
print(response.json()['images'])
print("Names:", ",".join(x["uri"] for x in response.json()['images'] if x["type"] == "primary"))
ja = [x["uri"] for x in response.json()['images'] if x["type"] == "primary"][0]
print(ja)
#res = [image['uri'] for image in response.json()['images'] if 'type:primary' in image['members']]

