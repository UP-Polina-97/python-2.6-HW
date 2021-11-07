import requests
import json

def yandex_disk_folder():
    url = "https://cloud-api.yandex.net:443/"
    url_extra_folder = "v1/disk/resources"
    token = 'AQAAAABXPW06AAdM1-YiAlNVtE3xk5EvzmZuI7U'
    headers = {
        'accept': 'application/json',
        'authorization': f'OAuth {token}'}
    puting = requests.put(url + url_extra_folder, headers=headers, params={'path': 'photos'})
    return puting

print(yandex_disk_folder())