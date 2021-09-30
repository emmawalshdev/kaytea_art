from django.test import SimpleTestCase
from django.urls import reverse, resolve
from contact.views import contact


class TestUrls(SimpleTestCase):

    def test_contact_url_is_resolves(self):
        url = reverse('contact')
        print(resolve(url))
        self.assertEquals(resolve(url).func, contact)
