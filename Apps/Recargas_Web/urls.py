from django.urls import path
from .import views

urlpatterns = [
    path('', views.inicio_login, name='Inicio login'),
    path('subir-data-xlsx', views.cargar_archivo, name="cargar_archivo"),
]