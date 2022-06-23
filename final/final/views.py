from django.shortcuts import render


def home(request): #aca van a estar los login y register
    return render(request, 'cuentas/home.html')