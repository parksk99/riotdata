import requests
import json
import time
from riot_get import personal_key_get
URL = 'https://kr.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/{}/{}?page=1'

# 알아서 각자 티어 주석처리 해봐
bottom_tiers = ['GOLD','SILVER']
divisions = ['I','II','III','IV']

for bottom_tier in bottom_tiers:
    for division in divisions:
        response = personal_key_get(URL.format(bottom_tier, division)).json()
        with open('summoners/{}_{}.json'.format(bottom_tier,division),'w') as file:
            json.dump(response, file, indent = 4)