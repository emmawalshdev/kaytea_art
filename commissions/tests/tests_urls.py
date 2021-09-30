from django.test import SimpleTestCase
from django.urls import reverse, resolve
from commissions.views import commissions


class TestUrls(SimpleTestCase):

    def test_commissions_url_is_resolves(self):
        url = reverse('commissions')
        print(resolve(url))
        self.assertEquals(resolve(url).func, commissions)
