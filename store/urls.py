from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_view, name='store'),
    path('<slug:category_slug>/', views.store_view, name='product_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.details_view, name='product_details'),
]
