from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ProductoViewset
from .views import agregar_productos

#Definir un router
router = SimpleRouter()
router.register(r'api', ProductoViewset)

#ProductoViewset:
#ip:8000/productos/api]/ <--- GET de todo
#ip:8000/productos/api/{id} <--- POST, PUT, DELETE

urlpatterns = [
    path('', include(router.urls)),
    path('agregar/', agregar_productos, name='agregar_productos')
]