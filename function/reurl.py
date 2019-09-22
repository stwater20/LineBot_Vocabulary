import crawler

def reurl(url):
    data = {"url": url}
    headers = {'Content-type': 'application/json', 'reurl-api-key': '4070df69d794ea30114b353100ba214de0d3b6318d894494ab38acc62b055f6689'}
    response = requests.post(
        "https://api.reurl.cc/shorten", data=data_json, headers=headers)
    s = response.json()
    print(s['short_url'])
    return s['short_url']