from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('cheeses/', views.CheeseList.as_view(), name="cheeses"),
    path('cheese/new/', views.CheeseCreate.as_view(), name="cheese_create")

]