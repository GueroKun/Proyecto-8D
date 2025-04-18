from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    # Los campos urlField limitan la longitud de la url a 200 caracteres
    imagen = models.URLField()

    def __str__(self):
        return self.nombre
