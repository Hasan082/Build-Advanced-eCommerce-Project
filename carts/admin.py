from django.contrib import admin
from .models import Cart, cartItem


class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_active')


# Register the Cart model with the admin site.
# This allows the Cart model to be managed through the Django admin interface.
admin.site.register(Cart, CartAdmin)

# Register the cartItem model with the admin site.
# This allows the cartItem model to be managed through the Django admin interface.
admin.site.register(cartItem, CartItemAdmin)
