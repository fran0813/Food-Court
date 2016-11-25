from django import forms

from .models import Restaurante, Platillo, Comentario

class RestauranteForm(forms.ModelForm):

    class Meta:
        model = Restaurante
        fields = ('__all__' )
        exclude = ('restaurante_cliente',)
        labels = { 'nombre': 'Nombre del Restaurante', 
        			'telefono': 'Telefono', 
        			'direccion': 'Direccion', 
        			'sitioweb': 'Sitio Web', 
        			'informacion': 'Informacion', 
        			# 'image': 'Seleccione una imagen' 
        		  }
        widgets = { 'nombre': forms.TextInput(attrs={'class':'form-control'}),
        			'telefono': forms.TextInput(attrs={'class':'form-control'}),
        			'direccion': forms.TextInput(attrs={'class':'form-control'}),
        			'sitioweb': forms.TextInput(attrs={'class':'form-control'}),
        			'informacion': forms.Textarea(attrs={'class':'form-control'}),
        			# 'image': forms.TextInput(attrs={'class':'form-control'}),
        		  }


class PlatilloForm(forms.ModelForm):

    class Meta:
        model = Platillo
        fields = ('nombre', 'precio', 'detalle', 'restaurante_platillo' )
        labels = { 'nombre': 'Nombre del Platillo', 
        			'precio': 'Precio', 
        			'detalle': 'Descripcion', 
        			'restaurante_platillo' : 'Restaurante',
        		  }
        widgets = { 'nombre': forms.TextInput(attrs={'class':'form-control'}),
        			'precio': forms.TextInput(attrs={'class':'form-control'}),
        			'detalle': forms.TextInput(attrs={'class':'form-control'}),
        			'restaurante_platillo': forms.Select(attrs={'class':'form-control'}),
        		  }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(PlatilloForm, self).__init__(*args, **kwargs)
        # import pdb; pdb.set_trace()
        self.fields['restaurante_platillo'].queryset = Restaurante.objects.filter( restaurante_cliente_id = user.id )

class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('comentarios',)
        labels = {'comentarios':'Comentario'}
        widgets = { 'comentarios': forms.Textarea(attrs={'class':'form-control'})}