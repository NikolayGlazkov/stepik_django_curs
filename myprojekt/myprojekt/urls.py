
from django.contrib import admin
from django.urls import path, include
from ferst.views import index  # Импортируем представление index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ferst/', include('ferst.urls')),  # Подключение urls.py вашего приложения
    path('create_client/', include("ferst.urls")),
    path('show_clients',include('ferst.urls')),
    path('', index, name='home'),  # Главная страница
    # Другие URL, если есть
]