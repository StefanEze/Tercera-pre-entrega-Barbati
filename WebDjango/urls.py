from django.urls import path
from WebDjango import views
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', views.inicio, name='Inicio'),
    # path("buscar/", views.buscar),
    path("publicaciones", views.publicaciones, name='Publicaciones'),
    path("publicacion/list", views.PublicacionList.as_view(),name="List"),
    path(r"^(?<pk>\d+)$", views.PublicacionDetalle.as_view(), name="Detail"),
    path(r"^nuevo$", views.PublicacionCreacion.as_view(), name="New"),
    path(r"^editar(?<pk>\d+)$", views.PublicacionUpdate.as_view(), name="Edit"),
    path(r"^borrar(?<pk>\d+)$", views.PublicacionDelete.as_view(), name="Delete"),
    path('login', views.login_request ,name ="Login"),
    path('register', views.register ,name ="Register"),
    path("logout",LogoutView.as_view(template_name="WebDjango/logout.html"),name = "Logout"),
    path("editarPerfil", views.editarPerfil, name="EditarPerfil"),
    path("agregarAvatar",views.agregarAvatar,name="AgregarAvatar"),
    ]
