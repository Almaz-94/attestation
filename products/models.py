from django.db import models

from retail.models import Member


class Product(models.Model):
    """ Модель продукта, с названием, моделью, датой выходы на рынок и внешним ключом к производителю """
    name = models.CharField(max_length=100, verbose_name="название")
    model = models.CharField(max_length=50, verbose_name='модель')
    launch_date = models.DateField(verbose_name='дата выхода на рынок')
    manufacturer = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='производитель')

    def __str__(self):
        return f'Product {self.name}, manufacturer {self.manufacturer}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'