from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    Gender = models.CharField(max_length=20, blank=True)
    Profile_pic = models.ImageField(default="static/blog.jpg",upload_to='static/')
    Bios = models.TextField(default="", blank=True)

# # Create your models here.
# class blog_data(models.Model):
#     blog_title = models.CharField(max_length=100, default=None)
#     blog_text = models.TextField(max_length=10000)
#     time_post = models.DateTimeField(auto_now_add=True)
#     blog_catagory=models.CharField(max_length=100,default="Other")
#     username=models.CharField(max_length=100)
    

    
