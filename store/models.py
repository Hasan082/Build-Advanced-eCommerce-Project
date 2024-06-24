from django.db import models
from category.models import Category
from django.urls import reverse


class Product(models.Model):
    """
    Represents a product in the store.

    Attributes:
        prod_name (str): The name of the product.
        slug (str): The slugified version of the product name, used in URLs.
        description (str): Description of the product.
        price (Decimal): Price of the product.
        image (ImageField): Image of the product.
        stock (int): Number of units in stock.
        is_available (bool): Indicates if the product is available for purchase.
        category (ForeignKey): Category to which the product belongs.
        created_at (DateTimeField): Date and time when the product was created.
        updated_at (DateTimeField): Date and time when the product was last updated.
    """

    prod_name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='photos/products/')
    stock = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        """
        Returns the canonical URL for accessing a specific product.

        Returns:
            str: The URL of the product details page.
        """
        return reverse('product_details', args=[self.category.slug, self.slug])

    def __str__(self):
        """
        Returns a string representation of the product.

        Returns:
            str: The name of the product.
        """
        return self.prod_name


class VariationManager(models.Manager):
    """
    Custom manager for Variation model, providing filtered querysets.

    Methods:
        colors(): Returns queryset of variations categorized as 'color' and available.
        sizes(): Returns queryset of variations categorized as 'size' and available.
    """

    def colors(self):
        """
        Returns a queryset of variations categorized as 'color' and available.

        Returns:
            QuerySet: Variations with 'color' category and is_active=True.
        """
        return super(VariationManager, self).filter(variation_category='color', is_active=True)

    def sizes(self):
        """
        Returns a queryset of variations categorized as 'size' and available.

        Returns:
            QuerySet: Variations with 'size' category and is_active=True.
        """
        return super(VariationManager, self).filter(variation_category='size', is_active=True)


variation_category_choice = (
    ('color', 'color'),
    ('size', 'size'),
)


class Variation(models.Model):
    """
    Represents a variation of a product.

    Attributes:
        product (ForeignKey): The product to which this variation belongs.
        variation_category (str): Category of the variation ('color' or 'size').
        variation_value (str): Value of the variation (e.g., 'Red', 'Large').
        is_active (bool): Indicates if the variation is active.
        created_at (DateTimeField): Date and time when the variation was created.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(choices=variation_category_choice, max_length=100)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = VariationManager()

    def __str__(self):
        """
        Returns a string representation of the variation.

        Returns:
            str: The category of the variation ('color' or 'size').
        """
        return self.variation_category
