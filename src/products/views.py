from django.shortcuts import render

# importing model 
from .models import Product
from .forms import ProductForm

# Create your views here.
# obj = Product.objects.get(id = 1)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
        
    context_obj = {
        "form" : form
    }
    return render(request, "products/product_create.html", context_obj)

def product_detail_view(request):
    obj = Product.objects.get( id = 1 )

    # context_obj = {
    #     "title" : obj.title,
    #     "description" : obj.description
    # }

    context_obj = {
        "object" : obj
    }
    return render(request, "products/product_detail.html", context_obj)
