from django.urls import path, include
from .views import index, redireciona, setacookie

app_name = 'aula3'

urlpatterns = [
    path('', index),
    path('cookie', setacookie),
    path('uol', redireciona)
]