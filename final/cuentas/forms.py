from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Perfil

class CrearUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ActualizarUsuarioForm(forms.ModelForm):
    class Meta:
        model= User
        fields= ('username', 'email', 'first_name', 'last_name')
        widgets= {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
        }

class CambiarAvatarForm(forms.ModelForm):
    class Meta:
        model= Perfil
        fields= ('avatar', 'bio')
        widgets={
            'bio': forms.Textarea(attrs={'class':'form-control'})
        }
       