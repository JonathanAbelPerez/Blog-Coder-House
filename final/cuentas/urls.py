from unicodedata import name
from django.urls import path
from . import views
from .views import *

urlpatterns = [

    path('profile/', views.profile, name='profile'),
    path('registro/', views.registro, name="registro"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/editar_perfil', EditarUsuarioView.as_view(), name='editar_perfil'),
    path('profile/editar_avatar/', CambiarAvatarView.as_view(), name='editar_avatar'),
]