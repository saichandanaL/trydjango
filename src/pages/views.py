from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request ,*args, **kargs):
    return render(request, "home.html", {})

def contact_view(request, *args, **kargs):
    print(args , kargs)
    print(request.user)
    return HttpResponse("<H1>Contact Details</H1>")