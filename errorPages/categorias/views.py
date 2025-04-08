from django.shortcuts import render, redirect
from .models import Categoria
from .forms import categoriaForm
from django.http import JsonResponse

# Create your views here.
def agregar_categorias(request):
    if request.method == 'POST':
        form = categoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregarCategoria')
    else:
        form = categoriaForm()
        return render(request, 'agregarCategoria.html', {'form': form})

import json
def registrar_categoria(request):
    if request.method == 'POST': 
        try:
            data = json.loads(request.body) # Funcion que convierte texto crudo y lo convierte en JSON
            categoria = Categoria.objects.create(
                nombre = data['nombre'],
                imagen = data['imagen']
            ) # estamos construyendo la instancia y guardandola en la BD
            return JsonResponse({
                'mensaje': 'Categoria registrada correctamente',
                'id': categoria.id
            }, status=201)
        except Exception as e:
            return JsonResponse({
                'Error': 'Ocurrio un error:'+str(e)
            }, status=400)
    return JsonResponse({
        'Error': 'Metodo no soportado'
        }, status=405)

def ver_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'verCategoria.html', {'categorias': categorias})

def categorias_json(request):
    return render(request, 'categorias.html')

def lista_categorias(request):
    categorias = Categoria.objects.all()
    data = [
        {
            'nombre': c.nombre,
            'imagen': c.imagen
        }
        for c in categorias
    ]

    return JsonResponse(data, safe=False)