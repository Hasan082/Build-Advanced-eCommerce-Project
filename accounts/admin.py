from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


# Define the custom admin class for the Account model by extending UserAdmin
class AccountAdmin(UserAdmin):
    # `list_display` specifies the fields to display in the admin list view.
    # This makes it easier to see key information about each account at a glance.
    list_display = (
        'id', 'email', 'first_name', 'last_name', 'username', 'phone', 'last_login', 'date_joined', 'is_active')

    # `list_display_links` determines which fields in the `list_display` are clickable,
    # allowing you to navigate to the detail page of an account by clicking on these fields.
    list_display_links = ('email', 'first_name')

    # `list_filter` adds filters on the right sidebar of the list view,
    # which allows you to filter the list of accounts by specific criteria.
    list_filter = ('is_active', 'date_joined', 'last_login')

    # `readonly_fields` makes the specified fields read-only in the admin form.
    # These fields will still be displayed, but cannot be edited directly.
    readonly_fields = ('date_joined', 'last_login')

    # `search_fields` allows you to add a search box in the admin list view.
    # You can search accounts based on the fields specified here.
    search_fields = ('email', 'first_name', 'last_name')

    # `ordering` determines the default order of accounts in the list view.
    # Here, it orders the accounts by the `date_joined` field in descending order.
    ordering = ('-date_joined',)

    # `filter_horizontal` is used for displaying many-to-many fields with a horizontal filter interface.
    # Since we have no such fields here, it is left as an empty tuple.
    filter_horizontal = ()

    # `fieldsets` customizes the layout of fields on the account edit form page in the admin.
    # An empty tuple means no specific layout is defined, and default layout will be used.
    fieldsets = ()


# Register the `Account` model with the customized `AccountAdmin` class.
# This connects the `Account` model with its admin interface configuration.
admin.site.register(Account, AccountAdmin)
