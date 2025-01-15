import requests
from web3 import HTTPProvider, Web3
import time

# loading secrets from .env
from dotenv import load_dotenv
load_dotenv()
# RPC URL for connecting to the Arbitrum mainnet
ARBITRUM_MAINNET_RPC_URL=os.environ["ARBITRUM_MAINNET_RPC_URL"]
# private key for signing transactions (keep this secure)
PRIVATE_KEY=os.environ["PRIVATE_KEY"]
# wallet address of the sender
WALLET_ADDRESS="<PUT_YOUR_WALLET_ADDRESS_HERE>"

# Initialize Web3 connection to the Arbitrum mainnet
w3 = Web3(HTTPProvider(ARBITRUM_MAINNET_RPC_URL))
# Retrieve account object from private key
account = w3.eth.account.from_key(PRIVATE_KEY)
# Print the address of the account
print(account.address)

# Set an allowance of 3.14 USDT
# Endpoint for setting token allowance
url = "https://beta-api.compasslabs.ai/beta/v0/generic/allowance/set/arbitrum%3Amainnet"
headers = {
    "accept": "application/json",  # Specify the response format
    "Content-Type": "application/json"  # Specify the request payload format
}
data = {
    "sender": WALLET_ADDRESS,  # Address of the sender setting the allowance
    "call_data": {
        "token": "USDT",  # Token to set allowance for
        "contract_name": "UniswapV3Router",  # Contract name to interact with
        "amount": "3.14"  # Allowance amount in USDT
    }
}
# Send POST request to set allowance
response = requests.post(url, headers=headers, json=data)
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
url = "https://beta-api.compasslabs.ai/beta/v0/uniswap/swap/sell_exactly/arbitrum%3Amainnet"

headers = {
    "accept": "application/json",  # Specify the response format
    "Content-Type": "application/json"  # Specify the request payload format
}

data = {
    "sender": WALLET_ADDRESS,  # Address of the sender initiating the trade
    "call_data": {
        "token_in": "USDT",  # Token to sell
        "token_out": "USDC",  # Token to receive
        "fee": "0.01",  # Transaction fee percentage
        "amount_in": 1.5,  # Amount of USDT to sell
        "amount_out_minimum": 1.4,  # Minimum amount of USDC to receive
        "wrap_eth": True  # Whether to wrap ETH in the process
    }
}
# Send POST request to initiate the trade
response = requests.post(url, headers=headers, json=data)

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




