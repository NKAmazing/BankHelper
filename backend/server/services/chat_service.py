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

    def add(self, chat_name, date):
        '''
        Method to add a Chat
        param:
            - chat_name: Name of the Chat
            - date: Date of the Chat
            - messages: Messages of the Chat
        '''
        model = self._set_chat_credentials(None, chat_name, date)
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
    
    def update(self, id, chat_name, date):
        '''
        Method to update a Chat
        param:
            - id: Id of the Chat
            - chat_name: Name of the Chat
            - date: Date of the Chat
            - messages: Messages of the Chat
        '''
        model = self._set_chat_credentials(id, chat_name, date)
        return self.__repository.update(model)
    
    def delete(self, id):
        '''
        Method to delete a Chat
        param:
            - id: Id of the Chat
        '''
        return self.__repository.delete_by_id(id)

    def _set_chat_credentials(self, id, chat_name, date):
        if id is not None:
            model = ChatModel(
                id = id,
                chat_name = chat_name,
                date = date
            )
        else:
            model = ChatModel(
                chat_name = chat_name,
                date = date
            )
        return model