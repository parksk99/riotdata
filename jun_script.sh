#!/bin/sh
mkdir matchids
mkdir puuids
rm puuids/CHAL*.json
rm puuids/GRAND*.json
rm puuids/MAS*.json
rm puuids/DIA*.json
rm puuids/PLA*.json
rm puuids/GOLD*.json
rm puuids/SI*.json
# rm puuids/BRON*.json
# rm puuids/IRON*.json

rm summoners/CHAL*.json
rm summoners/GRAND*.json
rm summoners/MAS*.json
rm summoners/DIA*.json
rm summoners/PLA*.json
rm summoners/GOLD*.json
rm summoners/SI*.json
# rm summoners/BRON*.json
# rm summoners/IRON*.json
python get_puuid.py
python get_matchid.py
