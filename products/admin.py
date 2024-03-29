from django.contrib import admin
from django.utils.html import format_html

from products.models import Product


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    """ Представление продукта в админ панели """
    list_display = ('pk', 'name', 'model', 'launch_date', 'manufacturer_url')
    def manufacturer_url(self, obj):
        """ Реализация гиперссылки на профиль производителя продукта """
        manufacturer = obj.manufacturer
        try:
            url = f'{manufacturer.id}/change/'
            return format_html("<a href='{url}'>{name}</a>", url=url, name=obj.manufacturer)
        except AttributeError:
            pass