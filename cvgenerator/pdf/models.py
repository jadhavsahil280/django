from django.db import models

# Create your models here.

class profile(models.Model):
    name = models.CharField(max_length=100)
    jobtitle = models.CharField(max_length=100)
    email = models.CharField(max_length=100)    
    phone = models.IntegerField()
    dob = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    address = models.TextField(max_length=1000)
    degree = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    passingyear = models.IntegerField()
    percentage = models.FloatField()
    previouscompanyname = models.CharField(max_length=500)
    experience = models.FloatField()
    jobdesc = models.TextField(max_length=1000)
    skills = models.TextField(max_length=1000)    
    languagesknown = models.TextField(max_length=1000)
    photo = models.ImageField(upload_to='profilephoto', default='profilephoto/user.jpg')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name