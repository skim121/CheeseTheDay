from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('cheeses/', views.CheeseList.as_view(), name="cheeses"),
    path('cheese/new/', views.CheeseCreate.as_view(), name="cheese_create"),
    path('cheese/<int:pk>', views.CheeseDetail.as_view(), name="cheese_detail"),
    path('cheese/<int:pk>/update/', views.CheeseUpdate.as_view(), name="cheese_update"),
    path('cheese/<int:pk>/delete/', views.CheeseDelete.as_view(), name="cheese_delete"),
    
    path('user/<username>/', views.profile, name="profile"),

    path('wines/', views.WineList.as_view(), name='wines'),
    path('wine/<int:pk>', views.WineDetail.as_view(), name='wine_detail'),
    path('wine/create/', views.WineCreate.as_view(), name='wine_create'),
    path('wine/<int:pk>/update/', views.WineUpdate.as_view(), name='wine_update'),
    path('wine/<int:pk>/delete/', views.WineDelete.as_view(), name='wine_delete'),
]