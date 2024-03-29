
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from products.serializers import ProductMiniSerializer
from retail.models import Member
from retail.validators import FactoryValidator


class MemberSerializer(ModelSerializer):
    """ Сериализатор для компании с выводом списка производимой продукции """
    products = ProductMiniSerializer(source='product_set', many=True, read_only=True)
    class Meta:

        model = Member
        fields = '__all__'
        validators = [FactoryValidator('member_type', 'is_factory', 'supplier', 'supplier_debt'), ]


class MemberUpdateSerializer(ModelSerializer):
    """ Сериализатор для редактирования компании с валидацией полей """
    class Meta:
        model = Member
        fields = '__all__'
        read_only_fields = ['supplier_debt']
        validators = [FactoryValidator('member_type', 'is_factory', 'supplier', 'supplier_debt') ]

    def validate_supplier(self, value):
        if self.instance.pk == value.pk:
            raise ValidationError('Компания не может быть своим же поставщиком')
        return value
