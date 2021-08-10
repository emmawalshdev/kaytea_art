from django.shortcuts import render, redirect

# Create your views here.
def view_bag(request):
    '''A view to render the bag content page'''

    return render(request, 'bag/bag.html')

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
    print(request.session['bag'])
    return redirect(redirect_URL)
