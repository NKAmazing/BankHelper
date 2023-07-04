from .repository import Create, Read, Update, Delete
from ..models import Chat as ChatModel
import json

class ChatRepository(Create, Read, Update, Delete):
    '''
    Class to manage the CRUD of the Chat model
    param:
        - Create: Class that inherits from the Create interface
        - Read: Class that inherits from the Read interface
        - Update: Class that inherits from the Update interface
        - Delete: Class that inherits from the Delete interface
    '''

    def __init__(self):
        self.__type_model = ChatModel

    @property
    def type_model(self):
        return self.__type_model
    
    def create(self, model):
        model = ChatModel(
            id = model.id,
            chat_name = model.chat_name,
            date = model.date,
        )
        return model.save()
    
    def find_all(self):
        return ChatModel.objects.all()
    
    def find_by_id(self, id):
        return ChatModel.objects.get(id=id)
    
    def find_by_chat_name(self, chat_name):
        return ChatModel.objects.get(chat_name=chat_name)
    
    def update(self, model):
        model = ChatModel(
            id = model.id,
            chat_name = model.chat_name,
            date = model.date,
            messages = model.messages
        )
        return model.save()
    
    def delete(self, model):
        model = ChatModel(
            id = model.id,
            chat_name = model.chat_name,
            date = model.date,
            messages = model.messages
        )
        return model.delete()
    
    def delete_by_id(self, id):
        return ChatModel.objects.get(id=id).delete()