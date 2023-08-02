from .repository import Create, Read, Update, Delete
from ..models import Bank as BankModel
import json

class BankRepository(Create, Read, Update, Delete):
    '''
    Class to manage the CRUD of the Bank model
    param:
        - Create: Class that inherits from the Create interface
        - Read: Class that inherits from the Read interface
        - Update: Class that inherits from the Update interface
        - Delete: Class that inherits from the Delete interface
    '''

    def __init__(self):
        self.__type_model = BankModel

    @property
    def type_model(self):
        return self.__type_model
    
    def create(self, model):
        bank = self._set_bank_model(model)
        return bank.save()
    
    def find_all(self):
        return BankModel.objects.all()
    
    def find_by_id(self, id):
        return BankModel.objects.get(id=id)
    
    def find_by_bank_name(self, bank_name):
        return BankModel.objects.get(bank_name=bank_name)
    
    def find_by_bank_email(self, bank_email):
        return BankModel.objects.get(bank_email=bank_email)
    
    def update(self, model):
        bank = self._set_bank_model(model)
        return bank.save()
    
    def delete(self, model):
        return model.delete()
    
    def delete_by_id(self, id):
        return BankModel.objects.get(id=id).delete()
    
    def _set_bank_model(self, model):
        return BankModel(
            id = model.id,
            bank_name = model.bank_name,
            bank_email = model.bank_email,
        )