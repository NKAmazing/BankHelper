from .repository import Create, Read, Update, Delete
from ..models import Account as AccountModel
import json

class AccountRepository(Create, Read, Update, Delete):
    '''
    Class to manage the CRUD of the Account model
    param:
        - Create: Class that inherits from the Create interface
        - Read: Class that inherits from the Read interface
        - Update: Class that inherits from the Update interface
    '''

    def __init__(self):
        self.__type_model = AccountModel

    @property
    def type_model(self):
        return self.__type_model
    
    def create(self, model):
        model = AccountModel(
            id = model.id,
            account_number = model.account_number,
            balance = model.balance,
            transactions = model.transactions
        )
        return model.save()
    
    def find_all(self):
        return AccountModel.objects.all()
    
    def find_by_id(self, id):
        return AccountModel.objects.get(id=id)
    
    def find_by_account_number(self, account_number):
        return AccountModel.objects.get(account_number=account_number)