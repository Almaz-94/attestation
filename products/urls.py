
from rest_framework import routers

from products.apps import ProductsConfig
from products.views import ProductViewSet

app_name = ProductsConfig.name

router = routers.DefaultRouter()
router.register('', ProductViewSet, basename='products')

urlpatterns = router.urls
