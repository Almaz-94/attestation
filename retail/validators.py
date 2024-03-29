from rest_framework.exceptions import ValidationError


class FactoryValidator:
    def __init__(self, member_type, is_factory, supplier, supplier_debt):
        self.member_type = member_type
        self.is_factory = is_factory
        self.supplier = supplier
        self.supplier_debt = supplier_debt

    def __call__(self, value):
        mem_type = dict(value).get(self.member_type)
        is_fac = dict(value).get(self.is_factory)
        sup = dict(value).get(self.supplier)
        sup_debt = dict(value).get(self.supplier_debt)
        if is_fac and mem_type != 0:
            raise ValidationError(f'Только завод может отмечать поле "is_factory"')
        elif not is_fac and mem_type == 0:
            raise ValidationError(f'Завод должен отмечать поле "is_factory"')
        elif is_fac and mem_type == 0 and sup:
            raise ValidationError(f'У завода не может быть поставщика')
        elif is_fac and mem_type == 0 and sup_debt:
            raise ValidationError(f'У завода не может быть задолженности перед поставщиком')


class SupplierValidator:
    def __call__(self, value):
        sup = dict(value).get('supplier')
        member_id = dict(value).get('id')
        print(sup, member_id)
        if sup == member_id:
            raise ValidationError(f'Нельзя указывать самого себя как своего поставщика')
