from eth_abi import decode_abi
from eth_typing import HexStr
from eth_utils import to_bytes


def hex_to_bytes(data: str) -> bytes:
    return to_bytes(hexstr=HexStr(data))


tx_input = "6da024ca21cce9bcf08a8017e112adf70beb96b62b66c25a559598c65c5ddaea00000000000000000000000000000000000000000000000107ad8f556c6c0000000000000000000000000000000000000000000000000000ebec21ee1da40000"
abi = ["bytes32", "int256"]
res = decode_abi(abi, hex_to_bytes(tx_input))

print(res)

# 0x6da024ca21cce9bcf08a8017e112adf70beb96b62b66c25a559598c65c5ddaea