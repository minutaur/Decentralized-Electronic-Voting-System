import requests
import json

headers = {'Content-Type': 'application/json'}

data = {
    'question': 'Q1',
    'options': ['A1', 'A2', 'A3']
}

res = requests.get('http://127.0.0.1:5000/open', data=json.dumps(data), headers=headers)
print(res.text)
