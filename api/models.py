from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class PSPUser(AbstractUser):
    following = models.ManyToManyField("self", blank=True, symmetrical=False)
    bio = models.CharField(max_length=150, blank=True)

class Uploads(models.Model):
    user = models.ForeignKey(PSPUser, on_delete=models.CASCADE)
    caption = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="images")
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(PSPUser, blank=True, related_name="user_likes")

class Comment(models.Model):
    upload = models.ForeignKey(Uploads, on_delete=models.CASCADE)
    commenter = models.ForeignKey(PSPUser, on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)


#TODO
# class UploadBorders(models.Model):
    ...