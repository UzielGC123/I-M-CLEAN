from django.urls import path
from . import views

urlpatterns = [
    # La ruta vacía ('') se asigna a la vista hola_mundo
    path('', views.hola_mundo, name='hola'),
]