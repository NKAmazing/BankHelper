from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from . import consumers

# Establishes the websocket URL router
websocket_urlpatterns = [
    re_path('ws/socket-server/', consumers.ChatConsumer.as_asgi()),
]

# Establishes the protocol type router
application = ProtocolTypeRouter({
    'websocket': URLRouter(
        websocket_urlpatterns
    ),
})
