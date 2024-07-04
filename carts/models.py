from django.db import models
from store.models import Product


class Cart(models.Model):
    """
    Represents a shopping cart.

    Attributes:
        cart_id (str): Unique identifier for the cart.
        date_added (DateTimeField): Timestamp when the cart was created.
    """

    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the cart.

        Returns:
            str: The cart_id of the cart.
        """
        return self.cart_id


class cartItem(models.Model):
    """
    Represents an item in a shopping cart.

    Attributes:
        product (ForeignKey): The product associated with this cart item.
        cart (ForeignKey): The cart to which this item belongs.
        quantity (int): The quantity of the product in the cart.
        is_active (bool): Indicates if the cart item is active.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        """
        Calculates the subtotal price for this cart item.

        Returns:
            Decimal: The subtotal price (product price * quantity).
        """
        return self.product.price * self.quantity

    def __str__(self):
        """
        Returns a string representation of the cart item.

        Returns:
            str: The name of the product.
        """
        return str(self.product)
