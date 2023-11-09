from django.views.generic import ListView, CreateView
from products.models import Product
from products.forms import ProductForm


class ProductsList(ListView):
    template_name = "home.html"
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        products = super().get_queryset().order_by('name')
        return products


class NewProduct(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'new_product.html'
    success_url = '/'

