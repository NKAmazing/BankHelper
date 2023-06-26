from .repository import Create, Read, Update, Delete
from ..models import Message as MessageModel
import json

class MessageRepository(Create, Read, Update, Delete):
    '''
    Class to manage the CRUD of the Message model
    param:
        - Create: Class that inherits from the Create interface
        - Read: Class that inherits from the Read interface
        - Update: Class that inherits from the Update interface
    '''

    def __init__(self):
        self.__type_model = MessageModel

    @property
    def type_model(self):
        return self.__type_model
    
    def create(self, model):
        model = MessageModel(
            id = model.id,
            content = model.content,
            date = model.date,
            user = model.user,
            chat_reference = model.chat_reference
        )
        return model.save()
    
    def find_all(self):
        return MessageModel.objects.all()
    
    def find_by_id(self, id):
        return MessageModel.objects.get(id=id)
    
    def find_by_content(self, content):
        return MessageModel.objects.get(content=content)
    
    def find_by_user(self, user):
        return MessageModel.objects.get(user=user)
    
    def find_by_chat_reference(self, chat_reference):
        return MessageModel.objects.get(chat_reference=chat_reference)