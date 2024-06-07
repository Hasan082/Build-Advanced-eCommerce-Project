from category.models import Category


def category_links(request):
    cat_links = Category.objects.all()
    return dict(cat_links=cat_links)
