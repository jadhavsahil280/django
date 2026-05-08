from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile/profilepic.jpg', upload_to='profile')
    location = models.CharField(max_length=300)

    def __str__(self):
        return self.user.username