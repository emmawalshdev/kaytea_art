from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from django.contrib.auth.models import User

from .models import Product, Category, ProductReview
from .forms import ProductForm, ProductReviewForm


# Create your views here.
def all_products(request):
    '''A view to show all products, inc search and sorting queries'''
    # return all products
    products = Product.objects.all()
    all_categories = Category.objects.all()

    # ensure that an error is not thrown when no q is specified
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

                if sortkey == 'category':
                    sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    # Make products available in template
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'all_categories': all_categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    '''A view to show individual product details'''
    # return all products
    product = get_object_or_404(Product, pk=product_id)
    reviews = ProductReview.objects.filter(product=product_id).order_by('-id')

    int_prod = int(product.stock)
    stock_num = [x for x in range(int_prod)]

    # calculate avg rating
    ratings = 0
    if len(reviews) != 0:
        for review in reviews:
            ratings += float(review.review_rating)
        avg_rating = ratings / len(reviews)
    else:
        avg_rating = None

    if request.method == "POST":
        form = ProductReviewForm(request.POST)

        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            form.instance.author = user
            review = form.save(commit=False)
            review.product = product
            review.save()
            messages.success(request, 'Your reply was successfully saved!')
            return redirect(reverse('product_detail', args=[product.id]))
    else:
        form = ProductReviewForm()

    # Make products available in template
    context = {
        'product': product,
        'stock_num': stock_num,
        'form': form,
        'reviews': reviews,
        'avg_rating': avg_rating,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def edit_review(request, review_id):
    """ Edit a review on a product page """
    review = get_object_or_404(ProductReview, pk=review_id)
    product_id = review.product.id
    product = get_object_or_404(Product, pk=product_id)

    if review.author != request.user and not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update review. Please ensure the form is valid.')
    else:
        form = ProductReviewForm(instance=review)
        messages.info(request, 'You are editing your review')

    template = 'products/edit_review.html'
    context = {
        'form': form,
        'review': review,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """ Delete a review from a product page """
    review = get_object_or_404(ProductReview, pk=review_id)
    product_id = review.product.id
    product = get_object_or_404(Product, pk=product_id)

    if review.author != request.user and not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('product_detail', args=[product.id]))

    review.delete()
    messages.success(request, 'Review successfully deleted.')

    return redirect(reverse('product_detail', args=[product.id]))
