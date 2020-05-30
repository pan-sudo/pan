from django.shortcuts import render
from django.http import HttpResponse
from phoneApp import models

def index(request):
    
    products = models.Product.objects.all()
    return render(request, 'index.html', locals())

# Create your views here.
