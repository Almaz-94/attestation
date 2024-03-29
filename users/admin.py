from django.contrib import admin

from users.models import User


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    """ Представление пользователя в админ панели """
    list_display = ('pk', 'username',)