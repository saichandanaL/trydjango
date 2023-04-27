from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request ,*args, **kargs):
    return render(request, "home.html", {})

def contact_view(request, *args, **kargs):
    print(args , kargs)
    print(request.user)

    send_context = {
        "address" : "abc",
        "phone" : "383897349",
        "year" : [2020, 2021, 2022],
        "weather" : ["rain","sunny","wind","cold"]
    }
    return render(request, "about.html", send_context)