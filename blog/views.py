from django.shortcuts import render
from .models import Blog


# Create your views here.
def all_blogs(request):
    '''A view to return all blogs'''
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/blog.html', context)
