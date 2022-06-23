from django.shortcuts import render
from django.http import HttpResponse

def home(request): #aca van a estar los login y register
    return render(request, 'cuentas/home.html')


def blog(request): #pagina post-login para ver el blog
    return render(request, 'cuentas/blog.html')

def profile(request): #pagina de perfil de usuario
    return render(request, 'cuentas/profile.html')

def blog_posts(request): #pagina individual de cada post en el blog
    return HttpResponse("Blog posts")

