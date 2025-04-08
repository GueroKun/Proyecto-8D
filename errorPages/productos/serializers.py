from rest_framework import serializers
from .models import Producto

# Es una clase que actua sobre un modelo
class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ' _all_' # <-- Todos los campos
