from django.contrib import admin

from category.models import Category
from store.models import Product, Variation


class ProductAdmin(admin.ModelAdmin):
    list_display = ('prod_name', 'price', 'stock', 'category', 'created_at', 'updated_at', 'is_available')
    list_filter = ('category', 'created_at', 'updated_at', 'is_available')
    prepopulated_fields = {
        'slug': ('prod_name',)
    }
    sortable_by = ('created_at', 'updated_at', 'is_available')
    search_fields = ('prod_name', 'price', 'stock', 'category', 'created_at', 'updated_at')


class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active', 'created_at',)
    list_editable = ('is_active',)
    list_filter = ('product','variation_category', 'variation_value',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
