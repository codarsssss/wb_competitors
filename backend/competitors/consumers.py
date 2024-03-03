import json

from channels.generic.websocket import AsyncWebsocketConsumer


class MainConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.task_id = self.scope['url_route']['kwargs']['task_id']
        self.group_name = f'task_{self.task_id}'

        # Добавляем пользователя в группу на основе task_id
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Удаляем пользователя из группы
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name,
        )

    # Этот метод вызывается, когда данные по конкурентам готовы
    async def send_details(self, event):
        # Отправляем детали клиенту
        await self.send(text_data=json.dumps(event['details']))
