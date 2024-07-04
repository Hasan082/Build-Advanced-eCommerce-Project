from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from carts.models import Cart, cartItem
from store.models import Product


def _cart_id(request):
    """
    Retrieves the current session's cart ID, creating a new session if it doesn't exist.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        str: The session key, which acts as the cart ID.
    """
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    """
    Adds a product to the cart. If the product is already in the cart, increases the quantity by one.

    Args:
        request (HttpRequest): The HTTP request object.
        product_id (int): The ID of the product to add to the cart.

    Returns:
        HttpResponse: Redirects to the cart home page.
    """
    if request.method == 'POST':
        color = request.POST.get('color')
        size = request.POST.get('size')

    product = get_object_or_404(Product, id=product_id)  # Retrieve the product

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
    cart.save()

    try:
        cart_item = cartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except cartItem.DoesNotExist:
        cart_item = cartItem.objects.create(product=product, quantity=1, cart=cart)
    cart_item.save()

    return redirect('cart_home')


def remove_cart(request, product_id):
    """
    Removes a product from the cart. If the quantity is greater than one, decreases the quantity by one.
    Otherwise, removes the product from the cart.

    Args:
        request (HttpRequest): The HTTP request object.
        product_id (int): The ID of the product to remove from the cart.

    Returns:
        HttpResponse: Redirects to the cart home page.
    """
    product = get_object_or_404(Product, id=product_id)
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_item = get_object_or_404(cartItem, product=product, cart=cart)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart_home')


def delete_cart(request, product_id):
    """
    Deletes a product from the cart, regardless of the quantity.

    Args:
        request (HttpRequest): The HTTP request object.
        product_id (int): The ID of the product to delete from the cart.

    Returns:
        HttpResponse: Redirects to the cart home page.
    """
    product = get_object_or_404(Product, id=product_id)
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_item = get_object_or_404(cartItem, product=product, cart=cart)
    cart_item.delete()

    return redirect('cart_home')


def cart_home(request, total=0, quantity=0, cart_items=None):
    """
    Displays the cart page with a summary of the cart's contents, including the total cost, quantity,
    tax, and grand total.

    Args:
        request (HttpRequest): The HTTP request object.
        total (Decimal, optional): The total cost of the items in the cart. Defaults to 0.
        quantity (int, optional): The total quantity of items in the cart. Defaults to 0.
        cart_items (QuerySet, optional): The items in the cart. Defaults to None.

    Returns:
        HttpResponse: Renders the cart page with the cart context.
    """
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = cartItem.objects.filter(cart=cart, is_active=True)

        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity

        tax = (2 * total) / 100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total
    }

    return render(request, 'cart.html', context)
