import requests
import json
import time
import os
from riot_get import personal_key_get
tier = [['SILVER_II.json', 'IRON_III.json', 'PLATINUM_II.json', 'SILVER_I.json', 'GOLD_III.json', 'BRONZE_IV.json', 'DIAMOND_IV.json'],
    ['DIAMOND_II.json', 'BRONZE_III.json', 'GOLD_I.json', 'IRON_II.json', 'PLATINUM_III.json', 'PLATINUM_IV.json', 'DIAMOND_I.json'], 
    ['GRANDMASTER_I.json', 'CHALLENGER_I.json', 'SILVER_III.json', 'PLATINUM_I.json', 'GOLD_II.json', 'GOLD_IV.json', 'MASTER_I.json'],
    ['BRONZE_I.json', 'SILVER_IV.json', 'IRON_IV.json', 'BRONZE_II.json', 'DIAMOND_III.json', 'IRON_I.json']]
def remove_duplication():
    file_names = os.listdir('matchids')
    for file_name in file_names:
        print(file_name)
        with open('matchids/{}'.format(file_name), 'r') as file:
            matchids = json.load(file)
            print('before', len(matchids))
            matchids = set(matchids)
        with open('matchids_nodup/{}'.format(file_name), 'w') as file:
            print('after', len(matchids))
            matchids = list(matchids)
            json.dump(matchids, file)
def getMatch(index):
    URL = 'https://asia.api.riotgames.com/lol/match/v5/matches/{}'
    for file_name in tier[index]:
        print(file_name)
        with open('matchids_nodup/{}'.format(file_name),'r') as file:
            matchids = json.load(file)
            for matchid in matchids:
                response = personal_key_get(URL.format(matchid))
                if response.status_code != 200:
                    print(response.status_code)
                else:
                    if not os.path.exists('matchs/{}'.format(file_name)):
                        os.makedirs('matchs/{}'.format(file_name))
                    with open('matchs/{}/{}'.format(file_name, matchid), 'w') as file:
                        json.dump(response.json(), file)

getMatch(3)