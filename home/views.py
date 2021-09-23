from django.shortcuts import render

# Create your views here.
def index(request):
    '''A view to return the uindex page'''

    return render(request, 'home/index.html')

def error_403(request, exception):
    """View to render a cutom 403 page"""
    return render(request, '../templates/403.html')


def error_404(request, exception):
    """View to render a cutom 404 page"""
    return render(request, '../templates/404.html')


def error_500(request):
    """View to render a cutom 500 page"""
    return render(request, '../templates/500.html')