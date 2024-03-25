import requests
import json

api_url = 'http://localhost:8000/api/orders/'

order_data = {
    "title": "Sample Order",
    "description": "This is a sample order description.",
    "status": "pending"
}
response = requests.post(url=api_url, data=json.dumps(order_data), headers={'Content-Type': 'application/json'})

if response.status_code == 201:
    print("Order created successfully.")
else:
    print(f"Error creating order. Status Code: {response.status_code}")
