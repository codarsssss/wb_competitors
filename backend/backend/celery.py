import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

app = Celery('backend')

# Использование строки здесь означает, что работник не должен сериализовать
# конфигурацию объекта для дочерних процессов.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Загрузка task модулей из всех зарегистрированных Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
