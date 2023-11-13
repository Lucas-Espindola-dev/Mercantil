from django.test import TestCase
from django.urls import reverse


class ProductsURLsTest(TestCase):
    def test_products_home_is_correct(self):
        url = reverse('products:products_view')
        self.assertEqual(url, '/')
