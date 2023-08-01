from .command import Command
from ..workers.tasks import make_transaction
from ..functions import update_money

class MakeTransactionCommand(Command):
    '''
    Class to handle the logic of the command to make a transaction
    '''

    def __init__(self, data):
        self.data = data

    def execute(self):
        '''
        Handle method for the management of the action of making a transaction
        '''
        account_id = self.data['account_id']
        amount = self.data['amount']
        destination_account_id = self.data['destination_account_id']

        # Update the balance of the accounts
        update_balance = update_money(account_id, destination_account_id, amount)

        if update_balance:
            # Call the task to make the transaction
            response = make_transaction.delay(account_id, amount, destination_account_id)
            result = response.get()

            if result:
                # Set the response data to send to the frontend
                response_data = {
                    'action': 'make_transaction',
                    'transaction_info': result
                }
                return response_data
            else:
                response_data = {
                    'action': 'make_transaction',
                    'transaction_info': 'Error making transaction'
                }
                return response_data
        else:
            response_data = {
                'action': 'make_transaction',
                'transaction_info': 'Error updating balance'
            }
            return response_data