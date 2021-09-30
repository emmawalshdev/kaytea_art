from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.view_bag_url = reverse('view_bag')

    def test_view_bag(self):

        response = self.client.get(self.view_bag_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')
