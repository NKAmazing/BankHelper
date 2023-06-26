from ..repositories.account_repository import AccountRepository
from .services import Service
from ..models import Account as AccountModel

class AccountService(Service):
    '''
    Class that represents the service of the Entity Account
    param:
        - Service: Class that inherits from the Service interface
    '''

    def __init__(self):
        self.__repository = AccountRepository()

    def add(self, account_number, balance, transactions):
        '''
        Method to add a Account
        param:
            - account_number: Account Number of the Account
            - balance: Balance of the Account
            - transactions: Transactions of the Account
        '''
        model = AccountModel(
            account_number = account_number,
            balance = balance,
            transactions = transactions
        )
        return self.__repository.create(model)
    
    def get_all(self):
        '''
        Method to get all Accounts
        '''
        return self.__repository.find_all()
    
    def get_by_id(self, id):
        '''
        Method to get a Account by its id
        param:
            - id: Id of the Account
        '''
        return self.__repository.find_by_id(id)
    
    def get_by_account_number(self, account_number):
        '''
        Method to get a Account by its account_number
        param:
            - account_number: Account Number of the Account
        '''
        return self.__repository.find_by_account_number(account_number)
