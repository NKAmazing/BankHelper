from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ChatConsumer(AsyncWebsocketConsumer):
    
    # Connects to the websocket
    async def connect(self):
        await self.accept()

    # Disconnects from the websocket
    async def disconnect(self, close_code):
        pass

    # Receives a message from the websocket
    async def receive(self, text_data):
        # Convertir los datos a formato JSON
        data = {
            'message': text_data
        }
        message_json = json.dumps(data)

        # Enviar el mensaje JSON al cliente
        await self.send(text_data=message_json)

        print(f"Message received: {message_json}")
