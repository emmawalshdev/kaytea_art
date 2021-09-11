from django.shortcuts import render, redirect
from .forms import CommissionsForm
from django.contrib import messages


# Create your views here.
def commissions(request):
    '''A view to return the contact form page'''
    if request.method == 'POST':
        form = CommissionsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message was\
                sucessfully sent!')
            return redirect('commissions')
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    form = CommissionsForm()
    context = {
        'form': form
    }
    return render(request, 'commissions/commissions.html', context)
