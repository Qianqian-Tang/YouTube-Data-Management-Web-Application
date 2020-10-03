import json
import requests

with open('file.json') as f:
  data = json.load(f)

for sub in data['USvideos']:
    for i in sub:
        if i=='category_id':

            sub[i]= int(sub[i])
        elif i=='views':

            sub[i]= int(sub[i])
        elif i=='likes':

            sub[i]= int(sub[i])
        elif i=='likes':

            sub[i]= int(sub[i])
        elif i=='dislikes':

            sub[i]= int(sub[i])
        elif i=='comment_count':

            sub[i]= int(sub[i])

url = 'https://web-group-proj.firebaseio.com/'
response = requests.put(url+'USvideos.json', json.dumps(data['USvideos'], indent=4, separators=(',', ':')))


