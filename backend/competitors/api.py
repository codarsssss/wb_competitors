# competitors/api.py

import logging

import requests
from django.conf import settings
from requests.exceptions import RequestException


def extract_product_id(product_url):
    return product_url.split('/')[-2]


def get_competitors(product_id):
    try:
        response = requests.get(f'{settings.SIMILAR_API_URL}{product_id}')
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        logging.error(f'Ошибка при запросе к API получения конкурентов: {e}')
        return []


def get_product_details(product_ids):
    ids_string = ';'.join(map(str, product_ids))
    try:
        response = requests.get(f'{settings.WB_API_URL}{ids_string}')
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        logging.error(f'Ошибка при запросе к API деталей продуктов: {e}')
        return []
