from assistant.workers.tasks import get_account_info, update_account_balance
import requests

# Here is the functions for the server

def search_user(email):
    url = f"http://localhost:8000/client/get_user_by_email/{email}/"
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return False
    
def create_user(username, email, password, address, phone, account_id):
    url = 'http://localhost:8000/client/create_user/'
    data = {
        'username': username,
        'email': email,
        'password': password,
        'address': address,
        'phone': phone,
        'account': account_id
    }
    response = requests.post(url, data=data)
    result = response.json()
    return result

def select_balance(data):
    '''
    Function to select the balance of an account
    '''
    balance = data['balance']
    return balance

def get_account(account_id):
    '''
    Function to get the data of an account
    '''
    url = f'http://localhost:8000/bank/get_account/{account_id}'
    response = requests.get(url)
    account = response.json()
    return account

def update_money(source_account_id, destination_account_id, amount):
    '''
    Function to update balance money between two accounts
    '''
    # Get the data of the source account
    account_info = get_account(source_account_id)

    # Select the balance of the source account
    source_balance = select_balance(account_info)

    # Convert the amount to float
    amount = float(amount)

    # Calculate the new balance of the source account
    new_source_balance = source_balance - amount

    # Update the balance of the source account
    result_acc_src = update_account_balance.delay(source_account_id, new_source_balance, account_info)

    # Get the data of the destination account
    account_info = get_account(destination_account_id)

    # Select the balance of the destination account
    destination_balance = select_balance(account_info)

    # Calculate the new balance of the destination account
    new_destination_balance = destination_balance + amount

    # Update the balance of the destination account
    result_acc_des = update_account_balance.delay(destination_account_id, new_destination_balance, account_info)

    if result_acc_src.get() and result_acc_des.get():
        return True
    else:
        return False