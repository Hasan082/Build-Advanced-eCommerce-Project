from django.shortcuts import render  # Importing the render function to render templates.
from store.models import Product


# Defining the index view function which handles requests to the home page.
def index(request):
    # Get all product from Store with filter available
    products = Product.objects.all().filter(is_available=True)
    context = {'products': products}
    # The render function takes the request object, the template name, and an optional context dictionary.
    return render(request, 'index.html', context)
