from django.urls import path
from WebDjango import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path("usuarios", views.usuarios, name='Usuarios'),
    path("busquedaEmail/", views.busquedaEmail, name='BusquedaEmail'),
    path("buscar/", views.buscar),
    path("envios", views.envios, name='Envios'),
    path("articulos", views.articulos, name='Articulos'),
    path("busquedaNombre/", views.busquedaNombre, name='BusquedaNombre'),
    path("buscarNombre/", views.buscarNombre),
    ]
