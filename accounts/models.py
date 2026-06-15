from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    owner=models.OneToOneField(User,on_delete=models.CASCADE)


