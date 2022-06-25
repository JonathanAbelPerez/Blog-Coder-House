from dataclasses import fields
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields= ('titulo', 'cuerpo')
        widgets= {
            'titulo': forms.TextInput(attrs={'class': 'form-control','placeholder':'Agregar un titulo...'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribir un artículo...'}),
        }
