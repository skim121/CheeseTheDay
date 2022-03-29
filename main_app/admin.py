from django.contrib import admin
from .models import Cheese, Wine # import the Cat model from models.py
# Register your models here.

admin.site.register(Cheese) 
admin.site.register(Wine) 
# this line will add the model to the admin panel