from django.shortcuts import render
from WebDjango.models import *
from WebDjango.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from WebDjango.forms import *
from django.contrib.auth.hashers import make_password



@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request,"WebDjango/inicio.html",{'url':avatares[0].imagen.url})



#--------------------------------------------------------Publicaciones--------------------------------------------------------

#Esta función muestra el formulario
def publicaciones(request):
    if request.method == "POST":
        miFormulario = PublicacionFormulario(request.POST) #Aqui me llega la informacion del html
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            publicacion = Publicacion(
                titulo=informacion['titulo'], 
                subtitulo=informacion['subtitulo'], 
                cuerpo=informacion['cuerpo'],
                autor=informacion['autor'],
                fecha=informacion['fecha'],
                imagen=informacion['imagen'],)
            publicacion.save()
            return render(request, "WebDjango/inicio.html")
    else:
        miFormulario = PublicacionFormulario()
    return render(request, "WebDjango/Publicaciones/publicaciones.html", {"miFormulario":miFormulario})

class PublicacionList(ListView):
    model = Publicacion
    template_name ="WebDjango/Publicaciones/publicaciones_list.html"

class PublicacionDetalle(DetailView):
    model = Publicacion
    template_name ="WebDjango/Publicaciones/publicacion_detalle.html"

class PublicacionCreacion(CreateView):
    model = Publicacion
    template_name ="WebDjango/Publicaciones/publicacion_form.html"
    success_url = "/WebDjango/publicacion/list"
    fields= [
        'titulo', 
        'subtitulo',
        'cuerpo',
        'autor',
        'fecha',
        'imagen'
        ]

class PublicacionUpdate(UpdateView):
    model = Publicacion
    template_name ="WebDjango/Publicaciones/publicacion_form.html"
    success_url = "/WebDjango/publicacion/list"
    fields= [
        'titulo', 
        'subtitulo',
        'cuerpo',
        'autor',
        'fecha',
        'imagen'
        ]

class PublicacionDelete(DeleteView):
    model = Publicacion
    template_name ="WebDjango/Publicaciones/publicacion_confirm_delete.html"
    success_url = "/WebDjango/publicacion/list"

#--------------------------------------------------------INICIAR SESION--------------------------------------------------------
@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request,"WebDjango/inicio.html",{'url':avatares[0].imagen.url})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)
            if user is not None:
                login(request,user)
                
                return render(request,"WebDjango/inicio.html", {"mensaje": f"Bienvenido {usuario}!!!"})
            else:
                return render(request,"WebDjango/inicio.html", {"mensaje": "Error, datos incorrectos"})
        else:
            return render(request,"WebDjango/inicio.html", {"mensaje": "Error, formulario erróneo"})
    form = AuthenticationForm()
    return render(request,"WebDjango/login.html", {'form':form})



#--------------------------------------------------------REGISTRAR--------------------------------------------------------

def register(request):

    if request.method =="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"WebDjango/inicio.html",{"mensaje":"Usuario Creado :)"})
        
    else:
        form = UserRegisterForm()

    return render(request,"WebDjango/register.html",{"form":form})

#--------------------------------------------------------EDITAR PERFIL--------------------------------------------------------
@login_required
def editarPerfil(request):
    usuario=request.user
    if request.method=="POST":
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            print(miFormulario)
            usuario.email = informacion['email']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            if informacion['password1'] == informacion['password2']:
                usuario.password = make_password(informacion['password1'])
                usuario.save()
            else:
                return render(request, "inicio.html",{"mensaje":"Contraseña incorrecta"})
            
            return render(request, "inicio.html")
    else:
        miFormulario = UserEditForm(initial={"email":usuario.email})

    return render(request,"webDjango/editarPerfil.html", {"miFormulario":miFormulario,"usuario":usuario})
    

#--------------------------------------------------------AVATAR--------------------------------------------------------

@login_required
def agregarAvatar(request):
    if request.method =='POST':
        miFormulario = AvatarFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            u = User.objects.get(username=request.user)
            avatar= Avatar(user=u, imagen=miFormulario.cleaned_data['imagen'])
            avatar.save()

            return render(request,'inicio.html')
    else:
        miFormulario= AvatarFormulario()
    return render(request,'WebDjango/agregarAvatar.html', {'miFormulario':miFormulario})
