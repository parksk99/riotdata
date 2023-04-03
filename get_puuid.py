import requests
import json
import time
import os
from riot_get import personal_key_get

URL = 'https://kr.api.riotgames.com/lol/summoner/v4/summoners/{}'

files = os.listdir('summoners')
for file in files:
    print(file)
    with open('summoners/'+file, 'r') as f:
        summoners = json.load(f)
    puuids = []
    for summoner in summoners:
        if summoner['freshBlood'] == False:
            summonerId = summoner['summonerId']
            response = personal_key_get(URL.format(summonerId))
            if response.status_code != 200:
                print(response)
            response = response.json()
            puuids.append(response['puuid'])
    with open('puuids/'+file, 'w') as f:
        json.dump(puuids, f)