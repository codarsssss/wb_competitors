from celery.result import AsyncResult
from django.http import JsonResponse
from django.shortcuts import render

from .api import extract_product_id
from .tasks import get_competitors_task


def index(request):
    context = {'task_id': None, 'results': None}

    if request.method == 'POST':
        product_url = request.POST.get('product_url')
        product_id = extract_product_id(product_url)

        # Асинхронно запускаем задачу Celery для получения данных о конкурентах
        task = get_competitors_task.delay(product_id)

        # Сохраняем ID задачи в контексте, чтобы передать его в шаблон
        context['task_id'] = task.id

    return render(request, 'competitors/index.html', context)


def task_status(request, task_id):
    # Эта функция будет вызываться AJAX-запросом для проверки статуса задачи
    task_result = AsyncResult(task_id)
    if task_result.ready():
        # Если задача завершена, извлекаем результат и передаем его в шаблон
        context = {
            'task_id': None,
            'results': task_result.result,
        }
        return render(request, 'competitors/index.html', context)
    else:
        # Если результат ещё не готов, возвращаем статус 'PENDING'
        return JsonResponse({'status': 'PENDING'}, status=202)
