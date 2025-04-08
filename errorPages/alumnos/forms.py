from django import forms
from .models import Alumno

class alumnoForm(forms.ModelForm):
    #Meta es la clase que define la informacion del formulario
    class Meta:
        # De que modelo se basa este formulario
        model = Alumno

        # Campos que se van a mostrar en el formulario
        fields = ['nombre', 'apellido', 'edad', 'matricula', 'correo']

        # personalizar la apariencia del formulario (widgets)
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del alumno'
                }
            ),
             'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellido del alumno'
                }
            ),
            'edad': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Edad del alumno'
                }
            ),
            'matricula': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Matricula del alumno'
                }
            ),
            'correo': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo del alumno'
                }
            ),
            
        }

        #Personalizar las etiquetas
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'edad': 'Edad',
            'matricula': 'Matricula',
            'correo': 'Correo electronico'
        }

        #Mensajes de error personalizados
        error_messages = {
            'nombre': {
                'required': 'El nombre del alumno es obligatorio',
            },
            'apellido': {
                'required': 'El apellido del alumno es obligatorio',
            },
            'edad': {
                'required': 'La edad del alumno es obligatorio',
            },
            'matricula': {
                'required': 'La matricula del alumno es obligatorio',
            },
            'correo': {
                'required': 'El correo del alumno es obligatorio',
            }
        }
