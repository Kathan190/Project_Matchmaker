from django.shortcuts import render
from django.http import HttpResponse, request
from Home.models import Contact

# Create your views here.


def home(request):
    if request.method == "POST":
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        cnumber = request.POST.get('cnumber')
        contact = Contact(email=email, fname=fname, cnumber=cnumber)
        contact.save()
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')
    