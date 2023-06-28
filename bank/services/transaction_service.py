from ..repositories.transaction_repository import TransactionRepository
from .services import Service
from ..models import Transaction as TransactionModel

class TransactionService(Service):
    '''
    Class that represents the service of the Entity Transaction
    param:
        - Service: Class that inherits from the Service interface
    '''

    def __init__(self):
        self.__repository = TransactionRepository()

    def add(self, amount, date, status, source_account, destination_account):
        '''
        Method to add a Transaction
        param:
            - amount: Amount of the Transaction
            - date: Date of the Transaction
            - status: Status of the Transaction
            - source_account: Source Account of the Transaction
            - destination_account: Destination Account of the Transaction
        '''
        model = TransactionModel(
            amount = amount,
            date = date,
            status = status,
            source_account = source_account,
            destination_account = destination_account
        )
        return self.__repository.create(model)
    
    def get_all(self):
        return self.__repository.find_all()
    
    def get_by_id(self, id):
        return self.__repository.find_by_id(id)
    
    def get_by_amount(self, amount):
        return self.__repository.find_by_amount(amount)
    
    def get_by_date(self, date):
        return self.__repository.find_by_date(date)
    
    def get_by_status(self, status):
        return self.__repository.find_by_status(status)
    
    def get_by_source_account(self, source_account):
        return self.__repository.find_by_source_account(source_account)
    
    def get_by_destination_account(self, destination_account):
        return self.__repository.find_by_destination_account(destination_account)
    
    def update(self, id, amount, date, status, source_account, destination_account):
        '''
        Method to update a Transaction
        param:
            - id: Id of the Transaction
            - amount: Amount of the Transaction
            - date: Date of the Transaction
            - status: Status of the Transaction
            - source_account: Source Account of the Transaction
            - destination_account: Destination Account of the Transaction
        '''
        model = TransactionModel(
            id = id,
            amount = amount,
            date = date,
            status = status,
            source_account = source_account,
            destination_account = destination_account
        )
        return self.__repository.update(model)
    
    def delete(self, id):
        '''
        Method to delete a Transaction
        param:
            - id: Id of the Transaction
        '''
        return self.__repository.delete_by_id(id)