from .repository import Create, Read, Update, Delete
from ..models import User as UserModel
import json

class UserRepository(Create, Read, Update, Delete):
    '''
    Class to manage the CRUD of the User model
    param:
        - Create: Class that inherits from the Create interface
        - Read: Class that inherits from the Read interface
        - Update: Class that inherits from the Update interface
        - Delete: Class that inherits from the Delete interface
    '''

    def __init__(self):
        self.__type_model = UserModel

    @property
    def type_model(self):
        return self.__type_model
    
    def create(self, model):
        user = self._set_user_model(model)
        return user.save()
    
    def find_all(self):
        return UserModel.objects.all()
    
    def find_by_id(self, id):
        return UserModel.objects.get(id=id)
    
    def find_by_username(self, username):
        return UserModel.objects.get(username=username)
    
    def find_by_email(self, email):
        return UserModel.objects.get(email=email)
    
    def find_by_account(self, account):
        return UserModel.objects.get(account=account)
    
    def update(self, model):
        user = self._set_user_model(model)
        return user.save()
    
    def delete(self, model):
        return model.delete()

    def delete_by_id(self, id):
        return UserModel.objects.get(id=id).delete()
    
    def _set_user_model(self, model):
        return UserModel(
            id=model.id,
            username=model.username,
            email=model.email,
            password=model.password,
            address=model.address,
            phone=model.phone,
            account=model.account
        )