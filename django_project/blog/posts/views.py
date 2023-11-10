from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    context= {
        "title": "home",
        "data": [1,2,3,4,5,6],
    }
    return render(request, 'home/landing_page.html', context)


def about(request):
    context= {
        "title": "about",
        "data": [1,2,3,4,5,6],
    }
    return render(request, 'about/about_page.html', context) 
