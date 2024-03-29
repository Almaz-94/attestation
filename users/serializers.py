from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'password',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Создает пользователя и устанавливает ему пароль"""

        instance = super().create(validated_data)
        instance.set_password(validated_data['password'])
        instance.save()
        return instance
