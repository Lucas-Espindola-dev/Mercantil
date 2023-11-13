from django.test import TestCase
from django.urls import resolve, reverse
from products import views


class ProductsViewTest(TestCase):
    def test_products_home_views_Class_is_correct(self):
        view = resolve(reverse('products:products_view'))
        self.assertIs(view.func, views.ListView.as_view())

