from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .models import Alumno
from .serializers import AlumnoSerializer
from .forms import alumnoForm
from django.shortcuts import render

class AlumnoViewSet(viewsets.ModelViewSet):
    #conojunto de querys de la base de datos
    queryset = Alumno.objects.all()

    #sabes como empaquetar y enviar la informacion
    serializer_class = AlumnoSerializer

    #sabes como renderizar la informacion
    renderer_classes = [JSONRenderer]
    
def agregar_alumnos(request):
        form = alumnoForm()
        return render(request, 'Castañeda_Christian.html', {'form': form})
