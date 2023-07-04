from .repository import Create, Read, Update, Delete
from ..models import Transaction as TransactionModel
import json

class TransactionRepository(Create, Read, Update, Delete):
    '''
    Class to manage the CRUD of the Transaction model
    param:
        - Create: Class that inherits from the Create interface
        - Read: Class that inherits from the Read interface
        - Update: Class that inherits from the Update interface
        - Delete: Class that inherits from the Delete interface
    '''

    def __init__(self):
        self.__type_model = TransactionModel

    @property
    def type_model(self):
        return self.__type_model
    
    def create(self, model):
        model = TransactionModel(
            id = model.id,
            amount = model.amount,
            date = model.date,
            status = model.status,
            source_account = model.source_account,
            destination_account = model.destination_account
        )
        return model.save()
    
    def find_all(self):
        return TransactionModel.objects.all()
    
    def find_by_id(self, id):
        return TransactionModel.objects.get(id=id)
    
    def find_by_amount(self, amount):
        return TransactionModel.objects.get(amount=amount)
    
    def find_by_date(self, date):
        return TransactionModel.objects.get(date=date)
    
    def find_by_status(self, status):
        return TransactionModel.objects.get(status=status)
    
    def find_by_source_account(self, source_account):
        return TransactionModel.objects.get(source_account=source_account)

    def find_all_by_source_account(self, source_account):
        return TransactionModel.objects.filter(source_account=source_account)
    
    def find_by_destination_account(self, destination_account):
        return TransactionModel.objects.get(destination_account=destination_account)
    
    def update(self, model):
        model = TransactionModel(
            id = model.id,
            amount = model.amount,
            date = model.date,
            status = model.status,
            source_account = model.source_account,
            destination_account = model.destination_account
        )
        return model.save()
    
    def delete(self, model):
        return model.delete()
    
    def delete_by_id(self, id: int):
        return TransactionModel.objects.get(id=id).delete()