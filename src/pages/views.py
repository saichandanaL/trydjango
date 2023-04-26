from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request ,*args, **kargs):
    return HttpResponse("<H1>Hello world</H1>")

def contact_view(request, *args, **kargs):
    return HttpResponse("<H1>Contact Details</H1>")