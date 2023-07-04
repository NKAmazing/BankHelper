"""
ASGI config for bank_helper project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import server.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bank_helper.settings')

application = ProtocolTypeRouter(   {
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            server.routing.websocket_urlpatterns
        )
    ),

})
