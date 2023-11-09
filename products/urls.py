from django.urls import path
from products.views import ProductsList, NewProduct

urlpatterns = [
    path('', ProductsList.as_view(), name='products_view'),
    path('new_product/', NewProduct.as_view(), name='new_product'),
    ]
