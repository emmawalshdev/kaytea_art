from django.shortcuts import render

# Create your views here.
def index(request):
    '''A view to return the index page'''

    return render(request, 'home/index.html')

def error_403(request, exception):
    """View to render a cutom 403 page"""
    return render(request, '../templates/403.html', status=403)


def error_404(request, exception):
    """View to render a cutom 404 page"""
    return render(request, '../templates/404.html', status=404)


def error_500(request):
    """View to render a cutom 500 page"""
    return render(request, '../templates/500.html', status=500)