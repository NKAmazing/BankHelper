from channels.generic.websocket import AsyncWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
from bank.workers.tasks import get_account_info
from bank.workers.tasks import make_transaction
from bank.workers.tasks import show_transactions_list

class ChatConsumer(WebsocketConsumer):
    
    def connect(self):
        self.room_group_name = 'chat'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
            )

        self.accept()


    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json['action']

        if action == 'send_menu':
            self.send_menu()
        elif action == 'get_account_info':
            self.handle_get_account_info(text_data_json)
        elif action == 'make_transaction':
            self.handle_make_transaction(text_data_json)
        elif action == 'show_transactions_list':
            self.handle_show_transactions_list(text_data_json)
        else:
            print('Error: Action does not exist')

    def send_menu(self):
        menu = {
            'action': 'send_menu',
            'options': [
                {'label': 'Show information account', 'value': 'get_account_info'},
                {'label': 'Make a transaction', 'value': 'make_transaction'},
                {'label': 'Show transaction history', 'value': 'show_transactions_list'}
            ]
        }
        self.send(text_data=json.dumps(menu))

    def handle_get_account_info(self, data):
        '''
        Handle method for the management of the action of obtaining the account information
        '''
        account_id = data['account_id']
        get_account_info.delay(account_id)

    def handle_make_transaction(self, data):
        '''
        Handle method for the management of the action of making a transaction
        '''
        account_id = data['account_id']
        amount = data['amount']
        destination_account_id = data['destination_account_id']
        make_transaction.delay(account_id, amount, destination_account_id)

    def handle_show_transactions_list(self, data):
        '''
        Handle method for the management of the action of showing the transaction history
        '''
        account_id = data['account_id']
        show_transactions_list.delay(account_id)


    # def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['message']

    #     async_to_sync(self.channel_layer.group_send)(
    #         self.room_group_name,
    #         {
    #             'type':'chat_message',
    #             'message': message
    #         }
    #     )

    def chat_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message
        }))
