#Need to install requests and json package for python
import requests
import json

# Set authentication parameters: api_id and api_key
api_id = '<API ID>'
api_key = '<API KEY>'

# Set the request url and parameters
url = 'https://my.imperva.com/api/prov/v1/sites/configure?site_id=<Site ID>&param=site_ip&value=<Public IP>'

# Set proper headers
headers = {
    "x-API-Id": api_id,
    "x-API-Key": api_key,
    "Content-Type":"application/json",
    "Accept":"application/json"
}

params = {}
# Make the HTTP request
response = requests.post(url, data=json.dumps(params), headers=headers)

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()
# Decode the JSON response into a dictionary and use the data
data = response.json()
print(json.dumps(data))
