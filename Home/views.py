from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.


def home(reqeust):
    #return HttpResponse('<h1>Kathan sheth</h1>')
    return render(reqeust, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')
    #return HttpResponse('<h1>About</h1>')
    