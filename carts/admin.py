from django.contrib import admin
from .models import Cart, cartItem

# Register the Cart model with the admin site.
# This allows the Cart model to be managed through the Django admin interface.
admin.site.register(Cart)

# Register the cartItem model with the admin site.
# This allows the cartItem model to be managed through the Django admin interface.
admin.site.register(cartItem)
