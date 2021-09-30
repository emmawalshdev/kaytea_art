from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.product_url = reverse('products')
        self.product_detail_url = reverse('product_detail', args=[1])
        self.product1 = Product.objects.create(
            id=1,
            stock=2,
            price=3
        )

    def test_all_products(self):

        response = self.client.get(self.product_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_product_detail_GET(self):

        response = self.client.get(self.product_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')