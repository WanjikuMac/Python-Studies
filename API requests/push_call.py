import requests
import sys

script, phone = sys.argv

assert len(sys.argv) == 2

headers = {"Content-Type": "application/x-www-form-urlencoded",
            "apikey": "AT's API Key"
            }

push = requests.post("https://voice.africastalking.com/call",
                        data = {
                                "username": "pad_40130",
                                "to": sys.argv[1], 
                                "from": "+254711082951"
                                }, headers=headers)

print(push)
print(push.text)