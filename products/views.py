from django.views.generic import ListView
from products.models import Product


class ProductsList(ListView):
    template_name = "home.html"
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        products = super().get_queryset().order_by('name')
        return products

