from django.http import Http404
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


def details_view(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    context = {'single_product': single_product}
    return render(request, 'products_details.html', context)
