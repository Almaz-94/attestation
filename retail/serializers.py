from rest_framework.serializers import ModelSerializer

from products.serializers import ProductMiniSerializer
from retail.models import Member
from retail.validators import FactoryValidator, SupplierValidator


class MemberSerializer(ModelSerializer):
    products = ProductMiniSerializer(many=True, read_only=True)
    class Meta:

        model = Member
        fields = '__all__'
        validators = [FactoryValidator('member_type', 'is_factory', 'supplier', 'supplier_debt'), SupplierValidator(), ]


class MemberUpdateSerializer(ModelSerializer):
    class Meta:

        model = Member
        fields = '__all__'
        read_only_fields = ['supplier_debt']
        validators = [FactoryValidator('member_type', 'is_factory', 'supplier', 'supplier_debt'), SupplierValidator(), ]

