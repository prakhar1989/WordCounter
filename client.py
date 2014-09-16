import requests
import json
import time
from collections import Counter

URL = "http://192.241.186.225/"
# URL = "http://127.0.0.1:8000/"

def get_count(text, words_excluded):
    cnt = Counter()
    for word in text.split():
        if word not in words_excluded:
            cnt[word] += 1
    return dict(cnt)

def get_request():
    try:
        r = requests.get(URL)
    except:
        print "Err: Unable to connect to the server."
        return

    data = r.json()
    count = get_count(data.get('text'), data.get('words'))
    request_data = {"words" : count,
                    "text"  : data.get("text"),
                    "token" : data.get("token")}
    headers = {'content-type': 'application/json'}
    r = requests.post(URL + "validate", data=json.dumps(request_data), headers=headers)
    print "Text:", data.get('text')[:30] + "...", "Status Code:", r.status_code

if __name__ == "__main__":
    count = 10
    print "Hitting %s requests ..." % count
    get_request()
    for i in range(count):
        get_request()
        time.sleep(2)

