from django import forms

class CursoFormulario(forms.Form):

    #campos del formulario
    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()