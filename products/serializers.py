
from rest_framework.serializers import ModelSerializer

from products.models import Product


class ProductSerializer(ModelSerializer):
    """ Сериализатор для создания продукта """
    class Meta:
        model = Product
        fields = '__all__'


class ProductMiniSerializer(ModelSerializer):
    """ Сериализатор для вывода названия продукта в профиле компании """
    class Meta:
        model = Product
        fields = ['name']