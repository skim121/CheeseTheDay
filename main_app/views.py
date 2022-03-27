from django.shortcuts import render
from django.views import View 
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse 
from .models import Cheese 


# Create your views here.

class Home(TemplateView): 
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

# class Cheese: 
#     def __init__ (self, name, type, milk):
#         self.name = name 
#         self.type = type
#         self.milk = milk 

# cheeses = [
#     Cheese("Burrata", "fresh", "cow"), 
#     Cheese("Mozzarella", "fresh", "cow"), 
#     Cheese("Feta", "fresh", "goat"),
#     Cheese("Brie", "soft", "cow"),
#     Cheese("Camembert", "soft", "cow"),
#     Cheese("Havarti", "semi-soft", "cow"),
#     Cheese("Muenster", "semi-soft", "cow"),
#     Cheese("Cheddar", "semi-firm", "cow"),
#     Cheese("Gouda", "semi-firm", "cow"),
#     Cheese("Gruyere", "semi-firm", "cow"),
#     Cheese("Asiago", "hard", "cow"), 
#     Cheese("Manchego", "hard", "cow"),
#     Cheese("Parmesan", "hard", "cow"),
#     Cheese("Pecorino", "hard", "sheep"),
#     Cheese("Gorgonzola", "blue", "cow"),
#     Cheese("Roquefort", "blue", "sheep"),
# ]

class CheeseList(TemplateView):
    template_name = "cheese.html"
    def get_context_data(self,**kwargs): 
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None: 
            context["cheeses"] = Cheese.objects.filter(name__icontains=name)
            context["header"] = f"Search result for {name}:"
        else:
            context['cheeses'] = Cheese.objects.all()
            context['header'] = "List of Cheeses"
        return context

class CheeseCreate(CreateView): 
    model = Cheese
    fields = ['name', 'type', 'milk', 'origin', 'img']
    template_name="cheese_create.html"
    def get_success_url(self):
        return reverse('cheese_detail', kwargs={'pk': self.object.pk})

class CheeseDetail(DetailView):
    model = Cheese
    template_name = "cheese_detail.html"

class CheeseUpdate(UpdateView):
    model = Cheese
    fields = '__all__'
    template_name = "cheese_update.html"
    def get_success_url(self):
        return reverse('cheese_detail', kwargs={'pk': self.object.pk})