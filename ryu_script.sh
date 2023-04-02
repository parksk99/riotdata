#!/bin/sh
mkdir matchids

rm puuids/CHAL*.json
rm puudis/GRAND*.json
rm puuids/MAS*.json
# rm puudis/DIA*.json
# rm puuids/PLA*.json
rm puuids/GOLD*.json
rm puuids/SI*.json
rm puuids/BRON*.json
rm puuids/IRON*.json

python get_matchid.py