import requests
import time
apikey = 'xxx' # 자기 api 키
header = { "X-Riot-Token": apikey}

def personal_key_get(URL):
    response = requests.get(URL, headers = header)
    time.sleep(1.2)
    return response