from django.urls import path
from . import views
from .views import BlogView, PostDetailView

app_name='posts'

urlpatterns = [

    path('blog/', BlogView.as_view(), name='blog'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='postdetail'),
    path('crear/', views.crear_post, name='crear_post')
    
]