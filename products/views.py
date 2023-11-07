from django.shortcuts import render
from django.views.generic import TemplateView


class ProductsList(TemplateView):
    template_name = "home.html"
