from re import template
from traceback import print_tb
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from appmusica.models import Curso, Profesor, Estudiante, Avatar
from appmusica.forms import AvatarFormulario, CursoFormulario, UsuarioRegistroForm, UsuarioEditForm



#Vistas basadas en clases
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#Autenticacion django
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def inicio(request):
    
    avatar= Avatar.objects.filter(user=request.user)

    if len(avatar) > 0:
        imagen= avatar[0].imagen.url

    dict_ctx = {"title": "Inicio", "page": "Inicio", "imagen_url": imagen}
    return render(request, "appmusica/index.html", dict_ctx)
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

def about(request):
    return render(request, 'appmusica/about.html')

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

class CursoLista(ListView, LoginRequiredMixin):
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

def login_request(request):

    if request.method == "POST":

        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            nombre_usuario = data.get("username")
            contrasenia = data.get("password")

            usuario = authenticate(username=nombre_usuario, password=contrasenia)

            if usuario is not None:
                login(request, usuario)
                
                dict_ctx = {"title": "Inicio", "page": usuario }
                return render(request, "appmusica/index.html", dict_ctx)
            else:
                dict_ctx = {"title": "Inicio", "page": usuario, "errors": ["El usuario no existe"] }
                return render(request, "appmusica/index.html", dict_ctx)
        else:
            dict_ctx = {"title": "Inicio", "page": "anonymous", "errors": ["Revise los datos indicados en el form"] }
            return render(request, "appmusica/index.html", dict_ctx)
    else:
        form = AuthenticationForm()
        return render(request, "appmusica/login.html", {"form": form})

def register_request(request):

    if request.method =="POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            form.save()

            dict_ctx = {"title": "Inicio", "page":usuario}
            return render(request, "appmusica/index.html", dict_ctx)
        else:
            dict_ctx = {"title": "Inicio", "page":"anonymous", "errors":["No paso las validaciones"] }
            return render(request, "appmusica/index.html", dict_ctx)
    else:
        form = UsuarioRegistroForm()
        return render(request, "appmusica/register.html", {"form":form})

@login_required()
def actualizar_usuario(request):

    usuario= request.user

    if request.method == "POST":
        formulario = UsuarioEditForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]
            usuario.last_name = data["last_name"]
            usuario.first_name = data["first_name"]

            usuario.save()

            return redirect("Inicio")
        else:
            formulario = UsuarioEditForm(initial={"email": usuario.email})
            return render(request, "appmusica/editar_usuario.html", {"form": formulario, "errors": ["Datos invalidos"]})

    else:
        formulario = UsuarioEditForm(initial={"email": usuario.email})
        return render(request, "appmusica/editar_usuario.html", {"form": formulario})

@login_required()
def cargar_imagen(request):

    if request.method == "POST":

        formulario = AvatarFormulario(request.POST,request.FILES)

        if formulario.is_valid():

            usuario = request.user

            avatar = Avatar.objects.filter(user=usuario)

            if len(avatar) > 0:
                avatar = avatar[0]
                avatar.imagen = formulario.cleaned_data["imagen"]
                avatar.save()

            else:
                avatar = Avatar(user=usuario, imagen=formulario.cleaned_data["imagen"])
                avatar.save()
            
        return redirect("Inicio")
    else:

        formulario = AvatarFormulario()
        return render(request, "appmusica/cargar_imagen.html", {"form": formulario})