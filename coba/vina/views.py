from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def vina(request):
    template = loader.get_template('menu.html')
    return HttpResponse(template.render())

def menu(request):
    template = loader.get_template('menu.html')
    return HttpResponse(template.render())

def base(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())