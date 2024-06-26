from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('inicio_login/', views.inicio_login, name='inicio_login'),
    path('cargar_archivo/', views.cargar_archivo, name='cargar_archivo'),
    path('cargar_archivo_gestionrw/', views.cargar_archivo_gestionrw, name='cargar_archivo_gestionrw'),
]
