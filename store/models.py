from django.db import models
from category.models import Category


class Product(models.Model):
    prod_name       = models.CharField(max_length=255, unique=True)
    slug            = models.SlugField(max_length=255, unique=True)
    description     = models.TextField(max_length=500, blank=True)
    price           = models.DecimalField(max_digits=5, decimal_places=2)
    image           = models.ImageField(upload_to='photos/products/')
    stock           = models.PositiveIntegerField(default=0)
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.prod_name
