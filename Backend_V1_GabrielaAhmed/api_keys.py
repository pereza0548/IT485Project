import requests
import json
url = 'https://api.petfinder.com/v2/oauth2/token'
data = {
    "grant_type": "client_credentials",
    "client_id": "Key",
    "client_secret": "Secret"
}

response = requests.post(url, data=data)

# Parse the JSON response
response_json = response.json()

# Extract the access_token
access_token = response_json['access_token']

CALL_URL = 'https://api.petfinder.com/v2/animals'