from django.contrib import admin
from django.utils.html import format_html
from django import forms

from retail.models import Member


class MemberForm(forms.ModelForm):
    """ Форма компании в админ панели с валидацией """
    class Meta:
        model = Member
        fields = '__all__' #['member_type', 'is_factory', 'supplier', 'supplier_debt']
        def clean(self):
            mem_type = self.cleaned_data.get('member_type')
            is_fac = self.cleaned_data.get('is_factory')
            sup = self.cleaned_data.get('supplier')
            sup_debt = self.cleaned_data.get('supplier_debt')
            if is_fac and mem_type != 0:
                raise forms.ValidationError(f'Только завод может отмечать поле {self.is_factory}')
            elif not is_fac and mem_type == 0:
                raise forms.ValidationError(f'Завод должен отмечать поле {self.is_factory}')
            elif is_fac and mem_type == 0 and sup:
                raise forms.ValidationError(f'У завода не может быть поставщика')
            elif is_fac and mem_type == 0 and sup_debt:
                raise forms.ValidationError(f'У завода не может быть задолженности перед поставщиком')
            return self.cleaned_data

@admin.register(Member)
class MemberModelAdmin(admin.ModelAdmin):
    """ Представление компании в админ панели с возможностью гашения долгов """
    form = MemberForm
    list_display = ('id', 'name', 'city', 'member_type', 'supplier_url', 'supplier_debt')
    list_filter = ('city',)
    actions = ['reset_debt']


    def reset_debt(self, request, queryset):
        """ Админ-действие гасящее долг компании """
        queryset.update(supplier_debt=0)

    def supplier_url(self, obj):
        """ Реализация гиперссылки на профиль поставщика компании """
        supplier = obj.supplier
        try:
            url = f'{supplier.id}/change/'
            return format_html("<a href='{url}'>{name}</a>", url=url, name=obj.supplier)
        except AttributeError:
            pass