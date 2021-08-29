from django.shortcuts import render
from .models import Blog

from django.core.paginator import Paginator


# Create your views here.
def all_blogs(request):
    '''A view to return all blogs'''
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 3)
    # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'blogs': blogs,
        'page_obj': page_obj,
    }

    return render(request, 'blog/blog.html', context)
