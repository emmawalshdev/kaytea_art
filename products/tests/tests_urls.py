from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import (
    all_products, product_detail, add_product,
    edit_product, edit_review)


class TestUrls(SimpleTestCase):

    def test_products_url_is_resolves(self):
        url = reverse('products')
        print(resolve(url))
        self.assertEquals(resolve(url).func, all_products)

    def test_products_detail_url_resolves(self):
        url = reverse('product_detail', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, product_detail)

    def test_add_product_url_resolves(self):
        url = reverse('add_product')
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_product)

    def test_edit_product_url_resolves(self):
        url = reverse('edit_product', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, edit_product)

    def test_edit_review_url_resolves(self):
        url = reverse('edit_review', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, edit_review)
