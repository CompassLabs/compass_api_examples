# a simple python script that works out of the box with one dependency (requests)

import requests

url = "https://beta-api.compasslabs.ai/beta/v0/generic/balance/get/arbitrum%3Amainnet"
headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}
data = {
    "sender": "0xb8340945eBc917D2Aa0368a5e4E79C849c461511",
    "call_data": {
        "token": "USDT"
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
