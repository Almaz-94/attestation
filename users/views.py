from rest_framework.generics import CreateAPIView

from users.serializers import UserSerializer


class UserRegister(CreateAPIView):
    """ Представление для создания пользователя """
    serializer_class = UserSerializer
    