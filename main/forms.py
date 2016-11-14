# -*- coding:utf-8 -*-
from django import forms

from .models import Restaurante

class RestauranteForm(forms.ModelForm):

    class Meta:
        model = Restaurante
        fields = ('nombre', 'telefono', 'direccion', 'sitioweb', 'informacion', 'image' )
        labels = { 'nombre': 'Nombre del Restaurante', 
        			'telefono': 'Telefono', 
        			'direccion': 'Direccion', 
        			'sitioweb': 'Sitio Web', 
        			'informacion': 'Información', 
        			'image': 'Seleccione una imágen' 
        		  }
        widgets = { 'nombre': forms.TextInput(attrs={'class':'form-control'}),
        			'telefono': forms.TextInput(attrs={'class':'form-control'}),
        			'direccion': forms.TextInput(attrs={'class':'form-control'}),
        			'sitioweb': forms.TextInput(attrs={'class':'form-control'}),
        			'informacion': forms.Textarea(attrs={'class':'form-control'}),
        			'imagen': forms.TextInput(attrs={'class':'form-control'}),
        		  }