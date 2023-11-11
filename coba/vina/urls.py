from django.urls import path
from . import views

urlpatterns = [
    path('vina', views.vina, name='vina'),
    path('menu', views.menu, name='menu'),
    path('base', views.base, name='base'),
    path('home', views.home, name='home'),
]