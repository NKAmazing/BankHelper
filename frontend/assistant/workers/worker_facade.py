from .functions import get_bank_name, get_account_number, get_bank_url, get_client_url, get_server_url
from decouple import config
import requests


class WorkerFacade:
    '''
    Class to handle the complexity of the assistant's tasks through the Facade pattern
    '''

    @staticmethod
    def get_account_info(account_id):

        # Get the bank url
        bank_url = get_bank_url()

        # Make the request GET to the API REST of the bank
        url = f'{bank_url}/get_account/{account_id}/'
        response = requests.get(url)
        # Get the account info
        account = response.json()

        # Get the bank id
        bank_id = account['bank']
        # Call the task get the bank name
        bank_name = get_bank_name(bank_id)

        result = {
            'account_id': account['id'],
            'account_number': account['account_number'],
            'balance': account['balance'],
            'bank': bank_name
        }

        return result

    @staticmethod
    def make_transaction(account_id, amount, destination_account_id):

        # Get the bank url
        bank_url = get_bank_url()

        # Make the request POST to the API REST of the bank
        url = f'{bank_url}/create_transaction/'
        data = {
            'amount': amount,
            'source_account': account_id,
            'destination_account': destination_account_id,
            'status': 'CONFIRMMED'
        }
        response = requests.post(url, data=data)
        result = response.json()
        return result

    @staticmethod
    def show_transactions_list(account_id):

        # Get the bank url
        bank_url = get_bank_url()

        # Make the request GET to the API REST of the bank
        url = f'{bank_url}/get_transactions_by_source_account/{account_id}'
        response = requests.get(url)
        transactions = response.json()

        for transaction in transactions:
            source_account_number = get_account_number(account_id)
            destination_account_id = transaction['destination_account']
            destination_account_number = get_account_number(destination_account_id)
            transaction['source_account'] = source_account_number
            transaction['destination_account'] = destination_account_number
        
        return transactions

    @staticmethod 
    def update_account_balance(account_id, new_balance, account_info):
        '''
        Function to update the balance of an account
        '''

        # Get the bank url
        bank_url = get_bank_url()

        account_url = f'{bank_url}/update_account/{account_id}/'

        data = {
            'id': account_info['id'],
            'account_number': account_info['account_number'],
            'balance': new_balance,
            'bank_id': account_info['bank']
        }
        resp = requests.put(account_url, data=data)
        if resp.status_code == 200:
            result = resp.json()
            return result
        else:
            print("STATUS: ", resp.status_code)
            print('Error updating the account balance')
            return None

    @staticmethod
    def search_user(email):
        '''
        Function to search a user by email
        '''

        # Get the client url
        client_url = get_client_url()

        # Set the url to make the request
        url = f"{client_url}/get_user_by_email/{email}/"

        # Make the request
        response = requests.get(url)

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