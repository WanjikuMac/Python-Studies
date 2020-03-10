import requests
import sys

phone = sys.argv

push = requests.post("http://ec2-99-81-80-152.eu-west-1.compute.amazonaws.com/sample.xml",
                        data = {"username": "pad_40130",
                                "to": phone, 
                                "from": "+254711082951"},
                          auth = ("apikey")  
                        )