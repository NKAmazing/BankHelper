from .command import Command
from ..workers.tasks import show_transactions_list

class ShowTransactionsListCommand(Command):
    '''
    Class to handle the logic of the command to show the transactions list
    '''
    def __init__(self, data):
        self.data = data

    def execute(self):
        '''
        Handle method for the management of the action of showing the transactions list
        '''
        account_id = self.data['account_id']
        response = show_transactions_list.delay(account_id)
        result = response.get()
        response_data = {
            'action': 'show_transactions_list',
            'transactions_list': result
        }
        return response_data