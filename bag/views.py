from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.
def view_bag(request):
    '''A view to render the bag content page'''

    return render(request, 'bag/bag.html')

def adjust_bag(request, item_id):
    '''Adjust the quantity of the specified product to the requested amount'''

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    # overwrite the session var with updated version
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    '''Remove the specified product from the bag'''
    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)

        # overwrite the session var with updated version
        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)

def add_to_bag(request, item_id):
    '''Add a quantity of the specified product to the bag'''

    # get quantity added
    quantity = int(request.POST.get('quantity'))
    # get redirect from form to redirect when process is complete
    redirect_URL = request.POST.get('redirect_url')
    # check if bag in session, create one if not
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        # update quantity if item already exists 
        bag[item_id] == quantity
    else:
        # add item to bag
        bag[item_id] = quantity

    # overwrite the session var with updated version
    request.session['bag'] = bag
    return redirect(redirect_URL)
