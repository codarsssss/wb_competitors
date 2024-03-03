from django.urls import path

from . import views

urlpatterns = [
    path('competitors/', views.index, name='index'),
    path(
        'start-competitors-task/', views.start_competitors_task,
        name='start_competitors_task',
    ),
]
