import requests

id = 1

api_url = f'http://localhost:8000/api/orders/{id}/'

response = requests.get(api_url)

if response.status_code == 200:
    order_data = response.json()
    print(order_data)
else:
    print("Error retrieving the order.")
