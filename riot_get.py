import requests
import time
apikey = 'RGAPI-46244d47-7b6d-4799-af39-3522ddb23683' # 자기 api 키
header = { "X-Riot-Token": apikey}

def personal_key_get(URL):
    response = requests.get(URL, headers = header)
    time.sleep(1.2)
    return response