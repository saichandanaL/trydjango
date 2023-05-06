from django.shortcuts import render

# importing model 
from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.
# obj = Product.objects.get(id = 1)

# for creating forms
def product_create_view(request):
    my_form = RawProductForm(request.POST)
    
    context_obj = {
            "form" : my_form
        }

    return render(request, "products/product_create.html", context_obj)

# for raw html
# def product_create_view(request):
#     print(request)

#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
    
#     context_obj = {}

#     return render(request, "products/product_create.html", context_obj)

# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()

#     context_obj = {
#         "form" : form
#     }
#     return render(request, "products/product_create.html", context_obj)

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
