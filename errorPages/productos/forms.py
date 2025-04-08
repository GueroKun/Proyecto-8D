#Define los formularios de los modelos en esta app
from django import forms
from .models import Producto

#Se debe crear una clases para cada modlo
class productoForm(forms.ModelForm):
    #Meta es la clase que define la informacion del formulario
    class Meta:
        # De que modelo se basa este formulario
        model = Producto

        # Campos que se van a mostrar en el formulario
        fields = ['nombre', 'precio', 'imagen', 'categoria']

        # personalizar la apariencia del formulario (widgets)
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Nombre del producto'
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Precio del producto'
                }
            ),
            'imagen': forms.URLInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'URL de la imagen del producto'
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class': 'form-input'
                }
            )
        }

        #Personalizar las etiquetas
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio del producto',
            'imagen': 'URL de la imagen del producto',
            'categoria': 'Categoria del producto'
        }

        #Mensajes de error personalizados
        error_messages = {
            'nombre': {
                'required': 'El nombre del producto es obligatorio',
            },
            'precio': {
                'required': 'El precio del producto es obligatorio',
                'invalid': 'El precio del producto debe ser un número valido',
            },
            'imagen': {
                'required': 'La URL de la imagen del producto es obligatoria',
            }
        }
