from django.core.exceptions import ValidationError
from django.db import models

NULLABLE = {'null':True, 'blank':True}


class Member(models.Model):
    """ Модель компании с валидацией данных для админ панели"""
    COMPANY_TYPES = (
        (0, "завод"),
        (1, "розничная сеть"),
        (2, "индивидуальный предприниматель")
    )

    name = models.CharField(max_length=100, verbose_name='название')
    email = models.EmailField(verbose_name="почта", unique=True)
    country = models.CharField(max_length= 50, verbose_name="страна")
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)
    street = models.CharField(max_length=50, verbose_name='улица', **NULLABLE)
    building = models.CharField(max_length=20, verbose_name='номер дома', **NULLABLE)
    registration_date = models.DateField(auto_now_add=True, verbose_name='дата регистрации компании')
    supplier_debt = models.DecimalField(max_digits=100, decimal_places=2, verbose_name='долг перед поставщиком', **NULLABLE)

    member_type = models.SmallIntegerField(choices=COMPANY_TYPES, verbose_name='тип компании')
    is_factory = models.BooleanField(default=False, verbose_name='является заводом')
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='поставщик', **NULLABLE)

    def clean(self):
        """ Валидация данных компании для админ панели """
        if self.is_factory and self.member_type != 0:
            raise ValidationError(f'Только завод может отмечать поле "is_factory"')
        elif not self.is_factory and self.member_type == 0:
            raise ValidationError(f'Завод должен отмечать поле "is_factory"')
        elif self.is_factory and self.member_type == 0 and self.supplier:
            raise ValidationError(f'У завода не может быть поставщика')
        elif self.is_factory and self.member_type == 0 and self.supplier_debt:
            raise ValidationError(f'У завода не может быть задолженности перед поставщиком')
        if self.supplier == self.pk and self.supplier:
            raise ValidationError(f'Компания не может быть своим же поставщиком')

    def __str__(self):
        return f'{self.name}, id: {self.pk}'

    class Meta:
        verbose_name = 'член сети'
        verbose_name_plural = 'члены сети'


