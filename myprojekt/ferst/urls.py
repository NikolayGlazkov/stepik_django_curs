# ferst/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Стартовая страница
    path('create_client/', views.create_client, name='create_client'),
    path('show_clients/', views.show_clients, name='show_clients'),
    path('edit_client/', views.edit_client, name='edit_client'),  # Убедитесь, что у вас есть такая запись

    # Другие URL, если есть
]
