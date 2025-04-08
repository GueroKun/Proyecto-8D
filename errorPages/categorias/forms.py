from django import forms
from .models import Categoria

class categoriaForm(forms.ModelForm):
    #Meta es la clase que define la informacion del formulario
    class Meta:
        # De que modelo se basa este formulario
        model = Categoria

        # Campos que se van a mostrar en el formulario
        fields = ['nombre', 'imagen']

        # personalizar la apariencia del formulario (widgets)
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre de la categoria'
                }
            ),
            'imagen': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'URL de la imagen de la categoria'
                }
            )
        }

        #Personalizar las etiquetas
        labels = {
            'nombre': 'Nombre de la categoria',
            'imagen': 'URL de la imagen de la categoria'
        }

        #Mensajes de error personalizados
        error_messages = {
            'nombre': {
                'required': 'El nombre de la categoria es obligatorio',
            },
            'imagen': {
                'required': 'La URL de la imagen de la categoria es obligatoria',
            }
        }
