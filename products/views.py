from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
    '''A view to show all products, inc search and sorting queries'''
    # return all products
    products = Product.objects.all()

    # Make products available in template
    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
