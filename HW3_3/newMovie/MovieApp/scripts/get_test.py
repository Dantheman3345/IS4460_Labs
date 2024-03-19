import requests
import json

resp = requests.get('http://127.0.0.1:8000/api/movies/')
print(resp.status_code)
print(resp.text)