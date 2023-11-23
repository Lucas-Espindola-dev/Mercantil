from django.views.generic import ListView, CreateView, DetailView, UpdateView
from products.models import Product
from products.forms import ProductModelForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class ProductsList(ListView):
    template_name = "home.html"
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        products = super().get_queryset().order_by('name')
        return products


class ProductDetail(DetailView):
    model = Product
    template_name = 'product_detail.html'


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class NewProduct(CreateView):
    model = Product
    form_class = ProductModelForm
    template_name = 'new_product.html'
    success_url = '/'


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductModelForm
