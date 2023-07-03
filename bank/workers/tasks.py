from bank_helper.celery import app
from client.controllers import user_controller as user
import requests
from django.test import RequestFactory

# Here is the Celery tasks that will be executed

@app.task
def get_account_info(account_id):
    print('HOLA ESTOY EN GET ACCOUNT INFO')
    print('ESTO ES ACCOUNT ID: ', account_id)
    # Make the request GET to the API REST of the bank
    url = f'http://localhost:8000/bank/get_account/{account_id}'
    print('ESTO ES URL: ', url)
    response = requests.get(url)
    print('ESTO ES RESPONSE: ', response)
    result = response.json()
    print('ESTO ES RESULT: ', result)
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

@app.task
def update_account_balance(requests, account_id, new_balance, data):
    '''
    Function to update the balance of an account
    '''
    account_url = f'http://localhost:8000/bank/update_account/{account_id}'
    data = {
        'account_number': data['account_number'],
        'balance': new_balance
    }
    resp = requests.put(account_url, data=data)

@app.task
def search_user(email):
    '''
    Function to search a user by email
    '''
    # Set the url to make the request
    url = f"http://localhost:8000/client/get_user_by_email/{email}/"

    print("ESTO ES URL: ", url)

    # Make the request
    response = requests.get(url)

    print("ESTO ES RESPONSE: ", response)

    # Check if the user exists
    if response.status_code == 200:
        # Get the user
        user = response.json()

        # Check if the user exists
        if user is not None:
            return user
        else:
            return None
    else:
        return None