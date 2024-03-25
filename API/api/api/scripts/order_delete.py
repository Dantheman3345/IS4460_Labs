import requests

id = 1
api_url = f'http://localhost:8000/api/orders/{id}/'

response = requests.delete(url=api_url)

if response.status_code == 204:
    print("Order deleted successfully.")
else:
    print(f"Error deleting the Order.")
