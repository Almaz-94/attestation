from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """ Сериализатор для создания пользователя """
    class Meta:
        model = User
        fields = ('pk', 'username', 'password',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """ Создание пользователя вместе с паролем """
        instance = super().create(validated_data)
        instance.set_password(validated_data['password'])
        instance.save()
        return instance
