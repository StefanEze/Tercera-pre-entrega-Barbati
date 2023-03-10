from django import forms
from django.db import models


class UsuarioFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    email=forms.EmailField()

class ArticuloFormulario(forms.Form):
    nombres = models.CharField(max_length=30)
    cantidad = models.IntegerField()

class EnvioFormulario(forms.Form):
    fecha = models.DateField()
    recibido = models.BooleanField()