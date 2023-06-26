from ..repositories.message_repository import MessageRepository
from .services import Service
from ..models import Message as MessageModel

class MessageService(Service):
    '''
    Class that represents the service of the Entity Message
    param:
        - Service: Class that inherits from the Service interface
    '''

    def __init__(self):
        self.__repository = MessageRepository()

    def add(self, content, date, user, chat_reference):
        '''
        Method to add a Message
        param:
            - content: Content of the Message
            - date: Date of the Message
            - user: User of the Message
            - chat_reference: Chat of the Message
        '''
        model = MessageModel(
            content = content,
            date = date,
            user = user,
            chat_reference = chat_reference
        )
        return self.__repository.create(model)
    
    def get_all(self):
        '''
        Method to get all Messages
        '''
        return self.__repository.find_all()
    
    def get_by_id(self, id):
        '''
        Method to get a Message by its id
        param:
            - id: Id of the Message
        '''
        return self.__repository.find_by_id(id)
    
    def get_by_content(self, content):
        '''
        Method to get a Message by its content
        param:
            - content: Content of the Message
        '''
        return self.__repository.find_by_content(content)
    
    def get_by_user(self, user):
        '''
        Method to get a Message by its user
        param:
            - user: User of the Message
        '''
        return self.__repository.find_by_user(user)
    
    def get_by_chat_reference(self, chat_reference):
        '''
        Method to get a Message by its chat_reference
        param:
            - chat_reference: Chat of the Message
        '''
        return self.__repository.find_by_chat_reference(chat_reference)