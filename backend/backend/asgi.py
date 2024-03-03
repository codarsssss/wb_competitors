import os

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from competitors import routing
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

asgi_application = get_asgi_application()

application = ProtocolTypeRouter({
            'http': asgi_application,
            'websocket': AllowedHostsOriginValidator(
                    URLRouter(routing.websocket_urlpatterns),
            ),
})
