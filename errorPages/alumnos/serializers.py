from rest_framework import serializers
from .models import Alumno

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__' #<--- todos los campos del modelo