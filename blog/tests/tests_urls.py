from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import (
    all_blogs, blog_detail, add_blog, edit_blog, edit_reply)


class TestUrls(SimpleTestCase):

    def test_blog_url_is_resolves(self):
        url = reverse('blog')
        print(resolve(url))
        self.assertEquals(resolve(url).func, all_blogs)

    def test_blog_detail_url_resolves(self):
        url = reverse('blog_detail', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, blog_detail)

    def test_add_blog_url_resolves(self):
        url = reverse('add_blog')
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_blog)

    def test_edit_blog_url_resolves(self):
        url = reverse('edit_blog', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, edit_blog)

    def test_edit_reply_url_resolves(self):
        url = reverse('edit_reply', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, edit_reply)
