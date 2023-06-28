from ..repositories.bank_repository import BankRepository
from .services import Service
from ..models import Bank as BankModel

class BankService(Service):
    '''
    Class that represents the service of the Entity Bank
    param:
        - Service: Class that inherits from the Service interface
    '''

    def __init__(self):
        self.__repository = BankRepository()

    def add(self, bank_name, bank_email):
        '''
        Method to add a Bank
        param:
            - bank_name: Name of the Bank
            - bank_email: Email of the Bank
        '''
        model = BankModel(
            bank_name=bank_name,
            bank_email=bank_email
        )

        return self.__repository.create(model)
    
    def get_all(self):
        '''
        Method to get all Banks
        '''
        return self.__repository.find_all()
    
    def get_by_id(self, id):
        '''
        Method to get a Bank by its id
        param:
            - id: Id of the Bank
        '''
        return self.__repository.find_by_id(id)
    
    def get_by_bank_name(self, bank_name):
        '''
        Method to get a Bank by its bank_name
        param:
            - bank_name: Name of the Bank
        '''
        return self.__repository.find_by_bank_name(bank_name)
    
    def get_by_bank_email(self, bank_email):
        '''
        Method to get a Bank by its bank_email
        param:
            - bank_email: Email of the Bank
        '''
        return self.__repository.find_by_bank_email(bank_email)
    
    def update(self, id, bank_name, bank_email):
        '''
        Method to update a Bank
        param:
            - id: Id of the Bank
            - bank_name: Name of the Bank
            - bank_email: Email of the Bank
        '''
        model = BankModel(
            id=id,
            bank_name=bank_name,
            bank_email=bank_email
        )

        return self.__repository.update(model)
    
    def delete(self, id):
        '''
        Method to delete a Bank
        param:
            - id: Id of the Bank
        '''
        return self.__repository.delete_by_id(id)