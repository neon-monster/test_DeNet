from web3 import Web3


# w3 = Web3(Web3.HTTPProvider("https://polygon-rpc.com/"))
# w3 = Web3(Web3.HTTPProvider("https://polygon.technology/"))



token_addr = "0xC1c1afd7277Efc1c5195243A3C00B92c1F65Cb60"     
acc_address = "0x51f1774249Fc2B0C2603542Ac6184Ae1d048351d"        

w3 = Web3(Web3.HTTPProvider(
    f"https://api.polygonscan.com/api?module=contract&action=getabi&address=0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270&apikey={token_addr}"))

simplified_abi = [
    {
        'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}],
        'name': 'balanceOf',
        'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
        'stateMutability': 'view', 'type': 'function', 'constant': True
    },
    {
        'inputs': [],
        'name': 'decimals',
        'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}],
        'stateMutability': 'view', 'type': 'function', 'constant': True
    },
    {
        'inputs': [],
        'name': 'symbol',
        'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}],
        'stateMutability': 'view', 'type': 'function', 'constant': True
    },
    {
        'inputs': [],
        'name': 'totalSupply',
        'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
        'stateMutability': 'view', 'type': 'function', 'constant': True
    }
]

contract = w3.eth.contract(abi=simplified_abi)
symbol = contract.functions.symbol()
decimals = contract.functions.decimals()
totalSupply = contract.functions.totalSupply() / 10**decimals
addr_balance = contract.functions.balanceOf(acc_address).call() / 10**decimals

print("===== %s =====" % symbol)
print("Total Supply:", totalSupply)
print("Addr Balance:", addr_balance)

print(addr_balance)