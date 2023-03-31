from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Publicacion(models.Model):
    titulo = models.CharField(max_length=60)
    subtitulo = models.CharField(max_length=60)
    cuerpo = models.CharField(max_length=500)
    autor =models.CharField(max_length=30)
    fecha= models.DateField(default=datetime.now)
    imagen= models.ImageField(null=True, blank=True, upload_to="media/")
    
    def __str__(self):
        return f"{self.titulo}, publicado por {self.autor}"

class Articulo(models.Model):
    nombre = models.CharField(max_length=35)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}"

class Envio(models.Model):
    fecha = models.DateField()
    recibido = models.BooleanField()

    def __str__(self):
        return f"Fecha de envio: {self.fecha} --- Entregado: {self.recibido}"
    

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)