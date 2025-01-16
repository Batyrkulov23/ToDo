from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('<int:task_id>/', views.task_detail, name='task_detail'),
    path('create/', views.create_task, name='create_task'),
    path('<int:task_id>/toggle/', views.toggle_task_status, name='toggle_task_status'),
    path('<int:task_id>/delete/', views.delete_task, name='delete_task'),  # Новый маршрут
    path('<int:task_id>/edit/', views.edit_task, name='edit_task'),  # Новый маршрут

]
