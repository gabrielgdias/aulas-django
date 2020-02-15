from django.urls import path, include
from . import views

app_name = 'aula3'

urlpatterns = [
    path('', views.index),
    path('cookie', views.setacookie),
    path('uol', views.redireciona),
    path('<int:code>', views.show_code),
    path('cat/<int:cat>', views.redirect_cat),
    path('get/', views.show_get_values),
    path('post/', views.show_post_values)
]