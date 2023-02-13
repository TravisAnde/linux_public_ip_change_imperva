# Need to install requests and json package for python
import requests
import json
from requests import get
 
# Get public IP
external_ip = get('https://api.ipify.org').content.decode('utf8')
  
# Set authentication parameters: api_id and api_key
api_id = '<insert_your_api_id_here>'
api_key = '<insert_your_api_key_here>'
 
# Set site id parameter
site_id = '<insert_your_site_id_here>'
 
# Set the request url and parameters
url = 'https://my.imperva.com/api/prov/v1/sites/configure?site_id={}&param=site_ip&value={}'.format(site_id, external_ip)
 
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
