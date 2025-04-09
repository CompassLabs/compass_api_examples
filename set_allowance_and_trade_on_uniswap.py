import requests
from web3 import HTTPProvider, Web3
import time

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
url = "https://api.compasslabs.ai/v0/generic/allowance/set"
data = {
    "chain": "arbitrum:mainnet",
    "sender": WALLET_ADDRESS,
    "token": "USDT",
    "contract_name": "UniswapV3Router",
    "amount": "3.14"
}

# Send POST request to set allowance
response = requests.post(url, json=data)
# Print the API response
print("allowance response")

# Extract transaction data from the API response
allowance_transaction = response.json()

# Sign the transaction using the private key
allowance_signed_transaction = w3.eth.account.sign_transaction(allowance_transaction, PRIVATE_KEY)
# Send the signed transaction to the network
transaction_hash = w3.eth.send_raw_transaction(allowance_signed_transaction.raw_transaction)
# Print the transaction hash
print(transaction_hash.hex())




time.sleep(0.1) # wait for the allowance the previous transaction to be broadcasted to the arbitrum network



# Execute a trade using Uniswap
# Endpoint for executing a token swap
url = "https://api.compasslabs.ai/v0/uniswap/swap/sell_exactly"

data = {
    "chain":"arbitrum:mainnet",
    "sender": WALLET_ADDRESS,  # Address of the sender initiating the trade
    "token_in": "USDC",  # Token to sell
    "token_out": "USDT",  # Token to receive
    "fee": "0.01",  # Transaction fee percentage
    "amount_in": 1.5,  # Amount of USDT to sell
    "amount_out_minimum": 1.4,  # Minimum amount of USDC to receive
    "wrap_eth": True  # Whether to wrap ETH in the process
}
# Send POST request to initiate the trade
response = requests.post(url, json=data)

# Print the status code and API response
print(response.status_code)
print(response.json())

# Extract transaction data from the API response
uniswap_transaction = response.json()

# Sign the transaction using the private key
uniswap_signed_transaction = w3.eth.account.sign_transaction(uniswap_transaction, PRIVATE_KEY)
# Send the signed transaction to the network
transaction_hash = w3.eth.send_raw_transaction(uniswap_signed_transaction.raw_transaction)
# Print the transaction hash
print(transaction_hash.hex())




