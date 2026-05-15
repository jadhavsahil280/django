from django.contrib import admin
from .models import profile

class profileadmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'gender', 'jobtitle', 'degree')

# Register your models here.

admin.site.register(profile, profileadmin)