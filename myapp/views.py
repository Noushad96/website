#manualadded
from django.shortcuts import render, HttpResponse

from django.contrib import admin

# Create your views here.

def index(request):
    context={"variable":"this is sent"}
    return render(request,'index.html',context)
    #return HttpResponse("this is myapp")  # webpage pe de diya


def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about myapp")

def service(request):
    return render(request, 'services.html')
    #return HttpResponse("this is about myapp service")

def contact(request):
    return render(request, 'contact.html')
    #return HttpResponse("this is about myapp contact details")


