import requests
from web3 import HTTPProvider, Web3


# constants
ARBITRUM_MAINNET_RPC_URL="<YOUR_ARBITRUM_MAINNET_RPC_URL>"
PRIVATE_KEY="<YOUR_PRIVATE_KEY>"
WALLET_ADDRESS="<A_WALLET_ADDRESS>"
# get account
w3 = Web3(HTTPProvider(ARBITRUM_MAINNET_RPC_URL))
account = w3.eth.account.from_key(PRIVATE_KEY)
print(account.address)


# set an allowance of 3.14 USDT

url = "https://beta-api.compasslabs.ai/beta/v0/generic/allowance/set/arbitrum%3Amainnet"
headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}
data = {
    "sender": WALLET_ADDRESS,
    "call_data": {
        "token": "USDT",
        "contract_name": "UniswapV3Router",
        "amount": "3.14"
    }
}
response = requests.post(url, headers=headers, json=data)
print(response.json())




