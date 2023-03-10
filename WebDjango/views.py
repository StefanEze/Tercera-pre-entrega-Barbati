from django.shortcuts import render
from WebDjango.models import *
from WebDjango.forms import *

# Create your views here.

def inicio(request):
    return render(request,"WebDjango/inicio.html")



#--------------------------------------------------------USUARIOS--------------------------------------------------------

def usuarios(request):
    if request.method == "POST":
        miFormulario = UsuarioFormulario(request.POST) #Aqui me llega la informacion del html
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            usuario = Usuario(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            usuario.save()
            return render(request, "WebDjango/inicio.html")
    else:
        miFormulario = UsuarioFormulario()
    return render(request, "WebDjango/usuarios.html", {"miFormulario":miFormulario})



def busquedaEmail(request):
    return render(request, "WebDjango/busquedaEmail.html")



def buscar(request):
    if request.GET['email']:
        email = request.GET['email']
        usuarios = Usuario.objects.filter(email__icontains=email)
        return render(request,'WebDjango/usuarioresp.html', {"usuarios":usuarios, "email":email})
    else:
        respuesta ="No enviaste datos."
    return render(request,'WebDjango/usuarioresp.html',{"respuesta":respuesta})



#--------------------------------------------------------ARTICULOS--------------------------------------------------------

def articulos(request):
    if request.method == "POST":
        elFormulario = ArticuloFormulario(request.POST) #Aqui me llega la informacion del html
        print(elFormulario)

        if elFormulario.is_valid:
            informacion = elFormulario.cleaned_data
            articulo = Articulo( nombres = informacion["nombres"], cantidad=informacion['cantidad'])
            articulo.save()
            return render(request, "WebDjango/inicio.html")
    
    else:
        elFormulario = ArticuloFormulario()
    
    return render(request, "WebDjango/articulos.html", {"elFormulario":elFormulario})



def busquedaNombre(request):
    return render(request, "WebDjango/busquedaNombre.html")



def buscarNombre(request):
    if request.GET['nombres']:
        nombres = request.GET['nombres']
        articulos = Articulo.objects.filter(nombre__icontains=nombres)
        return render(request,'WebDjango/articuloresp.html', {"articulos":articulos, "nombres":nombres})
    else:
        respuesta ="No enviaste datos."
    return render(request,'WebDjango/articuloresp.html',{"respuesta":respuesta})


#--------------------------------------------------------ENVIOS--------------------------------------------------------

def envios(request):
    if request.method == "POST":
        miFormulario = EnvioFormulario(request.POST) #Aqui me llega la informacion del html
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            envio = Envio(fecha=informacion['fecha'], recibido=informacion['recibido'])
            envio.save()
            return render(request, "WebDjango/inicio.html")
    
    else:
        miFormulario = EnvioFormulario()
    
    return render(request, "WebDjango/envios.html", {"miFormulario":miFormulario})



def busquedaNombre(request):
    return render(request, "WebDjango/busquedaNombre.html")



def buscarNombre(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        articulos = Articulo.objects.filter(nombre__icontains=nombre)
        return render(request,'WebDjango/usuarioresp.html', {"articulos":articulos, "nombre":nombre})
    else:
        respuesta ="No enviaste datos."
    return render(request,'WebDjango/articuloresp.html',{"respuesta":respuesta})

