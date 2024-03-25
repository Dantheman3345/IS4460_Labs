import requests
import json

api_url = 'http://localhost:8000/api/customers/'

customer_data = {
    "name": "Customer X",
    "email": 'customerx@example.com',
    "phone_number": "8014445555"
}
response = requests.post(url = api_url, data=json.dumps(customer_data),headers={'Content-Type':'application/json'})

if response.status_code == 201:
    print("Customers created sucessfully.")
else:
    print(f"Error creating customers.")