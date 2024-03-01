from django.urls import path

from . import views

urlpatterns = [
    path('competitors/', views.index, name='index'),
    path('task-status/<str:task_id>/', views.task_status, name='task_status'),

]
