from django.contrib import admin

from users.models import User


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username',)