
from rest_framework.serializers import ModelSerializer

from products.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductMiniSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name']