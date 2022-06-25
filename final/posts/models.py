from audioop import reverse
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length= 255, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo= models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.titulo + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('posts:postdetail', args=(str(self.id)) )