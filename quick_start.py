# a simple python script that works out of the box with one dependency (requests)

import requests

url = "https://api.compasslabs.ai/v0/generic/balance/get"
data = {
    "chain": "ethereum:mainnet",
    "user": "0xb8340945eBc917D2Aa0368a5e4E79C849c461511",
    "token": "USDT"
}

response = requests.post(url, json=data)
print(response.json())
