import sys
sys.path.append("../secret")
import crawler
from secret import RE_api_key

def reurl(url):
    data = {"url": url}
    headers = {'Content-type': 'application/json', 'reurl-api-key': RE_api_key}
    response = requests.post(
        "https://api.reurl.cc/shorten", data=data_json, headers=headers)
    s = response.json()
    print(s['short_url'])
    return s['short_url']