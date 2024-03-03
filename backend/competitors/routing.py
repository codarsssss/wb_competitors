from django.urls import re_path

from .consumers import MainConsumer

websocket_urlpatterns = [
    re_path(r'ws/task-status/(?P<task_id>\w+)/$', MainConsumer.as_asgi()),
]
