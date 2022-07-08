from json_conv import pred_dict
import json
import requests
import tester
url = 'http://127.0.0.1:5000/predict'
r = requests.post(url, json=pred_dict)

print(r.json())
