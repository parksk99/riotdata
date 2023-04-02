import requests
import json
import time
import os
from riot_get import personal_key_get
URL = 'https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{}/ids?type=ranked&start=0&count=20'
file_names = os.listdir('puuids')
for filename in file_names:
    matchids = []
    with open('puuids/'+filename, 'r') as file:
        puuids = json.load(file)
        for puuid in puuids:
            response = personal_key_get(URL.format(puuid))
            if response.ok:
                matchids = matchids + response.json()
            else:
                print(response.status_code)
    with open('matchids/'+filename, 'w') as file:
        json.dump(matchids, file)