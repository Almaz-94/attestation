
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from products.models import Product
from products.serializers import ProductSerializer
from users.permissions import IsActive


class ProductViewSet(ModelViewSet):
    """ Реализация CRUD для модели продукта """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, IsActive, )