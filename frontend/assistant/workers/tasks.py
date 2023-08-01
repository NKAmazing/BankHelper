from frontend.celery import app
from .worker_facade import WorkerFacade

worker = WorkerFacade()

# Here is the Celery tasks that will be executed

@app.task
def get_account_info(account_id):
    '''
    Function task to get the account info
    param:
        - account_id: Id of the account
    '''
    return worker.get_account_info(account_id)

@app.task
def make_transaction(account_id, amount, destination_account_id):
    '''
    Function task to make a transaction
    param:
        - account_id: Id of the account
        - amount: Amount of the transaction
        - destination_account_id: Id of the destination account
    '''
    return worker.make_transaction(account_id, amount, destination_account_id)

@app.task
def show_transactions_list(account_id):
    '''
    Function task to show the transactions list
    param:
        - account_id: Id of the account
    '''
    return worker.show_transactions_list(account_id)
    

@app.task
def update_account_balance(account_id, new_balance, account_info):
    '''
    Function task to update the account balance
    param:
        - account_id: Id of the account
        - new_balance: New balance of the account
        - account_info: Account info
    '''
    return worker.update_account_balance(account_id, new_balance, account_info)

@app.task
def search_user(email):
    '''
    Function task to search a user
    param:
        - email: Email of the user
    '''
    return worker.search_user(email)