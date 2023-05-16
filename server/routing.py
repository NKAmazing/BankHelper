from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from . import consumers

# Establishes the websocket URL router
websocket_urlpatterns = [
    path('ws/', consumers.MyConsumer.as_asgi()),
]

# Establishes the protocol type router
application = ProtocolTypeRouter({
    'websocket': URLRouter(
        websocket_urlpatterns
    ),
})
