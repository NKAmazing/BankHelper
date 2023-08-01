from .commands.get_account_info_command import GetAccountInfoCommand
from .commands.make_transaction_command import MakeTransactionCommand
from .commands.show_transactions_list_command import ShowTransactionsListCommand

class MenuHandler:
    '''
    Class to handle the menu options the user can choose from the frontend
    '''
    def __init__(self):
        self.commands = {
            'get_account_info': GetAccountInfoCommand,
            'make_transaction': MakeTransactionCommand,
            'show_transactions_list': ShowTransactionsListCommand,
        }

    def handle_options(self, action, text_data_json):
        '''
        Handle method for the management of the menu options
        '''
        if action in self.commands:
            command_class = self.commands[action]
            command_instance = command_class(data=text_data_json)
            result = command_instance.execute()
        else:
            print('Error: Action does not exist')
            result = {'error': 'Action does not exist'}
        return result