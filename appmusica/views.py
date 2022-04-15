from re import template
from traceback import print_tb
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from appmusica.models import Curso, Profesor, Estudiante
from appmusica.forms import CursoFormulario



#Vistas basadas en clases
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def inicio(request):
    return render(request, "appmusica/index.html")
# Create your views here.
def cursos(request):
    print(request)

    cursos = Curso.objects.all()

    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            curso = Curso(data['nombre'], data['camada'])
            curso.save()

            return redirect('Inicio')
    else:   
        
        formulario = CursoFormulario()
        return render(request, "appmusica/cursos.html", {"cursos": cursos, "title": "Cursos", "page": "Cursos", "formulario": formulario})

def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, "appmusica/estudiantes.html", {"estudiantes": estudiantes, "title": "Estudiantes", "page": "Estudiantes"})

def profesores(request):
    profesores = Profesor.objects.all()
    return render(request, "appmusica/profesores.html", {"profesores": profesores})



def formulario_curso(request):

    if request.method == "POST":
        curso = CursoFormulario(request. POST) #ES PARA ASIGNAR A CADA CAMPO EL VALOR QUE CORRESPONDE
        print(curso)

        if curso.is_valid:   #Si pasó la validacion de django
            data = curso.cleaned_data

            curso_nuevo = Curso(data['nombre'], data['camada'])
            curso_nuevo.save()
        return render(request, 'appmusica/index.html')
    else:
        curso_form = CursoFormulario()
        return render(request, 'appmusica/cursosFormulario.html',{"formulario":curso_form})
    

def buscarCurso(request):

    data = request.GET.get("camada")
    print(data)
    if data: 
        curso = Curso.objects.filter(camada__icontains=data)
        print(curso)

        return render(request, 'appmusica/busquedaCurso.html', {"curso": curso[0], "id":data})

    return render(request, 'appmusica/busquedaCurso.html')


def borrar_curso(request, camada_id):
    try:
        curso = Curso.objects.get(camada=camada_id)
        curso.delete()

        return render(request, "appmusica/index.html")
    except Exception as exc:
        return render(request, "appmusica/index.html")
 
def actualizar_curso(request, camada_id):

    curso = Curso.objects.get(camada=camada_id)


    if request.method == "POST":
        formulario = CursoFormulario(request.POST)
        
        if formulario.is_valid():

            informacion = formulario.cleaned_data


            curso.nombre = informacion["nombre"]
            
            curso.save()

            return render(request, "appmusica/index.html")

    else:

        formulario = CursoFormulario(initial={"nombre": curso.nombre, "camada": curso.camada})

        return render(request, "appmusica/update_curso.html", {"formulario": formulario, "camada_id":camada_id})

class CursoLista(ListView):
    model = Curso
    template_name = "appmusica/cursos_list.html"

class CursoDetalle(DetailView):

    model = Curso
    template_name = "appmusica/curso_detalle.html"

class CursoCrear(CreateView):

    model = Curso
    success_url = "/appmusica/curso/list" #Renderiza en list
    fields = ['nombre', 'camada'] #Campos que aparecen en el formulario

class CursoActualizar(UpdateView):

    model = Curso
    success_url = "/appmusica/curso/list" 
    fields = ['nombre']

class CursoBorrar(DeleteView):
    model = Curso
    success_url = "/appmusica/curso/list" 
    fields = ['nombre']