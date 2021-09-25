from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


# Create your views here.
def contact(request):
    ''' A view to return the contact form page '''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message was\
                sucessfully sent!')
            return redirect('contact')
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact/contact.html', context)
