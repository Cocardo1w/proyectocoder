from dataclasses import fields
import email
from urllib import request
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comentarios, Entrada

class CursoFormulario(forms.Form):

    #campos del formulario
    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()

class UsuarioRegistroForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label='contrasenia1', widget=forms.PasswordInput)
    password1 = forms.CharField(label='contrasenia2', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_text = {k: "" for k in fields}

class UsuarioEditForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label='Contrasenia 1', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Contrasenia 2', widget=forms.PasswordInput)

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ['first_name','last_name','email', 'password1', 'password2']
        help_text = { k: "" for k in fields}

class Comentariosform(forms.ModelForm):

    class Meta:
        model = Comentarios
        fields = ('nombre','contenido')

        
class AvatarFormulario(forms.Form):

    imagen = forms.ImageField()