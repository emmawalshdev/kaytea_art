from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
# import form
from .forms import UserProfileForm


# Get profile for current user & return template
def profile(request):
    """ Display the user's profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    # update profile details
    if request.method == 'POST':
        # create a new instance of form
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    # populate form with users information
    form = UserProfileForm(instance=profile)

    # users order history
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    # return contexts to template
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)