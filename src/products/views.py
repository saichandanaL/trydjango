from django.shortcuts import render

# importing model 
from .models import Product

# Create your views here.
# obj = Product.objects.get(id = 1)
obj = Product.objects.get( id = 1 )

def product_detail_view(request):

    # context_obj = {
    #     "title" : obj.title,
    #     "description" : obj.description
    # }

    context_obj = {
        "object" : obj
    }
    return render(request, "products/product_detail.html", context_obj)
