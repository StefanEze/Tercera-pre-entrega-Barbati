from django.shortcuts import render
from WebDjango.models import *
from WebDjango.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView


def inicio(request):
    return render(request,"WebDjango/inicio.html")



#--------------------------------------------------------USUARIOS--------------------------------------------------------

#Esta función muestra el formulario
def usuarios(request):
    if request.method == "POST":
        miFormulario = UsuarioFormulario(request.POST) #Aqui me llega la informacion del html
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario = Usuario(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            usuario.save()
            return render(request, "WebDjango/inicio.html")
    else:
        miFormulario = UsuarioFormulario()
    return render(request, "WebDjango/Usuarios/usuarios.html", {"miFormulario":miFormulario})



def busquedaEmail(request):
    return render(request, "WebDjango/Usuarios/busquedaEmail.html")


#Esta función busca los datos registrados 
def buscar(request):
    if request.GET['email']:
        email = request.GET['email']
        usuarios = Usuario.objects.filter(email__icontains=email)
        return render(request,'WebDjango/Usuarios/usuarioresp.html', {"usuarios":usuarios, "email":email})
    else:
        respuesta ="No enviaste datos."
    return render(request,'WebDjango/Usuarios/usuarioresp.html',{"respuesta":respuesta})


#Esta funcion lee los usuarios
def leerUsuarios(request):

    usuarios = Usuario.objects.all() #Trae todos los usuarios

    contexto= {"usuarios": usuarios}

    return render(request, "WebDjango/Usuarios/leerUsuarios.html", contexto)


def eliminarUsuario(request, usuario_nombre):

    usuario = Usuario.objects.get(nombre=usuario_nombre)
    usuario.delete()

    #vuelvo al menú
    usuarios = Usuario.objects.all() #Trae todos los usuarios

    contexto= {"usuarios":usuarios}

    return render(request,"WebDjango/Usuarios/leerUsuarios.html", contexto)


def editarUsuario(request, usuario_nombre):

    #Recibe el nombre del usuario a moificar
    usuario = Usuario.objects.get(nombre=usuario_nombre)

    #Si es metodo Post hago lo mismo que el agregar
    if request.method =="POST":

        miFormulario = UsuarioFormulario(request.POST) #Aqui me llega toda la info del html

        print(miFormulario)

        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data

            usuario.nombre = informacion['nombre']
            usuario.apellido = informacion['apellido']
            usuario.email = informacion['email']

            usuario.save()

            return render(request,"WebDjango/inicio.html") #vuelvo al inicio
#Si no es post
    else:
        miFormulario= UsuarioFormulario(initial={"nombre":usuario.nombre,"apellido":usuario.apellido,"email":usuario.email})

    return render(request,"WebDjango/Usuarios/usuarios.html", {"miFormulario":miFormulario, "usuario_nombre": usuario_nombre})


#--------------------------------------------------------ARTICULOS--------------------------------------------------------

#Esta función muestra el formulario
def articulos(request):
    if request.method == "POST":
        elFormulario = ArticuloFormulario(request.POST) #Aqui me llega la informacion del html
        print(elFormulario)

        if elFormulario.is_valid():
            informacion = elFormulario.cleaned_data
            articulo = Articulo( nombre = informacion["nombre"], cantidad=informacion['cantidad'])
            articulo.save()
            return render(request, "WebDjango/inicio.html")
    
    else:
        elFormulario = ArticuloFormulario()
    
    return render(request, "WebDjango/Articulos/articulos.html", {"elFormulario":elFormulario})



def busquedaNombre(request):
    return render(request, "WebDjango/Articulos/busquedaNombre.html")


#Esta función busca los datos registrados 
def buscarNombre(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        articulos = Articulo.objects.filter(nombre__icontains=nombre)
        return render(request,'WebDjango/Articulos/articuloresp.html', {"articulos":articulos, "nombre":nombre})
    else:
        respuesta ="No enviaste datos."
    return render(request,'WebDjango/Articulos/articuloresp.html',{"respuesta":respuesta})


#Esta funcion lee los usuarios
def leerArticulos(request):

    articulos = Articulo.objects.all() #Trae todos los articulos

    contexto= {"articulos": articulos}

    return render(request, "WebDjango/Articulos/leerArticulos.html", contexto)


def eliminarArticulo(request, articulo_nombre):

    articulo = Articulo.objects.get(nombre = articulo_nombre)
    articulo.delete()

    #vuelvo al menú
    articulos = Articulo.objects.all() #Trae todos los articulos

    contexto= {"articulos":articulos}

    return render(request,"WebDjango/Articulos/leerArticulos.html", contexto)

def editarArticulo(request, articulo_nombre):

    #Recibe el nombre del articulo a moificar
    articulo = Articulo.objects.get(nombre=articulo_nombre)

    #Si es metodo Post hago lo mismo que el agregar
    if request.method =="POST":

        elFormulario = ArticuloFormulario(request.POST) #Aqui me llega toda la info del html

        print(elFormulario)

        if elFormulario.is_valid():
            
            informacion = elFormulario.cleaned_data

            articulo.nombre = informacion['nombre']
            articulo.cantidad = informacion['cantidad']

            articulo.save()

            return render(request,"WebDjango/inicio.html") #vuelvo al inicio
#Si no es post
    else:
        elFormulario= ArticuloFormulario(initial={"nombre":articulo.nombre,"cantidad":articulo.cantidad})

    return render(request,"WebDjango/Articulos/articulos.html", {"elFormulario":elFormulario, "articulo_nombre": articulo_nombre})

#--------------------------------------------------------ENVIOS--------------------------------------------------------

#Esta función muestra el formulario
def envios(request):
    if request.method == "POST":
        miFormulario = EnvioFormulario(request.POST) #Aqui me llega la informacion del html
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            envio = Envio(fecha=informacion['fecha'], recibido=informacion['recibido'])
            envio.save()
            return render(request, "WebDjango/inicio.html")
    
    else:
        miFormulario = EnvioFormulario()

    return render(request, "WebDjango/Envios/envios.html", {"miFormulario":miFormulario})


class EnvioList(ListView):
    model = Envio
    template_name ="WebDjango/Envios/envios_list.html"

class EnvioDetalle(DetailView):
    model = Envio
    template_name ="WebDjango/Envios/envios_detalle.html"

class EnvioCreacion(CreateView):
    model = Envio
    success_url = "/WebDjango/envio/list"
    fields= ['fecha', 'recibido']

class EnvioUpdate(UpdateView):
    model = Envio
    success_url = "/WebDjango/envio/list"
    fields= ['fecha', 'recibido']

class EnvioDelete(DeleteView):
    model = Envio
    success_url = "/WebDjango/envio/list"