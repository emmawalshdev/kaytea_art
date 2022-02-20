from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def privacy_view(request, *args, **kwargs):
    return render(request, "privacy.html")

def terms_view(request, *args, **kwargs):
    return render(request, "terms.html")
