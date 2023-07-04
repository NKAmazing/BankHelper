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

def update_money(requests, source_account_id, destination_account_id, amount):
    '''
    Function to update balance money between two accounts
    '''
    # Get the data of the source account
    account_info = get_account_info.delay(source_account_id)
    data = account_info.get()

    # Select the balance of the source account
    source_balance = select_balance(data)

    # Calculate the new balance of the source account
    new_source_balance = source_balance - amount

    # Update the balance of the source account
    update_account_balance.delay(source_account_id, new_source_balance, data)

    # Get the data of the destination account
    account_info = get_account_info.delay(destination_account_id)
    data = account_info.get()

    # Select the balance of the destination account
    destination_balance = select_balance(requests, data)

    # Calculate the new balance of the destination account
    new_destination_balance = destination_balance + amount

    # Update the balance of the destination account
    update_account_balance.delay(destination_account_id, new_destination_balance, data)