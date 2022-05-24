from json_conv import pred_dict
import json
import requests
import tester
url = 'http://0.0.0.0:8080/predict'
r = requests.get(url, json=pred_dict)

print(r.json())
