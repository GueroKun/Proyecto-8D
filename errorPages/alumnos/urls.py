from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import AlumnoViewSet
from .views import agregar_alumnos

#Definir un router
router = SimpleRouter()
router.register(r'api', AlumnoViewSet)

#AlumnoVieSet:
#ip:8000/alumnos/api/ <--- GET de todo
#ip:8000/alumnos/api/{id} <--- GET, POST, DELETE de uno

urlpatterns = [
    path('', include(router.urls)),
     path('registrar/', agregar_alumnos, name='agregarAlumno'),
]