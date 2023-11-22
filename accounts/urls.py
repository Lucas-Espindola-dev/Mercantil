from django.urls import path
from accounts.views import register_view


urlpatterns = [
    path('register/', register_view, name='register'),
]
