from bank_helper.celery import app
import requests

# Here is the Celery tasks that will be executed

@app.task
def get_account_info(account_id):
    # Make the request GET to the API REST of the bank
    url = f'http://localhost:8000/bank/get_account/{account_id}'
    response = requests.get(url)
    result = response.json()
    return result

@app.task
def make_transaction(account_id, amount, destination_account_id):
    # Make the request POST to the API REST of the bank
    url = 'http://localhost:8000/bank/create_transaction/'
    data = {
        'amount': amount,
        'source_account': account_id,
        'destination_account': destination_account_id,
        'status': 'CONFIRMMED'
    }
    response = requests.post(url, data=data)
    result = response.json()
    return result

@app.task
def show_transactions_list(account_id):
    # Make the request GET to the API REST of the bank
    url = f'http://localhost:8000/bank/get_transactions_by_source_account/{account_id}'
    response = requests.get(url)
    result = response.json()
    return result