import requests
import json

headers = {'Content-Type': 'application/json'}

data = {
    'id': ['id'],
    'vote': ['vote']
}

res = requests.post('http://127.0.0.1:5000/vote', data=json.dumps(data), headers=headers)

print(res.text)
