from asgiref.sync import async_to_sync
from celery import shared_task
from celery.utils.log import get_task_logger
from channels.layers import get_channel_layer

from .utils import get_competitors, get_product_details

logger = get_task_logger(__name__)


@shared_task(bind=True)
def get_competitors_task(self, product_id):
    competitors_ids = get_competitors(product_id)
    if competitors_ids:
        # Запускаем задачу для получения деталей продуктов
        get_product_details_task.delay(self.request.id, competitors_ids)


@shared_task
def get_product_details_task(task_id, product_ids):
    channel_layer = get_channel_layer()
    group_name = f'task_{task_id}'

    # Получаем детали продуктов
    details = get_product_details(product_ids)

    # Отправляем данные в группу WebSocket
    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'send_details',
            'details': details,
        },
    )
