from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('profile/', views.profile),
    path('blog/', views.blog),
    path('blog_posts/', views.blog_posts),
    
]