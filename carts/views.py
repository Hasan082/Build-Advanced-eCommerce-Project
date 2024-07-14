from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from carts.models import Cart, cartItem
from store.models import Product, Variation


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
    product = get_object_or_404(Product, id=product_id)
    product_variations = []
    if request.method == 'POST':
        for item in request.POST:
            key = item
            value = request.POST[key]
            try:
                variation = Variation.objects.get(product=product, variation_category__iexact=key,
                                                  variation_value__iexact=value)
                product_variations.append(variation)
            except ObjectDoesNotExist:
                pass

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))

    cart.save()

    is_cart_exist = cartItem.objects.filter(cart=cart, product=product).exists()
    if is_cart_exist:
        cart_item = cartItem.objects.filter(product=product, cart=cart)
        exist_var_list = []
        id = []
        for item in cart_item:
            existing_variation = item.variations.all()
            exist_var_list.append(list(existing_variation))
            id.append(item.id)

        if product_variations in exist_var_list:
            index = exist_var_list.index(product_variations)
            item_id = id[index]
            item = cartItem.objects.get(product=product, id=item_id)
            item.quantity += 1
            item.save()
        else:
            item = cartItem.objects.create(product=product, quantity=1, cart=cart)
            if len(product_variations) > 0:
                item.variations.clear()
                item.variations.add(*product_variations)
                item.save()
    else:
        cart_item = cartItem.objects.create(product=product, quantity=1, cart=cart)
        if len(product_variations) > 0:
            cart_item.variations.clear()
            cart_item.variations.add(*product_variations)
            cart_item.save()

    return redirect('cart_home')


def remove_cart(request, product_id, cart_item_id):
    """
    Removes a product from the cart. If the quantity is greater than one, decreases the quantity by one.
    Otherwise, removes the product from the cart.

    Args:
        request (HttpRequest): The HTTP request object.
        product_id (int): The ID of the product to remove from the cart.
        cart_item_id : The ID of the cart item to remove from the cart.
    Returns:
        HttpResponse: Redirects to the cart home page.
    """
    product = get_object_or_404(Product, id=product_id)
    cart = Cart.objects.get(cart_id=_cart_id(request))
    try:
        cart_item = get_object_or_404(cartItem, product=product, cart=cart, id=cart_item_id)

        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except ObjectDoesNotExist:
        pass

    return redirect('cart_home')


def delete_cart(request, product_id, cart_item_id):
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
    cart_item = get_object_or_404(cartItem, product=product, cart=cart, id=cart_item_id)
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
    tax = 0
    grand_total = 0
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
