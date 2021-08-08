from django.shortcuts import render, get_object_or_404
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


def product_detail(request, product_id):
    '''A view to show individual product details'''
    # return all products
    product = get_object_or_404(Product, pk=product_id)

    # Make products available in template
    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
