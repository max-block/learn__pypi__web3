import json
import os

from dotenv import load_dotenv
from web3 import Web3

load_dotenv()


def get_token_abi():
    with open("./token_abi.json") as f:
        return json.load(f)


def main():
    rpc_url = os.getenv("RPC_URL")
    user_address = Web3.toChecksumAddress(os.getenv("ADDRESS"))
    token_address = Web3.toChecksumAddress(os.getenv("TOKEN_ADDRESS"))
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    contract = w3.eth.contract(token_address, abi=get_token_abi())
    raw_balance = contract.functions.balanceOf(user_address).call()
    print(raw_balance)


if __name__ == "__main__":
    main()
