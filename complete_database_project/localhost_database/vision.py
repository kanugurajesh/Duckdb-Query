# importing required libraries
import requests
import json

# Define the URL
url = 'http://127.0.0.1:8000/query'

# Load the JSON file
with open('example.json', 'r') as f:
    payload = json.load(f)

# Send the request to the API by using the POST method
response = requests.post(url, json=payload)

# assigns the json output to the json_output variable
json_output = json.loads(response.text)

# prints the json output

print(json_output)
