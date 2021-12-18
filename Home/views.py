from django.shortcuts import render
from django.http import HttpResponse, request
from Home.models import Contact
from Home.models import Course
from Home.models import Year
from Home.models import SEyear
from Home.models import BMyear

# Create your views here.


def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def index(request):
    return render(request, 'home/index.html')

def contact(request):
    if request.method == "POST":
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        cnumber = request.POST.get('cnumber')
        contact = Contact(email=email, fname=fname, cnumber=cnumber)
        contact.save()
        return render(request, 'Home/contact.html')
    return render(request, 'Home/contact.html')
    
def main(request):
    context = {
        'courses':Course.objects.all()
    }
    return render(request, 'home/main.html', context)

def assignment(request):
    return render(request, 'home/assignment.html')

def cs(request):
    context = {
        'years':Year.objects.all()
    }
    return render(request, 'home/cs.html', context)

def se(request):
    context = {
        'seyears':SEyear.objects.all()
    }
    return render(request, 'home/se.html', context)

def bm(request):
    context = {
        'bmyears':BMyear.objects.all()
    }
    return render(request, 'home/bm.html', context)