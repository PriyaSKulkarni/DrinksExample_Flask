import requests;
import json;
import sys;
sys.stdout.reconfigure(encoding='utf-8')

response = requests.get("https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")
print(response.status_code)
data = response.json()['items']
#print(json.dumps(data['items'], ensure_ascii=False, indent=4))
for d in data:
    if d['answer_count'] == 0:
        print(d['link'])
