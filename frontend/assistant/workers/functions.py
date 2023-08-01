from decouple import config
import requests

def get_bank_name(bank_id):
    '''
    Function to get the bank name
    param:
        - bank_id: Id of the bank
    '''

    # Get the bank url
    bank_url = get_bank_url()

    # Make the request GET to the API REST of the bank
    url = f'{bank_url}/get/{bank_id}'
    bank_response = requests.get(url)
    bank = bank_response.json()
    bank_name = bank['bank_name']
    return bank_name

def get_account_number(account_id):
    '''
    Function to get the account number
    param:
        - account_id: Id of the account
    '''

    # Get the bank url
    bank_url = get_bank_url()

    # Make the request GET to the API REST of the bank
    account_url = f'{bank_url}/get_account/{account_id}'
    account_response = requests.get(account_url)
    account = account_response.json()
    account_number = account['account_number']
    return account_number

def get_bank_url():
    '''
    Function to get the bank url from the env file
    '''
    return config('BANK_URL')

def get_client_url():
    '''
    Function to get the client url from the env file
    '''
    return config('CLIENT_URL')

def get_server_url():
    '''
    Function to get the server url from the env file
    '''
    return config('SERVER_URL')