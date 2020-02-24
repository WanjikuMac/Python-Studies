import requests
import json
#make a simple get request to an API that doen't exist 
response1 = requests.get("http://api.open-notify.org/this-api-doesn't-exist")

#make an api request to an existing API which doesn't require query parameters
response = requests.get("http://api.open-notify.org/astros.json")
#status code 200 is everything is fine, code 404 the server wasn't found
print(response.status_code)
print(response.json())

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())

#make an API request with params
parameters = {
    "lat": 40.71,
    "lon": -74 
}

response = requests.get("http://api.open-notify.org/iss-pass.json", parameters)
jprint(response.json())

