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
    
class orders(models.Model):
    item = models.CharField(max_length=5000)
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=300)
    phone = models.IntegerField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def order_id(self):
        return f"ORD{self.id:04d}"

    def __str__(self):
        return self.name
    