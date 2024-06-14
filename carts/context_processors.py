from .models import Cart, cartItem
from .views import _cart_id


def cart_counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = cartItem.objects.filter(cart=cart)
            cart_count = sum(item.quantity for item in cart_items)
        except Cart.DoesNotExist:
            cart_count = 0

    return {'cart_count':cart_count}