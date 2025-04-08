from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .models import Producto
from .serializers import ProductoSerializers
from .forms import productoForm
from django.shortcuts import render

class ProductoViewset(viewsets.ModelViewSet):
    #Conjunto de query's de la  BD
    queryset = Producto.objects.all()

    #Saber como empaquetar e enviar la informacion
    serializer_class = ProductoSerializers

    #Saber como voy a renderizar las respuestas
    renderer_classes = [JSONRenderer]

def agregar_productos(request):
        form = productoForm()
        return render(request, 'agregar.html', {'form': form})