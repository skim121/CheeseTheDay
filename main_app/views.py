from django.shortcuts import render
from django.views import View 
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse 
from .models import Cheese, Wine 
from django.contrib.auth.models import User

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
#     Cheese("Manchego", "hard", "cow" ),
#     Cheese("Parmesan", "hard", "cow"),
#     Cheese("Pecorino", "hard", "sheep"),
#     Cheese("Gorgonzola", "blue", "cow" ),
#     Cheese("Roquefort", "blue", "sheep" ),
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
    def form_valid(self, form): 
        self.object = form.save(commit=False)
        self.object.user= self.request.user
        self.object.save()
        return HttpResponseRedirect('/cheeses/')

class CheeseDetail(DetailView):
    model = Cheese
    template_name = "cheese_detail.html"

class CheeseUpdate(UpdateView):
    model = Cheese
    fields = ['name', 'type', 'milk', 'origin', 'img']
    template_name = "cheese_update.html"
    def get_success_url(self):
        return reverse('cheese_detail', kwargs={'pk': self.object.pk})

class CheeseDelete(DeleteView): 
    model = Cheese
    template_name = "cheese_delete_confirm.html"
    success_url = "/cheeses/"

def profile(request, username): 
    user = User.objects.get(username=username)
    cheeses = Cheese.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'cheeses': cheeses})

class WineList(TemplateView):
    template_name = "wine_list.html"
    def get_context_data(self,**kwargs): 
        context = super().get_context_data(**kwargs)
        context['wines'] = Wine.objects.all()
        return context

class WineDetail(DetailView):
    model = Wine
    template_name = "wine_detail.html"

class WineCreate(CreateView):
    model = Wine
    fields = ['name', 'type', 'sweetness']
    template_name = "wine_form.html"
    success_url = '/wines'

class WineUpdate(UpdateView):
    model = Wine
    fields = ['name', 'type', 'sweetness']
    template_name = "wine_update.html"
    success_url = '/wines'

class WineDelete(DeleteView):
    model = Wine
    template_name = "wine_confirm_delete.html"
    success_url = '/wines'