import requests

id = 1

api_url = f'http://localhost:8000/api/customers/{id}/'

response = requests.get(api_url)

if response.status_code ==200:
    customer_data = response.json()
    print(customer_data)
else:
    print("Error retrieving the customer")
