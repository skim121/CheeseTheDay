from django.shortcuts import render
from django.views import View 
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse 
from .models import Cheese, Wine 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator 

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

@method_decorator(login_required, name='dispatch')
class CheeseCreate(CreateView): 
    model = Cheese
    fields = ['name', 'type', 'milk', 'origin', 'img', 'wine']
    template_name="cheese_create.html"
    def form_valid(self, form): 
        self.object = form.save(commit=False)
        self.object.user= self.request.user
        self.object.save()
        return HttpResponseRedirect('/cheeses/')

class CheeseDetail(DetailView):
    model = Cheese
    template_name = "cheese_detail.html"

@method_decorator(login_required, name='dispatch')
class CheeseUpdate(UpdateView):
    model = Cheese
    fields = ['name', 'type', 'milk', 'origin', 'img', 'wine']
    template_name = "cheese_update.html"
    def get_success_url(self):
        return reverse('cheese_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class CheeseDelete(DeleteView): 
    model = Cheese
    template_name = "cheese_delete_confirm.html"
    success_url = "/cheeses/"

@login_required
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

@method_decorator(login_required, name='dispatch')
class WineCreate(CreateView):
    model = Wine
    fields = ['name', 'type', 'sweetness']
    template_name = "wine_form.html"
    success_url = '/wines'

@method_decorator(login_required, name='dispatch')
class WineUpdate(UpdateView):
    model = Wine
    fields = ['name', 'type', 'sweetness']
    template_name = "wine_update.html"
    success_url = '/wines'

@method_decorator(login_required, name='dispatch')
class WineDelete(DeleteView):
    model = Wine
    template_name = "wine_confirm_delete.html"
    success_url = '/wines'

# def login_view(request): 
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             u = form.cleaned_data['username']
#             p = form.cleaned_data['password']
#             user = authenticate (username = u, password = p )
#             if user is not None: 
#                 if user.is_active: 
#                     login(request,user)
#                     return HttpResponseRedirect('/user/'+u)
#                 else: 
#                     print('The account has been disabled')
#             else:
#                 print('The username and/or password is incorrect')
#     else: 
#         form = AuthenticationForm()
#         return render(request, 'login.html', {'form': form}) #putting the form inside an object or dictionary

def login_view(request):
    # if POST, then authenticate the user (submitting the username and password)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    print('The account has been disabled')
                    return HttpResponseRedirect('/login')
        else: 
            return render(request, 'login.html', {'form': form})

    else:
        # user is going to the login page
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/cheeses')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
            user = form.save()
            login(request, user)
            print ('Hi', user.username)
            return HttpResponseRedirect('/user/' + str(user.username))
        else:
            return render(request, 'signup.html', {'form': form})

    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
