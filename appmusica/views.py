from django.http import HttpResponse
from django.shortcuts import render


def inicio(request):
    return render(request, "appmusica/index.html")
# Create your views here.
def estudiantes(request):
    return render(request, "appmusica/estudiantes.html")

def profesores(request):
    return render(request, "appmusica/profesores.html")

def cursos(request):
    return render(request, "appmusica/cursos.html")

def formulario_curso(request):

    datos = request.method
    print(datos)

    return render(request, 'appmusica/cursosFormulario.html')

