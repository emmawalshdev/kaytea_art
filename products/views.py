from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.
def all_products(request):
    '''A view to show all products, inc search and sorting queries'''
    # return all products
    products = Product.objects.all()
    # ensure that an error is not thrown when no q is specified
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET ['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    # Make products available in template
    context = {
        'products': products,
        'search_term': query,
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
