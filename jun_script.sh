#!/bin/sh
mkdir matchids

rm puuids/CHAL*.json
rm puuids/GRAND*.json
rm puuids/MAS*.json
rm puuids/DIA*.json
rm puuids/PLA*.json
rm puuids/GOLD*.json
rm puuids/SI*.json
# rm puuids/BRON*.json
# rm puuids/IRON*.json
python get_matchid.py
