from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):
    list_display = ('id' ,'email',  'first_name', 'last_name', 'username', 'phone', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name')
    list_filter = ('is_active', 'date_joined', 'last_login')
    filter_horizontal = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
