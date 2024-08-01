
import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import  URLRouter, ProtocolTypeRouter
from chat_rooms import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_dir.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    )
})
