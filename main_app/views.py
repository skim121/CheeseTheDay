from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View 
from django.http import HttpResponse 

# Create your views here.

class Home(TemplateView): 
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Cheese: 
    def __init__ (self, name, type, milk):
        self.name = name 
        self.type = type
        self.milk = milk 

cheeses = [
    Cheese("Burrata", "fresh", "cow"), 
    Cheese("Mozzarella", "fresh", "cow"), 
    Cheese("Feta", "fresh", "goat"),
    Cheese("Brie", "soft", "cow"),
    Cheese("Camembert", "soft", "cow"),
    Cheese("Havarti", "semi-soft", "cow"),
    Cheese("Muenster", "semi-soft", "cow"),
    Cheese("Cheddar", "semi-firm", "cow"),
    Cheese("Gouda", "semi-firm", "cow"),
    Cheese("Gruyere", "semi-firm", "cow"),
    Cheese("Asiago", "hard", "cow"), 
    Cheese("Manchego", "hard", "cow"),
    Cheese("Parmesan", "hard", "cow"),
    Cheese("Pecorino", "hard", "sheep"),
    Cheese("Gorgonzola", "blue", "cow"),
    Cheese("Roquefort", "blue", "sheep"),
]

class Cheese_List(TemplateView):
    template_name = "cheese.html"
    def get_context_data(self,**kwargs): 
        context = super().get_context_data(**kwargs)
        context['cheeses'] = cheeses
        return context
