from django.shortcuts import render
from WebDjango.models import *
from WebDjango.forms import *


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
    return render(request, "WebDjango/usuarios.html", {"miFormulario":miFormulario})



def busquedaEmail(request):
    return render(request, "WebDjango/busquedaEmail.html")


#Esta función busca los datos registrados 
def buscar(request):
    if request.GET['email']:
        email = request.GET['email']
        usuarios = Usuario.objects.filter(email__icontains=email)
        return render(request,'WebDjango/usuarioresp.html', {"usuarios":usuarios, "email":email})
    else:
        respuesta ="No enviaste datos."
    return render(request,'WebDjango/usuarioresp.html',{"respuesta":respuesta})



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
    
    return render(request, "WebDjango/articulos.html", {"elFormulario":elFormulario})



def busquedaNombre(request):
    return render(request, "WebDjango/busquedaNombre.html")


#Esta función busca los datos registrados 
def buscarNombre(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        articulos = Articulo.objects.filter(nombre__icontains=nombre)
        return render(request,'WebDjango/articuloresp.html', {"articulos":articulos, "nombre":nombre})
    else:
        respuesta ="No enviaste datos."
    return render(request,'WebDjango/articuloresp.html',{"respuesta":respuesta})


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

    return render(request, "WebDjango/envios.html", {"miFormulario":miFormulario})
