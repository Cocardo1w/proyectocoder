import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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