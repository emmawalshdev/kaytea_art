from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.commissions_url = reverse('commissions')

    def test_commissions(self):

        response = self.client.get(self.commissions_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'commissions/commissions.html')
