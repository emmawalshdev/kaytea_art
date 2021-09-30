from django.test import SimpleTestCase
from django.urls import reverse, resolve
from checkout.views import (
    checkout, checkout_success, cache_checkout_data)


class TestUrls(SimpleTestCase):

    def test_checkout_url_is_resolves(self):
        url = reverse('checkout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, checkout)

    def test_checkout_success_url_resolves(self):
        url = reverse('checkout_success', args=[123])
        print(resolve(url))
        self.assertEquals(resolve(url).func, checkout_success)

    def test_cache_checkout_data_url_resolves(self):
        url = reverse('cache_checkout_data')
        print(resolve(url))
        self.assertEquals(resolve(url).func, cache_checkout_data)
