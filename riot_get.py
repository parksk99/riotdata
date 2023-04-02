import requests
apikey = 'RGAPI-fc64aeac-4229-4ff9-bbe6-503820f1a51f' # 자기 api 키
header = { "X-Riot-Token": apikey}

def personal_key_get(URL):
    response = requests.get(URL, headers = header)
    time.sleep(1.2)
    return response