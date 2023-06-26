from ..repositories.chat_repository import ChatRepository
from .services import Service
from ..models import Chat as ChatModel

class ChatService(Service):
    '''
    Class that represents the service of the Entity Chat
    param:
        - Service: Class that inherits from the Service interface
    '''

    def __init__(self):
        self.__repository = ChatRepository()

    def add(self, chat_name, date, messages):
        '''
        Method to add a Chat
        param:
            - chat_name: Name of the Chat
            - date: Date of the Chat
            - messages: Messages of the Chat
        '''
        model = ChatModel(
            chat_name = chat_name,
            date = date,
            messages = messages
        )
        return self.__repository.create(model)
    
    def get_all(self):
        '''
        Method to get all Chats
        '''
        return self.__repository.find_all()
    
    def get_by_id(self, id):
        '''
        Method to get a Chat by its id
        param:
            - id: Id of the Chat
        '''
        return self.__repository.find_by_id(id)
    
    def get_by_chat_name(self, chat_name):
        '''
        Method to get a Chat by its chat_name
        param:
            - chat_name: Name of the Chat
        '''
        return self.__repository.find_by_chat_name(chat_name)