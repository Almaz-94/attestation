from rest_framework.generics import CreateAPIView

from users.serializers import UserSerializer


class UserRegister(CreateAPIView):
    serializer_class = UserSerializer
    