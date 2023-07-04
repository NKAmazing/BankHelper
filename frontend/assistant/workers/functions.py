import requests

def get_bank_name(bank_id):
    # Make the request GET to the API REST of the bank
    bank_url = f'http://localhost:8000/bank/get/{bank_id}'
    bank_response = requests.get(bank_url)
    bank = bank_response.json()
    bank_name = bank['bank_name']
    return bank_name

def get_account_number(account_id):
    # Make the request GET to the API REST of the bank
    account_url = f'http://localhost:8000/bank/get_account/{account_id}'
    account_response = requests.get(account_url)
    account = account_response.json()
    account_number = account['account_number']
    return account_number