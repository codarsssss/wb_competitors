from celery import shared_task
from celery.utils.log import get_task_logger

from .api import get_competitors, get_product_details

logger = get_task_logger(__name__)


@shared_task
def get_competitors_task(product_id):
    logger.info(
        f'Запуск задачи get_competitors_task с product_id={product_id}',
    )
    try:
        result = get_competitors(product_id)
        logger.info(
            f'Задача get_competitors_task успешно выполнена с результатом '
            f'{result}',
        )
        return result
    except Exception as e:
        logger.error(
            f'Ошибка при выполнении задачи get_competitors_task: '
            f'{e}',
        )
        raise


@shared_task
def get_product_details_task(product_ids):
    return get_product_details(product_ids)
