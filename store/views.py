from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from carts.models import cartItem
from category.models import Category
from .models import Product
from carts.views import _cart_id
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def store_view(request, category_slug=None):
    category = None
    products = None
    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)
        product_count = products.count()
        paginator = Paginator(products, 1)
        page = request.GET.get('page')
        products_per_page = paginator.get_page(page)
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        product_count = products.count()
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        products_per_page = paginator.get_page(page)

    context = {
        'products': products_per_page,
        'product_count': product_count,
    }
    return render(request, 'store.html', context)


def details_view(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = cartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e
    context = {
        'single_product': single_product,
        'in_cart': in_cart
    }
    return render(request, 'products_details.html', context)


def search(request):
    if 'query' in request.GET:
        query = request.GET['query']
        if query:
            products = Product.objects.order_by('-created_at').filter(
                Q(prod_name__icontains=query) | Q(description__icontains=query)
            )
            product_count = products.count()
        else:
            products = Product.objects.order_by('-created_at')
            product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count
    }
    return render(request, 'store.html', context)
