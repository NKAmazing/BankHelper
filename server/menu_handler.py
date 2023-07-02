from bank.workers.tasks import get_account_info
from bank.workers.tasks import make_transaction
from bank.workers.tasks import show_transactions_list
import json

# Class that handles the menu options

class MenuHandler:

    def handle_options(self, action, text_data_json):
        if action == 'send_menu':
            self.send_menu()
        elif action == 'get_account_info':
            result = self.handle_get_account_info(text_data_json)
        elif action == 'make_transaction':
            result = self.handle_make_transaction(text_data_json)
        elif action == 'show_transactions_list':
            result = self.handle_show_transactions_list(text_data_json)
        else:
            print('Error: Action does not exist')
            result = {'error': 'Action does not exist'}
        return result

    def send_menu(self):
        menu = {
            'action': 'send_menu',
            'options': [
                {'label': 'Show information account', 'value': 'get_account_info'},
                {'label': 'Make a transaction', 'value': 'make_transaction'},
                {'label': 'Show transaction history', 'value': 'show_transactions_list'}
            ]
        }
        self.send(text_data=json.dumps(menu))

    def handle_get_account_info(self, data):
        '''
        Handle method for the management of the action of obtaining the account information
        '''
        account_id = data['account_id']
        print('ESTO ES ACCOUNT ID: ', account_id)
        print('TIPO DE DATO DE ACCOUNT ID: ', type(account_id))
        response = get_account_info.delay(account_id)
        result = response.get()
        print('ESTO ES RESULT: ', result)
        response_data = {
            'action': 'get_account_info',
            'account_info': result
        }
        return response_data
        

    def handle_make_transaction(self, data):
        '''
        Handle method for the management of the action of making a transaction
        '''
        account_id = data['account_id']
        amount = data['amount']
        destination_account_id = data['destination_account_id']
        response = make_transaction.delay(account_id, amount, destination_account_id)
        result = response.get()
        response_data = {
            'action': 'make_transaction',
            'transaction_info': result
        }
        return response_data

    def handle_show_transactions_list(self, data):
        '''
        Handle method for the management of the action of showing the transaction history
        '''
        account_id = data['account_id']
        response = show_transactions_list.delay(account_id)
        result = response.get()
        response_data = {
            'action': 'show_transactions_list',
            'transactions_list': result
        }
        return response_data