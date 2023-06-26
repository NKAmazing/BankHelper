from ..repositories.user_repository import UserRepository
from .services import Service
from ..models import User as UserModel

class UserService(Service):
    '''
    Class that represents the service of the Entity User
    param:
        - Service: Class that inherits from the Service interface
    '''

    def __init__(self):
        self.__repository = UserRepository()

    def add(self, username, email, password, address, phone, account):
        '''
        Method to add a User
        param:
            - username: Username of the User
            - email: Email of the User
            - password: Password of the User
            - address: Address of the User
            - phone: Phone of the User
            - account: Account of the User
        '''
        model = UserModel(
            username = username,
            email = email,
            password = password,
            address = address,
            phone = phone,
            account = account
        )
        return self.__repository.create(model)
    
    def get_all(self):
        '''
        Method to get all Users
        '''
        return self.__repository.find_all()

    def get_by_id(self, id):
        '''
        Method to get a User by its id
        param:
            - id: Id of the User
        '''
        return self.__repository.find_by_id(id)

    def get_by_username(self, username):
        '''
        Method to get a User by its username
        param:
            - username: Username of the User
        '''
        return self.__repository.find_by_username(username)

    def get_by_email(self, email):
        '''
        Method to get a User by its email
        param:
            - email: Email of the User
        '''
        return self.__repository.find_by_email(email)
    
    def get_by_account(self, account):
        '''
        Method to get a User by its account
        param:
            - account: Account of the User
        '''
        return self.__repository.find_by_account(account)