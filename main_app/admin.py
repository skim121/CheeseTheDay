from django.contrib import admin
from .models import Cheese # import the Cat model from models.py
# Register your models here.

admin.site.register(Cheese) # this line will add the model to the admin panel