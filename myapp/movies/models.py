from django.db import models

# Create your models here.

class MovieData(models.Model):
    name = models.CharField(max_length=100)
    duration = models.FloatField()
    rating = models.FloatField()
    type = models.CharField(max_length=200, default='action')
    img = models.ImageField(upload_to='movies/', default='movies/placeholder/placeholder.img')


    def __str__(self):
        return self.name