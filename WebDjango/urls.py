from django.urls import path
from WebDjango import views
from django.contrib.auth.views import LogoutView


app_name = 'WebDjango'

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
    path("envio/list", views.EnvioList.as_view(),name="List"),
    path(r"^(?<pk>\d+)$", views.EnvioDetalle.as_view(), name="Detail"),
    path(r"^nuevo$", views.EnvioCreacion.as_view(), name="New"),
    path(r"^editar(?<pk>\d+)$", views.EnvioUpdate.as_view(), name="Edit"),
    path(r"^borrar(?<pk>\d+)$", views.EnvioDelete.as_view(), name="Delete"),
    path('login', views.login_request ,name ="Login"),
    path('register', views.register ,name ="Register"),
    path("logout",LogoutView.as_view(template_name="WebDjango/logout.html"),name = "Logout"),
    path("editarPerfil", views.editarPerfil, name="EditarPerfil"),
    ]
