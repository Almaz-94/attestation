from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from users.apps import UsersConfig
from users.views import UserRegister

app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserRegister.as_view(), name='user_register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]