from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from .models import Post

# Create your views here.
@method_decorator(login_required(login_url='login'), name="dispatch")
class BlogView(ListView):
    model = Post
    template_name = 'posts/blog.html'


#@login_required(login_url='login')
#def blog_posts(request): #pagina individual de cada post en el blog
#    return render(request, 'posts/blogposts.html')


@login_required(login_url='login')
def crear_post(request):
    return render(request, 'posts/crear_post.html')

class PostDetailView(DetailView):
    model= Post
    template_name = "posts/blogposts.html"