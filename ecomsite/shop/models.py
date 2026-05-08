from django.db import models

# Create your models here.
class products(models.Model):
    title = models.CharField(max_length=200)
    description  = models.TextField()
    price = models.FloatField()
    discounted_price = models.FloatField()
    category = models.CharField(max_length=200)
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.title
    