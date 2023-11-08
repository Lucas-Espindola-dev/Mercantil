from django.contrib import admin
from products.models import Product, Brand


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'brand',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
