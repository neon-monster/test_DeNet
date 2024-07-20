from flask import Flask, request, jsonify
from web3 import Web3

# Сделано при помощи AI
app = Flask(__name__)

# Подключение к сети Polygon
polygon_rpc_url = "https://polygon-rpc.com/"
web3 = Web3(Web3.HTTPProvider(polygon_rpc_url))


# Адрес токена и ABI
token_address = "0x1a9b54a3075119f1546c52ca0940551a6ce5d2d0"
erc20_abi = [
    {
        "constant": True,
        "inputs": [],
        "name": "name",
        "outputs": [{"name": "", "type": "string"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "symbol",
        "outputs": [{"name": "", "type": "string"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [{"name": "owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
]

# Создание контракта токена
token_contract = web3.eth.contract(address=token_address, abi=erc20_abi)

# Уровень A: Получение баланса выбранного адреса
@app.route('/get_balance', methods=['GET'])
def get_balance():
    address = request.args.get('address')
    balance = token_contract.functions.balanceOf(address).call()
    decimals = token_contract.functions.decimals().call()
    formatted_balance = balance / (10 ** decimals)
    return jsonify({"balance": formatted_balance})

# Уровень B: Получение балансов нескольких адресов сразу
@app.route('/get_balance_batch', methods=['POST'])
def get_balance_batch():
    addresses = request.json.get('addresses')
    balances = []
    for address in addresses:
        balance = token_contract.functions.balanceOf(address).call()
        decimals = token_contract.functions.decimals().call()
        formatted_balance = balance / (10 ** decimals)
        balances.append(formatted_balance)
    return jsonify({"balances": balances})

# Уровень C: Получение топ адресов по балансам токена
@app.route('/get_top', methods=['GET'])
def get_top():
    # Для упрощения, здесь просто возвращаем фиксированные адреса и балансы
    # В реальном приложении вам нужно будет реализовать логику получения топовых адресов
    top_addresses = [
        ("0xAddress1", 10000000000000000),
        ("0xAddress2", 5000000000000000),
        ("0xAddress3", 2500000000000000),
    ]
    return jsonify(top_addresses)

# Уровень D: Получение топ адресов с датами последних транзакций
@app.route('/get_top_with_transactions', methods=['GET'])
def get_top_with_transactions():
    # Аналогично, здесь просто фиксированные данные
    top_with_transactions = [
        ("0xAddress1", 10000000000000000, "2024-07-20"),
        ("0xAddress2", 5000000000000000, "2024-07-19"),
        ("0xAddress3", 2500000000000000, "2024-07-18"),
    ]
    return jsonify(top_with_transactions)

# Уровень E: Получение информации о токене
@app.route('/get_token_info', methods=['GET'])
def get_token_info():
    name = token_contract.functions.name().call()
    symbol = token_contract.functions.symbol().call()
    total_supply = token_contract.functions.totalSupply().call()
    decimals = token_contract.functions.decimals().call()
    formatted_supply = total_supply / (10 ** decimals)
    return jsonify({"symbol": symbol, "name": name, "totalSupply": formatted_supply})

# Уровень F: Запуск сервера
if __name__ == "__main__":
    app.run(host='192.168.0.1', port=8080)
