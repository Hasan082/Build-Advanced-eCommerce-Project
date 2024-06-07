from django.shortcuts import render, get_object_or_404
from category.models import Category
from .models import Product


def store_view(request, category_slug=None):
    category = None
    products = None
    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)
    else:
        products = Product.objects.all().filter(is_available=True)

    context = {'products': products}
    return render(request, 'store.html', context)
