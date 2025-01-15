import requests
from web3 import HTTPProvider, Web3
import os



# constants
# loading secrets from .env
import os
from dotenv import load_dotenv
load_dotenv()
ARBITRUM_MAINNET_RPC_URL=os.environ["ARBITRUM_MAINNET_RPC_URL"]
PRIVATE_KEY=os.environ["PRIVATE_KEY"]
# wallet address
WALLET_ADDRESS=os.environ["WALLET_ADDRESS"]
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


# Extract transaction data from the API response
allowance_transaction = response.json()
print(allowance_transaction)


# Sign the transaction using the private key
allowance_signed_transaction = w3.eth.account.sign_transaction(allowance_transaction, PRIVATE_KEY)
# Send the signed transaction to the network
transaction_hash = w3.eth.send_raw_transaction(allowance_signed_transaction.raw_transaction)
# Print the transaction hash
print(transaction_hash.hex())



