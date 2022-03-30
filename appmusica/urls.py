from django.urls import URLPattern, path
from appmusica.views import *

urlpatterns = [
    path('', inicio),
    path('estudiantes/', estudiantes),
    path('profesores/', profesores),
    path('cursos/', cursos),
]