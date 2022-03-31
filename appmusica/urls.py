from django.urls import URLPattern, path
from appmusica.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('estudiantes/', estudiantes, name="Estudiantes"),
    path('profesores/', profesores, name="Profesores"),
    path('cursos/', cursos, name="Cursos"),
    path('cursoformulario/', formulario_curso, name='Formulario'),

]