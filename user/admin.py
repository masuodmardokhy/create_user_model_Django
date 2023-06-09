from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin  #baseuseradminیک اسم مستعاره برای این یوزر ادمین که با اسم یوزر ادمین پایین اشتباه نکنیم
from django.contrib.auth.models import Group
from .forms import *
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreateForm
    list_display = ('email', 'username', 'phone')
    list_filter = ('email', 'is_active')
    fieldsets = (
        ('user', {'fields': ('email', 'password')}),
        ('personal_info', {'fields': ('is_admin',)}),
        ('permission', {'fields': ('is_active',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('email', 'username', 'password1', 'password2')}),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User,UserAdmin)
admin.site.unregister(Group)