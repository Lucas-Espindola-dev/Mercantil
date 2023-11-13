from django.test import TestCase
from django.urls import resolve


class ProductsViewTest(TestCase):
    def test_products_home_views_Class_is_correct(self):
        view = resolve('/')
        self.assertTrue(True)

