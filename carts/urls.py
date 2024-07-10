from django.urls import path
from . import views

# Define the URL patterns for the cart application.
urlpatterns = [
    path('', views.cart_home, name='cart_home'),
    # The empty string '' matches the root URL of the cart application. This URL pattern maps to the 'cart_home'
    # view, and the name 'cart_home' can be used to reference this URL pattern in templates and views.

    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    # The 'add_cart/<int:product_id>/' pattern matches URLs like 'add_cart/1/' where '1' is a product ID. The
    # '<int:product_id>' part captures the product ID as an integer and passes it to the 'add_cart' view as a
    # parameter. The name 'add_cart' can be used to reference this URL pattern in templates and views.

    path('remove_cart/<int:product_id>/<int:cart_item_id>/', views.remove_cart, name='remove_cart'),
    # The 'remove_cart/<int:product_id>/' pattern matches URLs like 'remove_cart/1/' where '1' is a product ID. The
    # '<int:product_id>' part captures the product ID as an integer and passes it to the 'remove_cart' view as a
    # parameter. The name 'remove_cart' can be used to reference this URL pattern in templates and views.

    path('delete_cart/<int:product_id>/', views.delete_cart, name='delete_cart'),
    # The 'delete_cart/<int:product_id>/' pattern matches URLs like 'delete_cart/1/' where '1' is a product ID. The
    # '<int:product_id>' part captures the product ID as an integer and passes it to the 'delete_cart' view as a
    # parameter. The name 'delete_cart' can be used to reference this URL pattern in templates and views.
]
