from multiprocessing import context, get_context
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import PostForm
from django.urls import reverse_lazy

from .models import Post

# Create your views here.
@method_decorator(login_required(login_url='login'), name="dispatch")
class BlogView(ListView):
    model = Post
    template_name = 'posts/blog.html'
    ordering = ['-id']

@method_decorator(login_required(login_url='login'), name="dispatch")
class PostDetailView(DetailView):
    model= Post
    template_name = "posts/blogposts.html"

@method_decorator(login_required(login_url='login'), name="dispatch")
class AgregarPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name= 'posts/crear_post.html'
    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user if user else None
        return super(AgregarPostView, self).form_valid(form)
    
@method_decorator(login_required(login_url='login'), name="dispatch")
class EditarPostView(UpdateView):
    model = Post
    template_name= 'posts/editar_post.html'
    form_class = PostForm

class BorrarPostView(DeleteView):
    model = Post
    template_name = 'posts/borrar_post.html'
    success_url= reverse_lazy('posts:blog')

