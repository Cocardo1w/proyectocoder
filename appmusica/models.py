from distutils.command.upload import upload
from time import timezone
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Entrada(models.Model):
    nombre = models.CharField(max_length=40)
    contenido = models.TextField(max_length=800)
    imagen = models.URLField()
    autor = models.CharField(max_length=40)
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre



class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField(primary_key=True)

    def __str__(self):
        return f"{self.nombre} | {self.camada}"


class Estudiante(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} | {self.apellido}"

class Profesor(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.nombre} | {self.apellido} | {self.profesion}"

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

 


