from django.contrib import admin

from products.models import Product


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'model', 'launch_date', 'manufacturer')