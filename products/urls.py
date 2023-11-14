from django.urls import path
from products.views import ProductsList, NewProduct
from django.conf.urls.static import static
from django.conf import settings

app_name = 'products'

urlpatterns = [
    path('', ProductsList.as_view(), name='products_view'),
    path('new_product/', NewProduct.as_view(), name='new_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
