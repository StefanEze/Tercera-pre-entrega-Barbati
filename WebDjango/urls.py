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
    path("leerUsuarios/", views.leerUsuarios, name="LeerUsuarios"),
    path("leerArticulos/", views.leerArticulos, name="LeerArticulos"),
    path("eliminarUsuario/<usuario_nombre>", views.eliminarUsuario, name="EliminarUsuario"),
    path("eliminarArticulo/<articulo_nombre>", views.eliminarArticulo, name="EliminarArticulo"),
    path("editarUsuario/<usuario_nombre>", views.editarUsuario, name="EditarUsuario"),
    path("editarArticulo/<articulo_nombre>", views.editarArticulo, name="EditarArticulo"),
    ]
