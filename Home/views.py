from django.shortcuts import render
from django.http import HttpResponse, request
from .models import *

# Create your views here.


def home(reqeust):
    return render(reqeust, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')
    