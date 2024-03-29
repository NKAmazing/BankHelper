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
        - Delete: Class that inherits from the Delete interface
    '''

    def __init__(self):
        self.__type_model = AccountModel

    @property
    def type_model(self):
        return self.__type_model
    
    def create(self, model):
        account = self._set_account_model(model)
        return account.save()
    
    def find_all(self):
        return AccountModel.objects.all()
    
    def find_by_id(self, id):
        return AccountModel.objects.get(id=id)
    
    def find_by_account_number(self, account_number):
        return AccountModel.objects.get(account_number=account_number)
    
    def update(self, model):
        account = self._set_account_model(model)
        return account.save()
    
    def delete(self, model):
        return model.delete()
    
    def delete_by_id(self, id):
        return AccountModel.objects.get(id=id).delete()
    
    def _set_account_model(self, model):
        return AccountModel(
            id = model.id,
            account_number = model.account_number,
            balance = model.balance,
            bank = model.bank
        )