from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} --- Emaill: {self.email}"

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