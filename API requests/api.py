import requests
import json
from datetime import datetime
#make a simple get request to an API that doen't exist 
response1 = requests.get("http://api.open-notify.org/this-api-doesn't-exist")

#make an api request to an existing API which doesn't require query parameters
response = requests.get("http://api.open-notify.org/astros.json")
#status code 200 is everything is fine, code 404 the server wasn't found
print(response.status_code)
print(response.json())

def jprint(obj):
    #dumps prints a formatted string that makes it easier to understand the json output
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

print(response.json())

#make an API request with params
parameters = {
    "lat": 40.71,
    "lon": -74 
}

#This endpoint tells us the next times that the international space station will pass over a given location on the earth
response = requests.get("http://api.open-notify.org/iss-pass.json", parameters)
jprint(response.json())

#dates printed in this are in epoch format 
pass_times =response.json()['response']
jprint(pass_times)


durations =[]
for z in pass_times:
    dur = z['duration']
    durations.append(dur)

print(durations)

risetimes = []
for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

print(risetimes)

#convert dates to timestamps and put them in a list
times = []

for rt in risetimes:
    time =datetime.fromtimestamp(rt)
    times.append(time)
    print(time)