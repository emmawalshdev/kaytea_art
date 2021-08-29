from django.shortcuts import render, get_object_or_404
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


# Create your views here.
def blog_detail(request, blog_id):
    '''A view to show individual blog details'''
    blog = get_object_or_404(Blog, pk=blog_id)
    # Show 25 contacts per page.

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog_detail.html', context)
