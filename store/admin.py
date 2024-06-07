from django.contrib import admin
from store.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('prod_name', 'price', 'stock', 'category', 'created_at', 'updated_at', 'is_available')
    list_filter = ('category', 'created_at', 'updated_at', 'is_available')
    prepopulated_fields = {
        'slug': ('prod_name',)
    }
    sortable_by = ('created_at', 'updated_at', 'is_available')
    search_fields = ('prod_name', 'price', 'stock', 'category', 'created_at', 'updated_at')


admin.site.register(Product, ProductAdmin)
