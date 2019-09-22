import sys
import json
sys.path.append("../secret")
import requests
from secret import RE_api_key

def reurl(url):
    data = {"url": url}
    data_json = json.dumps(data)
    headers = {'Content-type': 'application/json', 'reurl-api-key': RE_api_key}
    response = requests.post(
        "https://api.reurl.cc/shorten", data=data_json, headers=headers)
    s = response.json()
    print(s['short_url'])
    return s['short_url']