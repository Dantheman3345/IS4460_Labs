import requests
import json

id = 1
api_url = f'http://localhost:8000/api/customers/{id}/'

customer_data = {
    "name": "Customer D",
    "email": 'customerx@update.com',
    "phone_number": "8016666666"
}
response = requests.put(url = api_url, data=json.dumps(customer_data),headers={'Content-Type':'application/json'})

if response.status_code == 200:
    print("Customers updated sucessfully.")
else:
    print(f"Error Updating Customers.")