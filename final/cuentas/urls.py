from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('blog/', views.blog, name='blog'),
    path('blog_posts/', views.blog_posts),
    path('registro/', views.registro, name="registro"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logoutUser, name='logout'),
    path('crear_post/', views.crear_post, name='crear_post')
]