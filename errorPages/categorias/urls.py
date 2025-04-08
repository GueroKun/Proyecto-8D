from django.urls import path
from .views import *

urlpatterns = [
    path('registrar/', agregar_categorias, name='agregarCategoria'),
    path('api/get', lista_categorias, name='listaCategoria'),
    path('verCategoria/', ver_categorias, name='verCategoria'),
    path('json/', categorias_json, name='categorias'),
    path('api/post/', registrar_categoria, name='post')
]