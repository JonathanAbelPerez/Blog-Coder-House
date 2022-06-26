from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Perfil(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, upload_to="avatar/")
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.user)