from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class PublicacionFormulario(forms.Form):
    titulo = forms.CharField(max_length=60)
    subtitulo = forms.CharField(max_length=60)
    cuerpo = forms.CharField(max_length=500)
    autor =forms.CharField(max_length=30)
    date = forms.DateField()
    image = forms.ImageField()

class ArticuloFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    cantidad = forms.IntegerField()

class EnvioFormulario(forms.Form):
    fecha = forms.DateField()
    recibido = forms.BooleanField()

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la Contraseña", widget = forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "last_name", "first_name"]
        #Sacamos los mensajes de ayuda
        help_texts = {k:"" for k in fields}


class UserEditForm(UserChangeForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la Contraseña", widget = forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = [ "email", "password1", "password2", "last_name", "first_name"]
        #Sacamos los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class AvatarFormulario(forms.Form):
    username=forms.ModelChoiceField(queryset=User.objects.all())
    imagen = forms.ImageField(required=True)

    class Meta:
        model = User
        fields =['imagen']
        help_texts = {k:"" for k in fields}