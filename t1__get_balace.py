import os

from dotenv import load_dotenv
from web3 import Web3

load_dotenv()


def main():
    rpc_url = os.getenv("RPC_URL")
    address = os.getenv("ADDRESS")
    address = Web3.toChecksumAddress(address)
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    balance = w3.eth.get_balance(address)  # in gwei
    balance = Web3.fromWei(balance, "ether")  # in ETH
    print(balance)


if __name__ == "__main__":
    main()
