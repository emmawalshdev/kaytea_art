from django.test import SimpleTestCase
from django.urls import reverse, resolve
from about.views import about


class TestUrls(SimpleTestCase):

    def test_about_url_is_resolves(self):
        url = reverse('about')
        print(resolve(url))
        self.assertEquals(resolve(url).func, about)
