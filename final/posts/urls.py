from django.urls import path
from . import views
#from .views import BlogView, PostDetailView, AgregarPostView, EditarPostView, BorrarPostView
from .views import *
app_name='posts'

urlpatterns = [

    path('blog/', BlogView.as_view(), name='blog'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='postdetail'),
    path('crear/', AgregarPostView.as_view(), name='crear_post'),
    path('post/editar/<int:pk>/', EditarPostView.as_view(), name='editar'),
    path('post/<int:pk>/borrar', BorrarPostView.as_view(), name='borrar'),
]