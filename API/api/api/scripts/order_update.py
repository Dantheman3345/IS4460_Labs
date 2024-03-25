import requests
import json

id = 1
api_url = f'http://localhost:8000/api/orders/{id}/'

order_data = {
    "title": "Updated Order Title",
    "description": "Updated order description.",
    "status": "updated"
}
response = requests.put(url=api_url, data=json.dumps(order_data), headers={'Content-Type': 'application/json'})

if response.status_code == 200:
    print("Order updated successfully.")
else:
    print(f"Error Updating Order.")
