import requests

token_url = 'http://localhost:8000/api-token-auth/'

credentials ={
    'username': 'viewcust',
    'password': 'abcdefghijk',
}

response = requests.post(token_url, data=credentials)

print (response.json())