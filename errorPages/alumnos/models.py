from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    matricula = models.CharField(max_length=11, unique=True)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre
