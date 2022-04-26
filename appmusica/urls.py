from unicodedata import name
from django import views
from django.urls import URLPattern, path
from appmusica.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('login/', login_request, name="login"),
    path('register/', register_request, name="register"),
    path('logout/', LogoutView.as_view(template_name="appmusica/logout.html"), name="logout"),
    
    path('estudiantes/', estudiantes, name="Estudiantes"),
    path('profesores/', profesores, name="Profesores"),
    path('cursos/', cursos, name="Cursos"),
    path('cursoformulario/', formulario_curso, name='Formulario'),
    path('buscarcurso/', buscarCurso, name='BusquedaCurso'),
    path('borrarcurso/<camada_id>', borrar_curso, name="eliminarCurso"),
    path('update_curso/<camada_id>/', actualizar_curso),

    path("curso/list", CursoLista.as_view(), name="curso_list"),
    path("curso/nuevo/", CursoCrear.as_view(), name="curso_create"),
    path("curso/detalle/<pk>/", CursoDetalle.as_view(), name="curso_detail"),
    path("curso/editar/<pk>/", CursoActualizar.as_view(), name="curso_update"),
    path("curso/borrar/<pk>/", CursoBorrar.as_view(), name="curso_delete"),

    path('about/', about, name="About")
]