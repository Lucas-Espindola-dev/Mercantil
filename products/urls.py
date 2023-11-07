from django.urls import path
from products.views import ProductsList

urlpatterns = [
    path('', ProductsList.as_view(), name='products_view'),
    ]
