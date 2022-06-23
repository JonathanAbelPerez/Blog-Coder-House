from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length= 255, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body= models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)