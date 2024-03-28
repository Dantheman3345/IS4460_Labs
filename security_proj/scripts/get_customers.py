import requests

api_url = 'http://localhost:8000/api/customers/'

token = 'f1ffc6e4042e68a502f4d8254cc9f6f36df831f6'

headers = {
    'Authorization': f'Token {token}'
}
response = requests.get(api_url,headers=headers)

print(response.status_code)

if response.status_code == 200:
    print(f'Customers retrieval successful. {response.text}')
else:
    print(f'Customers retrieval failed. {response.text}')