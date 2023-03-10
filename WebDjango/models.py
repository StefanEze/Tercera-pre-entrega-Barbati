from django.db import models


# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    fecha_de_nacimiento = models.CharField(max_length=30)

class Articulo(models.Model):
    nombres = models.CharField(max_length=35)
    cantidad = models.IntegerField()

class Envio(models.Model):
    fecha = models.DateField()
    recibido = models.BooleanField()