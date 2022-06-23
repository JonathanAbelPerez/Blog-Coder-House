import django
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CrearUsuarioForm

"""----------------------- VISTAS GENERALES ----------------------------"""

def home(request): #aca van a estar los login y register
    return render(request, 'cuentas/home.html')

@login_required(login_url='home')
def blog(request): #pagina post-login para ver el blog
    return render(request, 'cuentas/blog.html')

@login_required(login_url='home')
def profile(request): #pagina de perfil de usuario
    return render(request, 'cuentas/profile.html')

@login_required(login_url='home')
def blog_posts(request): #pagina individual de cada post en el blog
    return HttpResponse("Blog posts")

@login_required(login_url='home')
def crear_post(request):
    return render(request, 'cuentas/crear_post.html')


"""------------------------- LOGIN-LOGOUT-REGISTRO-----------------------"""
def registro(request):
    if request.user.is_authenticated:
        return redirect('blog')
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
        return redirect('blog')
    else:
        if request.method=="POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
            
                username= form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")

                user = authenticate(username= username, password= password)
                if user is not None:
                    login(request, user)
                    return redirect('blog')
                else:
                    messages.info(request, 'Usuario o contraseña incorrecto')
        context={}
        return render(request, 'cuentas/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

