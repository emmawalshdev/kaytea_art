from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


# Create your views here.
def checkout(request):
    # get back from session
    bag = request.session.get('bag', {})
    if not bag:
        # if no bag, send error request (prevent manaual access)
        messages.error(request, "Your bag is empty!")
        return redirect(reverse('products'))

    # create instance of order
    order_form = OrderForm()
    # create the template
    template = 'checkout/checkout.html'
    # add the context contact order form
    context = {
        'order_form': order_form,
    }

    # render it all out
    return render(request, template, context)
