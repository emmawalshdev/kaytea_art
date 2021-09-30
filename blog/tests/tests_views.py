from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Blog


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.blog_url = reverse('blog')
        self.blog_detail_url = reverse('blog_detail', args=[1])
        self.blog1 = Blog.objects.create(
            id=1
        )
        self.add_blog_url = reverse('add_blog')

    def test_all_blogs(self):

        response = self.client.get(self.blog_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')

    def test_blog_detail_GET(self):

        response = self.client.get(self.blog_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_detail.html')