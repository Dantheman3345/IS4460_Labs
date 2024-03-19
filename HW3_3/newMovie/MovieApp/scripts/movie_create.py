import requests
import json


# Define the URL to your API endpoint for creating movies
api_url = "http://127.0.0.1:8000/api/movies"

# Create a dictionary with movie data
movie_data = {
    "title": "Example Movie",
    "description": "This is a description of the example movie.",
    "director": "John Doe",
    "release_year": "2023",
    "budget": "100",
    "runtime": "120",
    "rating": "5",
    "genre": "Drama",
    "image_url": "http://example.com/image.jpg",
    "youtube_url": "http://youtube.com/example"
}

# Send a POST request to the API endpoint with the movie data
response = requests.post(api_url, json=movie_data)

# Check the response status code
if response.status_code == 201:
    print("Movie created successfully.")
    # Optionally, print the response data
    print(response.json())
else:
    print(f"Failed to create movie. Status code: {response.status_code}")
    # Optionally, print the response text to understand what went wrong
    print(response.text)


