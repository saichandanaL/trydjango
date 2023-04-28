from django.shortcuts import render

# importing model 
from .models import Product

# Create your views here.
# obj = Product.objects.get(id = 1)
obj = Product.objects.get( id = 6 )

def product_detail_view(request):

    context_obj = {
        "title" : obj.title,
        "description" : obj.description
    }
    return render(request, "product/detail.html", context_obj)
