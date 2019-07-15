from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

class Register(models.Model):
    name = models.CharField(max_length=40)
    occup = models.CharField(max_length=15)
    username = models.CharField(max_length=20)
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.name
