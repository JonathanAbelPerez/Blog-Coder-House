from audioop import reverse
import django
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import generic
from .forms import CrearUsuarioForm, ActualizarUsuarioForm

"""----------------------- VISTAS GENERALES ----------------------------"""
@login_required(login_url='login')
def profile(request): #pagina de perfil de usuario
    return render(request, 'cuentas/profile.html')

class EditarUsuarioView(generic.UpdateView):
    form_class = ActualizarUsuarioForm
    template_name = 'cuentas/editar_perfil.html'
    success_url = reverse_lazy('profile')
    def get_object(self):
        return self.request.user



"""------------------------- LOGIN-LOGOUT-REGISTRO-----------------------"""
def registro(request):
    if request.user.is_authenticated:
        return redirect('posts:blog')
    else:
        form = CrearUsuarioForm()
        if request.method == "POST":
            form = CrearUsuarioForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "La cuenta " + user + " ha sido creada con exito")
                return redirect('login')

        context = {'form':form}
        return render(request, 'cuentas/registro.html', context)

def login_user(request):
    if request.user.is_authenticated:
        return redirect('posts:blog')
    else:
        if request.method=="POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
            
                username= form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")

                user = authenticate(username= username, password= password)
                if user is not None:
                    login(request, user)
                    return redirect('posts:blog')
                else:
                    messages.info(request, 'Usuario o contraseña incorrecto')
        context={}
        return render(request, 'cuentas/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

