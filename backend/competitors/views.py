from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from .tasks import get_competitors_task
from .utils import extract_product_id


def index(request):
    return render(request, 'competitors/index.html')


# Эндпоинт для AJAX-запроса для начала задачи Celery
@require_POST
def start_competitors_task(request):
    product_url = request.POST.get('product_url')
    product_id = extract_product_id(product_url)
    task = get_competitors_task.delay(product_id)
    return JsonResponse({'task_id': task.id})
