from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.checkout_url = reverse('checkout')

    def test_checkout(self):

        response = self.client.get(self.checkout_url)

        self.assertEquals(response.status_code, 302)