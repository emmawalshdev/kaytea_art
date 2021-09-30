from django.test import TestCase, Client
from django.urls import reverse
from contact.models import Contact


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.contact_url = reverse('contact')

    def test_contacts(self):

        response = self.client.get(self.contact_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
