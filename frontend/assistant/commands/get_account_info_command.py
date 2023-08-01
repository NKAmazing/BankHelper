from .command import Command
from ..workers.tasks import get_account_info

class GetAccountInfoCommand(Command):
    '''
    Class to handle the logic of the command to get the account information
    '''
    def __init__(self, data):
        self.data = data

    def execute(self):
        '''
        Handle method for the management of the action of obtaining the account information
        '''
        account_id = self.data['account_id']
        response = get_account_info.delay(account_id)
        result = response.get()
        response_data = {
            'action': 'get_account_info',
            'account_info': result
        }
        return response_data