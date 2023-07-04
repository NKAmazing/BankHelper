from channels.generic.websocket import AsyncWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
from assistant.menu_handler import MenuHandler

class ChatConsumer(WebsocketConsumer):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.room_group_name = 'chat'
        self.__menu_handler = MenuHandler()

    def connect(self):
        self.room_group_name = 'chat'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
            )

        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        if 'action' in text_data_json:
            action = text_data_json['action']

            result = self.__menu_handler.handle_options(action, text_data_json)

            self.send(text_data=json.dumps(result))
        elif 'message' in text_data_json:
            message = text_data_json['message']

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type':'chat_message',
                    'message': message
                }
            )
        else:
            print("No data received")

    def chat_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message
        }))